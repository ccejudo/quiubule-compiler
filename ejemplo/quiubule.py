from utils import yacc
from quiubule_lexer import tokens, lexer

def quiubule(input_file):
    # Read the input file
    with open(input_file, "r") as f:
        data = f.read()

    print(tokens)

    def p_dvar(p):
        'definicion : COSO CARACTER PYC'
        print("definición de coso")

    def p_dvar2(p):
        'definicion : COSO CARACTER IGUAL ENTERO PYC'
        print("definición de coso")
        print(p[0], p[1], p[2], p[3])

    # Error rule for syntax errors
    def p_error(p):
        print("Syntax error in input!")
    # Build the parser
    parser = yacc.yacc()

    try:
        s = "coso num = 10; coso foo;"
    except EOFError:
        exit(1)
    if not s: exit(1)
    parser.parse(s)
    """
    # Call lexer
    lexer.input(data)
    while True:
        tok = lexer.token()
        if not tok: break
        print(tok)
    """

if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Usage: %s <input file>" % sys.argv[0])
        sys.exit(1)

    quiubule(sys.argv[1])