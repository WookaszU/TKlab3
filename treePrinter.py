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
    def print_tree(self, indent=0):
        raise Exception("printTree not defined in class " + self.__class__.__name__)

    # to chyba niepotrzebne
    @addToClass(classes.PStart)
    def print_tree(self, indent=0):
        tree = ""
        for instruction in reversed(self.instructions):
            tree += instruction.print_tree(indent) if instruction.print_tree(indent) is not None else ""

        return tree

    @addToClass(classes.Instructions)
    def print_tree(self, indent=0):
        tree = ""
        for instruction in reversed(self.instructions):
            tree += instruction.print_tree(indent) if instruction.print_tree(indent) is not None else ""

        return tree

    @addToClass(classes.Instruction)
    def print_tree(self, indent=0):
        tree = ""
        for i in self.instructions:
            tree += i.print_tree(indent) if i.print_tree(indent) is not None else ""
        return tree

    # to chyba niepotrzebne
    @addToClass(classes.InstructionEnd)
    def print_tree(self, indent=0):
        return self.instruction.print_tree(indent)

    @addToClass(classes.PrintInstruction)
    def print_tree(self, indent=0):
        return delimiter_char * indent + "PRINT\n" + self.print_arg.print_tree(indent + 1)

    @addToClass(classes.PrintIdList)
    def print_tree(self, indent=0):
        if self.print_ids is None:
            return self.single_id.print_tree(indent)
        else:
            return self.single_id.print_tree(indent) + self.print_ids.print_tree(indent)

    @addToClass(classes.JumpStatement)
    def print_tree(self, indent=0):
        return self.jump_instr.print_tree(indent)

    @addToClass(classes.ContinueInstruction)
    def print_tree(self, indent=0):
        return delimiter_char * indent + "CONTINUE\n"

    @addToClass(classes.BreakInstruction)
    def print_tree(self, indent=0):
        return delimiter_char * indent + "BREAK\n"

    @addToClass(classes.ReturnInstruction)
    def print_tree(self, indent=0):
        if self.expression is None:
            return delimiter_char * indent + "RETURN\n"
        else:
            return delimiter_char * indent + "RETURN\n" + self.expression.print_tree(indent + 1)

    @addToClass(classes.ComplexInstruction)
    def print_tree(self, indent=0):
        return self.complex_instruction.print_tree(indent)

    @addToClass(classes.ForLoop)
    def print_tree(self, indent=0):
        tree = ""
        tree += delimiter_char * indent + "FOR\n"
        tree += delimiter_char * (indent + 1) + self.id + "\n"
        tree += delimiter_char * (indent + 1) + "RANGE\n"
        tree += delimiter_char * (indent + 2) + str(self.range_from) + "\n"
        tree += delimiter_char * (indent + 2) + str(self.range_to) + "\n"
        tree += self.instruction_block.print_tree(indent + 1)
        return tree

    @addToClass(classes.WhileLoop)
    def print_tree(self, indent=0):
        tree = delimiter_char * indent + "WHILE\n"
        tree += self.relation_expr.print_tree(indent + 1) + self.instruction_block.print_tree(indent + 1)
        return tree

    @addToClass(classes.IfInstruction)
    def print_tree(self, indent=0):
        tree = delimiter_char * indent + "IF\n"
        tree += self.relation_expr.print_tree(indent+1)
        tree += delimiter_char * indent + "THEN\n"
        tree += self.if_instruction_block.print_tree(indent + 1)
        tree += delimiter_char * indent + "ELSE\n" + self.else_instruction_block.print_tree(indent + 1)

        return tree

    @addToClass(classes.InstructionBlock)
    def print_tree(self, indent=0):
        return self.instructions.print_tree(indent)

    @addToClass(classes.Number)
    def print_tree(self, indent=0):
        return delimiter_char * indent + str(self.number) + "\n"

    @addToClass(classes.ExpressionNumber)
    def print_tree(self, indent=0):
        return self.number.print_tree(indent)

    @addToClass(classes.ExpressionVar)
    def print_tree(self, indent=0):
        return delimiter_char * indent + self.id

    @addToClass(classes.ExpressionAssigment)
    def print_tree(self, indent=0):
        tree = "=\n"
        tree += (indent+1) * delimiter_char + self.id + "\n"
        tree += self.expr.print_tree(indent + 1)
        return tree

    @addToClass(classes.ExpressionSum)
    def print_tree(self, indent=0):
        tree = ""
        tree += indent * delimiter_char + self.operator + "\n"
        tree += self.left.print_tree(indent + 1) + self.right.print_tree(indent + 1)
        return tree

    @addToClass(classes.ExpressionMul)
    def print_tree(self, indent=0):
        tree = ""
        tree += indent * delimiter_char + self.operator + "\n"
        tree += self.left.print_tree(indent + 1) + self.right.print_tree(indent + 1)
        return tree

    # TODO -----------------------------------------------------
    @addToClass(classes.ExpressionGroup)
    def print_tree(self, indent=0):
        return self.expr.print_tree(indent)

    @addToClass(classes.MatrixInitFunction)
    def print_tree(self, indent=0):
        return delimiter_char * indent + str(self.fun) + "\n" + delimiter_char * (indent+1) + str(self.args) + "\n"

    @addToClass(classes.MatrixElementModify)
    def print_tree(self, indent=0):
        tree = "=\n"
        tree += delimiter_char * (indent + 1) + "REF\n"
        tree += (indent + 2) * delimiter_char + self.id + "\n"
        tree += (indent + 2) * delimiter_char + str(self.x) + "\n"
        tree += (indent + 2) * delimiter_char + str(self.y) + "\n"
        tree += (indent + 1) * delimiter_char + str(self.value) + "\n"
        return tree

    @addToClass(classes.Negation)
    def print_tree(self, indent=0):
        return delimiter_char * indent + "-" + "\n" + self.value.print_tree(indent + 1)

    @addToClass(classes.MatrixTranspose)
    def print_tree(self, indent=0):
        tree = delimiter_char * indent + "TRANSPOSE" + "\n"
        tree += delimiter_char * (indent + 1) + self.id + "\n"
        return tree

    @addToClass(classes.SpecialAssigment)
    def print_tree(self, indent=0):
        tree = ""
        tree += indent * delimiter_char + self.operator + "\n"
        tree += self.left.print_tree(indent + 1) + self.right.print_tree(indent + 1)
        return tree

    @addToClass(classes.MatrixBinaryOperation)
    def print_tree(self, indent=0):
        tree = "\n"
        tree += indent * delimiter_char + self.operator + "\n"
        tree += self.left.print_tree(indent + 1) + "\n" + self.right.print_tree(indent + 1)
        return tree

    @addToClass(classes.MatrixInit)
    def print_tree(self, indent=0):
        return delimiter_char * indent + "MATRIX\n" + self.matrix_values.print_tree(indent)

    @addToClass(classes.MatrixValues)
    def print_tree(self, indent=0):
        if self.rows is None:
            return delimiter_char * (indent + 1) + "VECTOR\n" + self.row.print_tree(indent + 2)
        else:
            return delimiter_char * (indent + 1) + "VECTOR\n" + self.row.print_tree(indent + 2) + self.rows.print_tree(indent)

    @addToClass(classes.Row)
    def print_tree(self, indent=0):
        if self.row is None:
            return self.number.print_tree(indent)
        else:
            return self.number.print_tree(indent) + self.row.print_tree(indent)

    @addToClass(classes.RelationOperator)
    def print_tree(self, indent=0):
        return str(self.relation_operator)

    @addToClass(classes.RelationExpression)
    def print_tree(self, indent=0):
        tree = ""
        tree += indent * delimiter_char + str(self.relation_operator) + "\n"
        tree += self.left_expr.print_tree(indent + 1) + "\n"
        tree += self.right_expr.print_tree(indent + 1)
        return tree

