from SimpleLangParser import SimpleLangParser
from SimpleLangVisitor import SimpleLangVisitor
from custom_types import IntType, FloatType, StringType, BoolType

class TypeCheckVisitor(SimpleLangVisitor):
  # Mod '%' operation rules
  def visitMod(self, ctx: SimpleLangParser.ModContext):
    left_type = self.visit(ctx.expr(0))
    right_type = self.visit(ctx.expr(1))
    if isinstance(left_type, IntType) and isinstance(right_type, IntType):
        return IntType()
    else:
        raise TypeError("Unsupported operand types for %: {} and {}".format(left_type, right_type))
      
  # Exponential '^' operation rules
  def visitExp(self, ctx: SimpleLangParser.ModContext):
    left_type = self.visit(ctx.expr(0))
    right_type = self.visit(ctx.expr(1))
    
    if isinstance(left_type, (IntType, FloatType)) and isinstance(right_type, (IntType, FloatType)):
        return FloatType()
    else:
        raise TypeError("Unsupported operand types for ^: {} and {}".format(left_type, right_type))
  
  # Multiplication '*' operation rules
  def visitMul(self, ctx: SimpleLangParser.MulContext):
    left_type = self.visit(ctx.expr(0))
    right_type = self.visit(ctx.expr(1))
    
    if isinstance(left_type, (IntType, FloatType)) and isinstance(right_type, (IntType, FloatType)):
        return FloatType() if isinstance(left_type, FloatType) or isinstance(right_type, FloatType) else IntType()
    else:
      if isinstance(left_type, StringType) and isinstance(right_type, IntType):
        return StringType()
      else:
        if isinstance(left_type, BoolType) and isinstance(right_type, BoolType):
          return BoolType()
        raise TypeError("Unsupported operand types for *: {} and {}".format(left_type, right_type))
      
  def visitDiv(self, ctx: SimpleLangParser.DivContext):
    left_type = self.visit(ctx.expr(0))
    right_type = self.visit(ctx.expr(1))
    if isinstance(left_type, (IntType, FloatType)) and isinstance(right_type, (IntType, FloatType)):
        return FloatType() if isinstance(left_type, FloatType) or isinstance(right_type, FloatType) else IntType()
    else:
        raise TypeError("Unsupported operand types for /: {} and {}".format(left_type, right_type))


  def visitAdd(self, ctx: SimpleLangParser.AddContext):
    left_type = self.visit(ctx.expr(0))
    right_type = self.visit(ctx.expr(1))
    if isinstance(left_type, (IntType, FloatType)) and isinstance(right_type, (IntType, FloatType)):
        return FloatType() if isinstance(left_type, FloatType) or isinstance(right_type, FloatType) else IntType()
    else:
      if isinstance(left_type, BoolType) and isinstance(right_type, BoolType):
        return BoolType()
      else:
        raise TypeError("Unsupported operand types for +: {} and {}".format(left_type, right_type))
      
  def visitSub(self, ctx: SimpleLangParser.SubContext):
    left_type = self.visit(ctx.expr(0))
    right_type = self.visit(ctx.expr(1))
    
    if isinstance(left_type, (IntType, FloatType)) and isinstance(right_type, (IntType, FloatType)):
        return FloatType() if isinstance(left_type, FloatType) or isinstance(right_type, FloatType) else IntType()
    else:
        raise TypeError("Unsupported operand types for -: {} and {}".format(left_type, right_type))
  
  def visitInt(self, ctx: SimpleLangParser.IntContext):
    return IntType()

  def visitFloat(self, ctx: SimpleLangParser.FloatContext):
    return FloatType()

  def visitString(self, ctx: SimpleLangParser.StringContext):
    return StringType()

  def visitBool(self, ctx: SimpleLangParser.BoolContext):
    return BoolType()

  def visitParens(self, ctx: SimpleLangParser.ParensContext):
    return self.visit(ctx.expr())