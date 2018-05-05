import sys
import ply.yacc as yacc
import Mparser
from treePrinter import TreePrinter


if __name__ == '__main__':

    try:
        filename = sys.argv[1] if len(sys.argv) > 1 else "examplesZ3/example1.m"
        file = open(filename, "r")
    except IOError:
        print("Cannot open {0} file".format(filename))
        sys.exit(0)

    # Mparser = Mparser()
    # parser = yacc.yacc(module=Mparser)
    # text = file.read()
    # ast = parser.parse(text, lexer=Mparser.scanner)
    # ast.printTree()

    parser = Mparser.parser
    text = file.read()
    ast = parser.parse(text, lexer=Mparser.scanner.lexer)
    tree = ast.print_tree()
    print(tree)
