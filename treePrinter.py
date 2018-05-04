from __future__ import print_function
import classes


def addToClass(cls):

    def decorator(func):
        setattr(cls,func.__name__,func)
        return func
    return decorator


delimiter_char = '| '

class TreePrinter:

    @addToClass(classes.Node)
    def printTree(self, indent=0):
        raise Exception("printTree not defined in class " + self.__class__.__name__)

    @addToClass(classes.Instructions)
    def printTree(self, indent=0):
        pass
        # fill in the body

    @addToClass(classes.Instruction)
    def printTree(self, indent=0):
        tree = ""
        for i in self.instructions:
            tree += i.print_tree(indent) if i.print_tree(indent) is not None else ""
        return tree

    @addToClass(classes.InstructionEnd)
    def printTree(self, indent=0):
        return self.instruction.print_tree(indent)

    @addToClass(classes.PrintInstruction)
    def printTree(self, indent=0):
        return delimiter_char * indent + "PRINT\n" + self.print_arg.print_tree(indent + 1)

    @addToClass(classes.PrintIdList)
    def printTree(self, indent=0):
        if self.print_ids is None:
            return self.single_id.print_tree(indent)
        else:
            return self.single_id.print_tree(indent) + self.print_ids.print_tree(indent)

    @addToClass(classes.JumpStatement)
    def printTree(self, indent=0):
        pass
        # fill in the body TODO?????????????????????????????????????????

    @addToClass(classes.ContinueInstruction)
    def printTree(self, indent=0):
        return delimiter_char * indent + "CONTINUE\n"

    @addToClass(classes.BreakInstruction)
    def printTree(self, indent=0):
        return delimiter_char * indent + "BREAK\n"

    @addToClass(classes.ReturnInstruction)
    def printTree(self, indent=0):
        if self.expression is None:
            return delimiter_char * indent + "RETURN\n"
        else:
            return delimiter_char * indent + "RETURN\n" + self.expression.print_tree(indent + 1)

    @addToClass(classes.ComplexInstruction)
    def printTree(self, indent=0):
        return self.complex_instruction.print_tree(indent)

    @addToClass(classes.ForLoop)
    def printTree(self, indent=0):
        result = ""
        result += delimiter_char * indent + "FOR\n"
        result += self.range.print_tree(indent + 1) + self.instruction_block.print_tree(indent + 1)
        return result

    @addToClass(classes.WhileLoop)
    def printTree(self, indent=0):
        result = delimiter_char * indent + "WHILE\n"
        result += self.relation_expr.print_tree(indent + 1) + self.instruction_block.print_tree(indent + 1)
        return result

    @addToClass(classes.IfInstruction)
    def printTree(self, indent=0):
        result = delimiter_char * indent + "IF\n"
        result += self.relation_expr.print_tree(indent + 1) + self.if_instruction_block.print_tree(indent + 1)
        result += "" if self.else_instruction_block is None else delimiter_char * indent + "ELSE\n" + self.else_instruction_block.print_tree(
            indent + 1)

        return result

    @addToClass(classes.InstructionBlock)
    def printTree(self, indent=0):
        return self.instructions.print_tree(indent)

    @addToClass(classes.Number)
    def printTree(self, indent=0):
        return self.number.print_tree(indent)

    @addToClass(classes.ExpressionNumber)
    def printTree(self, indent=0):
        return self.number.print_tree(indent)

    @addToClass(classes.ExpressionVar)
    def printTree(self, indent=0):
        return self.id.print_tree(indent)

    @addToClass(classes.ExpressionAssigment)
    def printTree(self, indent=0):
        pass

    @addToClass(classes.ExpressionSum)
    def printTree(self, indent=0):
        pass
        # fill in the body

    @addToClass(classes.ExpressionMul)
    def printTree(self, indent=0):
        pass
        # fill in the body

    @addToClass(classes.ExpressionGroup)
    def printTree(self, indent=0):
        pass
        # fill in the body

    @addToClass(classes.MatrixInitFunction)
    def printTree(self, indent=0):
        return delimiter_char * indent + str(self.fun) + "\n" + self.args.print_tree(indent + 1)


    @addToClass(classes.MatrixElementModify)
    def printTree(self, indent=0):
        pass
        # fill in the body

    @addToClass(classes.Negation)
    def printTree(self, indent=0):
        pass
        # fill in the body

    @addToClass(classes.MatrixTranspose)
    def printTree(self, indent=0):
        pass
        # fill in the body

    @addToClass(classes.SpecialAssigment)
    def printTree(self, indent=0):
        pass
        # fill in the body

    @addToClass(classes.MatrixBinaryOperation)
    def printTree(self, indent=0):
        pass
        # fill in the body

    @addToClass(classes.MatrixInit)
    def printTree(self, indent=0):
        pass
        # fill in the body

    @addToClass(classes.MatrixValues)
    def printTree(self, indent=0):
        if self.rows is None:
            return delimiter_char * indent + "row\n" + self.row.print_tree(indent + 1)
        else:
            return delimiter_char * indent + "row\n" + self.row.print_tree(indent + 1) + self.rows.print_tree(indent)

    @addToClass(classes.Row)
    def printTree(self, indent=0):
        if self.row is None:
            return self.number.print_tree(indent)
        else:
            return self.number.print_tree(indent) + self.row.print_tree(indent)

    @addToClass(classes.RelationOperator)
    def printTree(self, indent=0):
        pass
        # fill in the body

    @addToClass(classes.RelationExpression)
    def printTree(self, indent=0):
        pass
        # fill in the body

