# Construccion de Compiladores - <br>Laboratorio 2 - Sistema de tipos con ANTLR

## <a href="youtube.com">Video de prueba</a>

## 1. Funcionamiento
La verificacion de tipos en ANTLR comienza por la defincion de operaciones en el g4, en este caso, en la produccion expr. Con la parte de op=regex podemos diferenciar los diferentes tipos de operaciones y con el # podemos indicar el nombre que le assignamos. Asimismo, esto puede servir para la definicion de tipos como se ven en las producciones a simbolos terminales.
```
expr: expr op=('*'|'/') expr       # MulDiv
    | expr op=('+'|'-') expr       # AddSub
    | expr op='%' expr             # Mod
    | INT                          # Int
    | FLOAT                        # Float
    | STRING                       # String
    | BOOL                         # Bool
    | '(' expr ')'                 # Parens
    ;
```
### Visitor

Para la version con visitor se hace uso del TypeCheckVisitor, el cual busca hacer la verificacion de tipos en vase a visitas dentro del arbol semantico. En este caso, se hace uso de tipos customizados ubicados en custom_types.py que siguen la convencion de nombre de "AlgoType" donde se establecen clases que solo regresan un texto que indica su tipo, como es el caso de int a continuacion
``` 
class IntType(Type):
  def __str__(self):
    return "int"
```
Con los nombres establecidos en la parte del g4 como "MulDiv" o "AddSub" podemos expander estos nombres y asociar visitores para las operaciones, asi como los tipos de datos. Esto nos ayuda a describir reglas para las operaciones y sus tipos de retornos. Como ejemplo MulDiv, que primero recoge el tipo de sus hijos izquieda y derecha en las producciones expr, y luego evlua sus tipos para especificar el resultado
```
  def visitMulDiv(self, ctx: SimpleLangParser.MulDivContext):
    left_type = self.visit(ctx.expr(0))
    right_type = self.visit(ctx.expr(1))
    
    if isinstance(left_type, (IntType, FloatType)) and isinstance(right_type, (IntType, FloatType)):
        return FloatType() if isinstance(left_type, FloatType) or isinstance(right_type, FloatType) else IntType()
    else:
        raise TypeError("Unsupported operand types for * or /: {} and {}".format(left_type, right_type))
```
Para tipos unitarios (es decir, no operandos) la revision es individual y solo se evalua el contexto del nodo 
```
  def visitInt(self, ctx: SimpleLangParser.IntContext):
    return IntType()
```
### Listener
La verificacion de tipos con listeners es distinta a visitors, pues no se cuenta con control sobre la navegacion del arbol. Esto trae el beneficio que este metodo es pasivo y requiere menor computo, pero es necesario mantener una constancia de los tipos traversados, lo que trae myor uso de memoria.

Para implementar un Type Cheker con listeners, es necesario describir una funcion para la entrada a un nodo y una para la salida. Estas funciones no tienen tipo de retorno, sino que solo almacenamos la informacion de tipos en el contexto. En la entrada de un nodo operacion no es necesario hacer nada, pues en este importa mas la salida, pues en este punto ya con la informacion de los hijos podemos verificar los tipos. Podemos ver que en la funcion de salida de una operacion evaluamos una condicion y podemos agregar el tipo correcto dado nuestro contexto, y si se falla podemos agregar el error a los logs
```
// Entrada
  def enterOperation(self, ctx: SimpleLangParser.OperationContext):
    pass

// Salida
  def exitOperation(self, ctx: SimpleLangParser.OperationContext):
    left_type = self.types[ctx.expr(0)]
    right_type = self.types[ctx.expr(1)]
    if condition(left_type, right_type):
      self.types[ctx] = CorrectType()
    else:
      self.errors.append(f"Unsupported operand types for operation: {left_type} and {right_type}")
```

## 2. Operaciones adicionales
Se decidio agregar las operaciones de Modulo y Exponencial ya que serian sencillas de implementar a las demas operaciones matematica ya establecidas.
- Cambios en g4: se agregaron las producciones de 'expr' para que contengan esto
```
    | expr op='%' expr             # Mod
    | expr op='^' expr             # Exp
```
Asimismo, se deben agregar los verificadores de tipo para listener y visitor de estas operaciones.

- Visitor:
Para Mod se realizo la siguiente funcion, la cual solo acepta que lo argumentos de ambos lados sean enteros y regresa tipo entero. Esta implementacion se vio apropiada debido a que la operacion de Modulo tiende a ser usada unicamente en valores discretos.

```
  def visitMod(self, ctx: SimpleLangParser.ModContext):
    left_type = self.visit(ctx.expr(0))
    right_type = self.visit(ctx.expr(1))
    if isinstance(left_type, IntType) and isinstance(right_type, IntType):
        return IntType()
    else:
        raise TypeError("Unsupported operand types for %: {} and {}".format(left_type, right_type))
```
Para exponencial se realizo lo siguiente, donde los argumentos a ambos lados, representativos de la base y exponente, pueden ser tanto decimales como enteros, pero el resultado siempre sera de punto flotante. Considerando donde la exponenciacion se haga por series de taylor, se considera apropiado que el resultado sea solo decimal

```
  def visitExp(self, ctx: SimpleLangParser.ModContext):
    left_type = self.visit(ctx.expr(0))
    right_type = self.visit(ctx.expr(1))
    
    if isinstance(left_type, (IntType, FloatType)) and isinstance(right_type, (IntType, FloatType)):
        return FloatType()
    else:
        raise TypeError("Unsupported operand types for ^: {} and {}".format(left_type, right_type))
```
- Listener
Para el listener se evalua la misma idea lo cual se ve a continuacion.

```
  # Mod '%'
  def enterMod(self, ctx: SimpleLangListener.ModContext):
    pass
  def exitMod(self, ctx: SimpleLangListener.ModContext):
    left_type = self.types[ctx.expr(0)]
    right_type = self.types[ctx.expr(1)]
    if not (isinstance(left_type, IntType) and isinstance(right_type, IntType)):
      self.errors.append(f"Unsupported operand types for %: {left_type} and {right_type}")
    self.types[ctx] = IntType()
  
  # Exp '^'
  def enterExp(self, ctx: SimpleLangListener.ExpContext):
    pass
  def exitExp(self, ctx: SimpleLangListener.ExpContext):
    left_type = self.types[ctx.expr(0)]
    right_type = self.types[ctx.expr(1)]
    if not (isinstance(left_type, (IntType, FloatType)) and isinstance(right_type, (IntType, FloatType))):
      self.errors.append(f"Unsupported operand types for ^: {left_type} and {right_type}")
    self.types[ctx] = FloatType()
```

## 3. Conflictos de Tipos

Para los conflictos de tipos que se deben agregar, se me ocurrieron las siguientes ideas para implementar
1. ACEPTAR str * int, que deberia de devolver una repeticion de la cadena por la cantidad establecia, es decir, un tipo String.
2. ACEPTAR suma booleana, que seria el equivalente a un OR
3. ACEPTAR multiplicacion booleana, que seria el equivalente a un AND


- Visitor
Primero, fue necesario separar la funcion que manejaba a la multiplicacion y division para agregar esta funcionalidad especial, por tanto ahora Mul y Div ahora seran producciones separadas y tendran funciones separadas, igual que Add y Sub. 


- Listener

