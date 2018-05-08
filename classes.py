
class Node:
    def __str__(self):
        return self.print_tree()


class PStart(Node):
    def __init__(self):
        self.instructions = []

    def add_instruction(self, instruction):
        self.instructions.append(instruction)


class Instructions(Node):
    def __init__(self):
        self.instructions = []

    def add_instruction(self, instruction):
        self.instructions.append(instruction)


class Instruction(Node):
    def __init__(self, instruction):
        self.instruction = instruction


class InstructionEnd(Node):
    def __init__(self, instruction):
        self.instruction = instruction


class PrintInstruction(Node):
    def __init__(self, arg):
        self.print_arg = arg


class PrintIdList(Node):
    def __init__(self, ids, single_id):
        self.print_ids = ids
        self.single_id = single_id


class JumpStatement(Node):
    def __init__(self, jump_instr):
        self.jump_instr = jump_instr


class ContinueInstruction(Node):
    pass


class BreakInstruction(Node):
    pass


class ReturnInstruction(Node):
    def __init__(self, expr):
        self.expression = expr


class ComplexInstruction(Node):
    def __init__(self, complex_instruction):
        self.complex_instruction = complex_instruction


class ForLoop(Node):
    def __init__(self, id, range_from, range_to, instruction_block):
        self.id = id
        self.range_from = range_from
        self.range_to = range_to
        self.instruction_block = instruction_block


class WhileLoop(Node):
    def __init__(self, relation_expr, instruction_block):
        self.relation_expr = relation_expr
        self.instruction_block = instruction_block


class IfInstruction(Node):
    def __init__(self, relation_expr, if_instruction_block, else_instruction_block):
        self.relation_expr = relation_expr
        self.if_instruction_block = if_instruction_block
        self.else_instruction_block = else_instruction_block


class InstructionBlock(Node):
    def __init__(self, instructions):
        self.instructions = instructions


class Number(Node):
    def __init__(self, number):
        self.number = number


class ExpressionNumber(Node):
    def __init__(self, number):
        self.number = number


class ExpressionVar(Node):
    def __init__(self, id):
        self.id = id


class ExpressionAssignment(Node):
    def __init__(self, id, expr):
        self.id = id
        self.expr = expr


class ExpressionSum(Node):
    def __init__(self, left, right, operator):
        self.left = left
        self.right = right
        self.operator = operator


class ExpressionMul(Node):
    def __init__(self, left, right, operator):
        self.left = left
        self.right = right
        self.operator = operator


class ExpressionGroup(Node):
    def __init__(self, expr):
        self.expr = expr


class MatrixInitFunction(Node):
    def __init__(self, fun, args):
        self.fun = fun
        self.args = args


class MatrixElementModify(Node):
    def __init__(self, id, x, y, value):
        self.id = id
        self.x = x
        self.y = y
        self.value = value


class Negation(Node):
    def __init__(self, value):
        self.value = value


class MatrixTranspose(Node):
    def __init__(self, id, op):
        self.id = id
        self.op = op


class SpecialAssigment(Node):
    def __init__(self, left, right, operator):
        self.left = left
        self.right = right
        self.operator = operator


class MatrixBinaryOperation(Node):
    def __init__(self, left, right, operator):
        self.left = left
        self.right = right
        self.operator = operator


class MatrixInit(Node):
    def __init__(self, matrix_values):
        self.matrix_values = matrix_values


class MatrixValues(Node):
    def __init__(self, rows, row):
        self.rows = rows
        self.row = row


class Row(Node):
    def __init__(self, row, number):
        self.row = row
        self.number = number


class RelationOperator(Node):
    def __init__(self, relation_operator):
        self.relation_operator = relation_operator


class RelationExpression(Node):
    def __init__(self, left_expr, right_expr, relation_operator):
        self.left_expr = left_expr
        self.right_expr = right_expr
        self.relation_operator = relation_operator
