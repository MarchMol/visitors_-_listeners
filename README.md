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

## 3. Conflictos de Tipos
asdasd

