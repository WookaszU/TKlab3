#!/usr/bin/python

import ply.yacc as yacc
import scanner
import classes

symtab = {}
tokens = scanner.tokens
scanner = scanner

precedence = (
   ("nonassoc", 'ONLYIF'),
   ("nonassoc", 'ELSE'),
   ("right", '=', 'ADDASSIGN', 'SUBASSIGN', 'MULASSIGN', 'DIVASSIGN'),
   ("nonassoc", '<', '>', 'E', 'NE', 'GE', 'LE'),
   ("left", '+', '-', 'DOTADD', 'DOTSUB'),
   ("left", '*', '/', 'DOTMUL', 'DOTDIV'),
   ("left", "TRANSPOSE"),
   ("right", 'UMINUS'),
)


def p_error(p):
    if p:
        print("Syntax error at line {0}: LexToken({1}, '{2}')".format(p.lineno, p.type, p.value))
    else:
        print("Unexpected end of input")

# to jest zle na dole ostatnia linijka na 100 % bo complexow nie przyjmuje
# ma problem z ostatnia instrukcja z listy, nie uwzgldnia jej
# niby teraz dziala, ale to jest kijowe mega i pewnie nie zadziala jak ostatnia jest complex_instr
# moze trzeba by bylo dodac jakas klase ogolna zawierajaca INSTRUCTION i COMPLEX_INSTR
def p_start(p):
    """start : INSTRUCTION
             | INSTRUCTION start
             | COMPLEX_INS start
             | COMPLEX_INS"""
    if len(p) == 3:
        p[0] = classes.PStart() if p[2] is None else p[2]
        p[0].add_instruction(p[1])
    else:
        p[0] = classes.Instructions()
        p[0].add_instruction(p[1])


def p_instructions(p):
    """INSTRUCTIONS : INSTRUCTION
                    | INSTRUCTION INSTRUCTIONS"""
    if len(p) == 3:
        p[0] = classes.Instructions() if p[2] is None else p[2]
        p[0].add_instruction(p[1])
    else:
        p[0] = classes.Instructions()


def p_instruction_end(p):
    """INSTRUCTION : INSTRUCTION ';'"""
    p[0] = classes.InstructionEnd(p[1])


def p_print(p):
    """INSTRUCTION : PRINT IDS ';'
                  | PRINT STRING ';'
                  """
    p[0] = classes.PrintInstruction(p[2])


def p_ids(p):
    """IDS : ID ',' IDS
            | ID
            """
    if len(p) > 2:
        p[0] = classes.PrintIdList(p[3], p[1])
    else:
        p[0] = classes.PrintIdList(None, p[1])


def p_jump_statement(p):
    """INSTRUCTION : JUMP_CONTINUE
                   | JUMP_BREAK
                   | JUMP_RETURN"""
    p[0] = classes.JumpStatement(p[1])


def p_jump_statement_continue(p):
    """JUMP_CONTINUE : CONTINUE ';'"""
    pass


def p_jump_statement_break(p):
    """JUMP_BREAK : BREAK ';'"""
    pass


def p_jump_statement_return(p):
    """JUMP_RETURN : RETURN EXPRESSION ';'"""

    if len(p) == 3:
        p[0] = classes.ReturnInstruction(p[2])
    else:
        p[0] = classes.ReturnInstruction(None)


def p_complex_instruction(p):
    """COMPLEX_INS : FORLOOP
                   | WHILELOOP
                   | IFELSE """
    p[0] = classes.ComplexInstruction(p[1])


def p_for_loop(p):
    """FORLOOP : FOR ID '=' INTNUM ':' INTNUM '{' INSTR_BLOCK  '}'
                  | FOR ID '=' INTNUM ':' ID '{' INSTR_BLOCK  '}'
                  | FOR ID '=' ID ':' INTNUM '{' INSTR_BLOCK  '}'
                  | FOR ID '=' ID ':' ID '{' INSTR_BLOCK  '}'
                  """
    p[0] = classes.ForLoop(p[6], p[8])


def p_while_loop(p):
    """WHILELOOP : WHILE '(' RELATION_EXPR ')' '{' INSTR_BLOCK  '}' """
    p[0] = classes.WhileLoop(p[3], p[6])


def p_if_else(p):
    """IFELSE : IF '(' RELATION_EXPR ')' INSTR_BLOCK %prec ONLYIF
                | IF '(' RELATION_EXPR ')' INSTR_BLOCK ELSE INSTR_BLOCK """
    if len(p) == 6:
        p[0] = classes.IfInstruction(p[3], p[5], None)
    else:
        p[0] = classes.IfInstruction(p[3], p[5], p[7])


def p_instructions_block(p):
    """INSTR_BLOCK : COMPLEX_INS
                    | INSTRUCTIONS """
    p[0] = classes.InstructionBlock(p[1])


def p_number(p):
    """NUMBER : INTNUM
              | FLOATNUM"""
    p[0] = classes.Number(p[1])


def p_expression_number(p):
    """EXPRESSION : NUMBER"""
    p[0] = classes.ExpressionNumber(p[1])


def p_expression_var(p):
    """EXPRESSION : ID"""
    p[0] = classes.ExpressionVar(p[1])


def p_expression_assignment(p):
    """INSTRUCTION : ID '=' EXPRESSION"""
    p[0] = classes.ExpressionAssigment(p[1], p[3])


def p_expression_sum(p):
    """EXPRESSION : EXPRESSION '+' EXPRESSION
                  | EXPRESSION '-' EXPRESSION"""
    p[0] = classes.ExpressionSum(p[1], p[3], p[2])


def p_expression_mul(p):
    """EXPRESSION : EXPRESSION '*' EXPRESSION
                  | EXPRESSION '/' EXPRESSION"""
    p[0] = classes.ExpressionMul(p[1], p[3], p[2])



def p_expression_group(p):
    """EXPRESSION : '(' EXPRESSION ')'"""
    p[0] = classes.ExpressionGroup(p[2])


def p_matrix_special_init(p):
    """EXPRESSION : ZEROS '(' INTNUM ')'
                  | ONES '(' INTNUM ')'
                  | EYE '(' INTNUM ')' """
    p[0] = classes.MatrixInitFunction(p[1], p[3])


# TODO ???????????????? czy to jest ok?
def p_matrix_element_modify(p):
    """INSTRUCTION : ID '[' INTNUM ',' INTNUM ']' '=' NUMBER"""
    p[0] = classes.MatrixElementModify(p[1], p[3], p[5], p[8])


def p_negation(p):
    """EXPRESSION : '-' EXPRESSION %prec UMINUS"""
    p[0] = classes.Negation(p[2])


# TODO  ???????? co jako 2 argument?
def p_matrix_transpose(p):
    """EXPRESSION : ID TRANSPOSE"""
    p[0] = classes.MatrixTranspose(p[1], p[2])


def p_special_assignment(p):
    """INSTRUCTION : ID ADDASSIGN ID
                   | ID SUBASSIGN ID
                   | ID MULASSIGN ID
                   | ID DIVASSIGN ID"""
    p[0] = classes.SpecialAssigment(p[1], p[3], p[2])


def p_matrix_binary_operations(p):
    """EXPRESSION : ID DOTADD ID
                  | ID DOTSUB ID
                  | ID DOTMUL ID
                  | ID DOTDIV ID"""
    p[0] = classes.MatrixBinaryOperation(p[1], p[3], p[2])


def p_matrix_init(p):
    """EXPRESSION : '[' MATRIX_VALUES ']'
        """
    p[0] = classes.MatrixInit(p[2])


def p_matrix_values(p):
    """MATRIX_VALUES : ROW
                     | ROW ';' MATRIX_VALUES
        """
    if len(p) > 2:
        p[0] = classes.MatrixValues(p[3], p[1])
    else:
        p[0] = classes.MatrixValues(None, p[1])


def p_row(p):
    """ROW : NUMBER
           | NUMBER ',' ROW
           """
    if len(p) > 2:
        p[0] = classes.Row(p[3], p[1])
    else:
        p[0] = classes.Row(None, p[1])


def p_relation_op(p):
    """RELATION_OP : E
                    | '<'
                    | '>'
                    | LE
                    | GE
                    | NE
                    """
    p[0] = classes.RelationOperator(p[1])


def p_expression_relation(p):
    """RELATION_EXPR : EXPRESSION RELATION_OP EXPRESSION
        """
    p[0] = classes.RelationExpression(p[1], p[3], p[2])


parser = yacc.yacc()

