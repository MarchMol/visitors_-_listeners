# Generated from SimpleLang.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .SimpleLangParser import SimpleLangParser
else:
    from SimpleLangParser import SimpleLangParser

# This class defines a complete listener for a parse tree produced by SimpleLangParser.
class SimpleLangListener(ParseTreeListener):

    # Enter a parse tree produced by SimpleLangParser#prog.
    def enterProg(self, ctx:SimpleLangParser.ProgContext):
        pass

    # Exit a parse tree produced by SimpleLangParser#prog.
    def exitProg(self, ctx:SimpleLangParser.ProgContext):
        pass


    # Enter a parse tree produced by SimpleLangParser#stat.
    def enterStat(self, ctx:SimpleLangParser.StatContext):
        pass

    # Exit a parse tree produced by SimpleLangParser#stat.
    def exitStat(self, ctx:SimpleLangParser.StatContext):
        pass


    # Enter a parse tree produced by SimpleLangParser#Div.
    def enterDiv(self, ctx:SimpleLangParser.DivContext):
        pass

    # Exit a parse tree produced by SimpleLangParser#Div.
    def exitDiv(self, ctx:SimpleLangParser.DivContext):
        pass


    # Enter a parse tree produced by SimpleLangParser#Add.
    def enterAdd(self, ctx:SimpleLangParser.AddContext):
        pass

    # Exit a parse tree produced by SimpleLangParser#Add.
    def exitAdd(self, ctx:SimpleLangParser.AddContext):
        pass


    # Enter a parse tree produced by SimpleLangParser#Float.
    def enterFloat(self, ctx:SimpleLangParser.FloatContext):
        pass

    # Exit a parse tree produced by SimpleLangParser#Float.
    def exitFloat(self, ctx:SimpleLangParser.FloatContext):
        pass


    # Enter a parse tree produced by SimpleLangParser#Sub.
    def enterSub(self, ctx:SimpleLangParser.SubContext):
        pass

    # Exit a parse tree produced by SimpleLangParser#Sub.
    def exitSub(self, ctx:SimpleLangParser.SubContext):
        pass


    # Enter a parse tree produced by SimpleLangParser#Mod.
    def enterMod(self, ctx:SimpleLangParser.ModContext):
        pass

    # Exit a parse tree produced by SimpleLangParser#Mod.
    def exitMod(self, ctx:SimpleLangParser.ModContext):
        pass


    # Enter a parse tree produced by SimpleLangParser#Bool.
    def enterBool(self, ctx:SimpleLangParser.BoolContext):
        pass

    # Exit a parse tree produced by SimpleLangParser#Bool.
    def exitBool(self, ctx:SimpleLangParser.BoolContext):
        pass


    # Enter a parse tree produced by SimpleLangParser#Mul.
    def enterMul(self, ctx:SimpleLangParser.MulContext):
        pass

    # Exit a parse tree produced by SimpleLangParser#Mul.
    def exitMul(self, ctx:SimpleLangParser.MulContext):
        pass


    # Enter a parse tree produced by SimpleLangParser#Parens.
    def enterParens(self, ctx:SimpleLangParser.ParensContext):
        pass

    # Exit a parse tree produced by SimpleLangParser#Parens.
    def exitParens(self, ctx:SimpleLangParser.ParensContext):
        pass


    # Enter a parse tree produced by SimpleLangParser#String.
    def enterString(self, ctx:SimpleLangParser.StringContext):
        pass

    # Exit a parse tree produced by SimpleLangParser#String.
    def exitString(self, ctx:SimpleLangParser.StringContext):
        pass


    # Enter a parse tree produced by SimpleLangParser#Exp.
    def enterExp(self, ctx:SimpleLangParser.ExpContext):
        pass

    # Exit a parse tree produced by SimpleLangParser#Exp.
    def exitExp(self, ctx:SimpleLangParser.ExpContext):
        pass


    # Enter a parse tree produced by SimpleLangParser#Int.
    def enterInt(self, ctx:SimpleLangParser.IntContext):
        pass

    # Exit a parse tree produced by SimpleLangParser#Int.
    def exitInt(self, ctx:SimpleLangParser.IntContext):
        pass



del SimpleLangParser