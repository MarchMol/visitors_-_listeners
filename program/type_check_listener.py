from SimpleLangListener import SimpleLangListener
from SimpleLangParser import SimpleLangParser
from custom_types import IntType, FloatType, StringType, BoolType

class TypeCheckListener(SimpleLangListener):

  def __init__(self):
    self.errors = []
    self.types = {}

  # Mod '%'
  def enterMod(self, ctx: SimpleLangParser.ModContext):
    pass
  def exitMod(self, ctx: SimpleLangParser.ModContext):
    left_type = self.types[ctx.expr(0)]
    right_type = self.types[ctx.expr(1)]
    if not (isinstance(left_type, IntType) and isinstance(right_type, IntType)):
      self.errors.append(f"Listener - Unsupported operand types for %: {left_type} and {right_type}")
    self.types[ctx] = IntType()
  
  # Exp '^'
  def enterExp(self, ctx: SimpleLangParser.ExpContext):
    pass
  def exitExp(self, ctx: SimpleLangParser.ExpContext):
    left_type = self.types[ctx.expr(0)]
    right_type = self.types[ctx.expr(1)]
    if not (isinstance(left_type, (IntType, FloatType)) and isinstance(right_type, (IntType, FloatType))):
      self.errors.append(f"Listener - Unsupported operand types for ^: {left_type} and {right_type}")
    self.types[ctx] = FloatType()
  
  # Mul '*'
  def enterMul(self, ctx: SimpleLangParser.MulContext):
    pass
  def exitMul(self, ctx: SimpleLangParser.MulContext):
    left_type = self.types[ctx.expr(0)]
    right_type = self.types[ctx.expr(1)]
    
    if self.is_valid_arithmetic_operation(left_type, right_type):
      self.types[ctx] = FloatType() if isinstance(left_type, FloatType) or isinstance(right_type, FloatType) else IntType()
    else: 
      if self.is_valid_bool_operation(left_type, right_type):
        self.types[ctx] = BoolType() 
      else:
        if self.is_valid_str_operation(left_type, right_type):
          self.types[ctx] = StringType() 
        else: 
          self.errors.append(f"Listener - Unsupported operand types for *: {left_type} and {right_type}")

  # Div '\'
  def enterDiv(self, ctx: SimpleLangParser.DivContext):
    pass
  def exitDiv(self, ctx: SimpleLangParser.DivContext):
    left_type = self.types[ctx.expr(0)]
    right_type = self.types[ctx.expr(1)]
    if not self.is_valid_arithmetic_operation(left_type, right_type):
      self.errors.append(f"Listener - Unsupported operand types for /: {left_type} and {right_type}")
    self.types[ctx] = FloatType() if isinstance(left_type, FloatType) or isinstance(right_type, FloatType) else IntType()

  # Add '+'
  def enterAdd(self, ctx: SimpleLangParser.AddContext):
    pass
  def exitAdd(self, ctx: SimpleLangParser.AddContext):
    left_type = self.types[ctx.expr(0)]
    right_type = self.types[ctx.expr(1)]
    
    if self.is_valid_arithmetic_operation(left_type, right_type):
      self.types[ctx] = FloatType() if isinstance(left_type, FloatType) or isinstance(right_type, FloatType) else IntType()
    else:
      if self.is_valid_bool_operation(left_type, right_type):
        self.types[ctx] = BoolType()
      else: 
        self.errors.append(f"Listener - Unsupported operand types for +: {left_type} and {right_type}")

  # Sub '-'
  def enterSub(self, ctx: SimpleLangParser.SubContext):
    pass
  def exitSub(self, ctx: SimpleLangParser.SubContext):
    left_type = self.types[ctx.expr(0)]
    right_type = self.types[ctx.expr(1)]
    if not self.is_valid_arithmetic_operation(left_type, right_type):
      self.errors.append(f"Unsupported operand types for -: {left_type} and {right_type}")
    self.types[ctx] = FloatType() if isinstance(left_type, FloatType) or isinstance(right_type, FloatType) else IntType()

  # Types listeners
  def enterInt(self, ctx: SimpleLangParser.IntContext):
    self.types[ctx] = IntType()

  def enterFloat(self, ctx: SimpleLangParser.FloatContext):
    self.types[ctx] = FloatType()

  def enterString(self, ctx: SimpleLangParser.StringContext):
    self.types[ctx] = StringType()

  def enterBool(self, ctx: SimpleLangParser.BoolContext):
    self.types[ctx] = BoolType()

  def enterParens(self, ctx: SimpleLangParser.ParensContext):
    pass

  def exitParens(self, ctx: SimpleLangParser.ParensContext):
    self.types[ctx] = self.types[ctx.expr()]

  ### CHECK OPERATIONS
  # Boolean Operation check
  def is_valid_bool_operation(self, left_type, right_type):
    if isinstance(left_type, BoolType) and isinstance(right_type, BoolType):
      return True
    return False
  
  # String Operation check
  def is_valid_str_operation(self, left_type, right_type):
    if isinstance(left_type, StringType) and isinstance(right_type, IntType):
      return True
    return False

  # Arithmetic Operation Check
  def is_valid_arithmetic_operation(self, left_type, right_type):
    if isinstance(left_type, (IntType, FloatType)) and isinstance(right_type, (IntType, FloatType)):
      return True
    return False