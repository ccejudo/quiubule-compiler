from utils import yacc

from quiubule_lexer import tokens, lexer

def p_instruction(p):
    '''instruction : instruction definicion
                   | definicion'''

def p_dvar(p):
    '''definicion : COSO CARACTER PYC
                  | COSO CARACTER IGUAL ENTERO PYC'''

def p_dvar_error(p):
    'definicion : COSO error PYC'
    print("Error al definir caracter en la línea", p.lineno(2))

def p_error(p):
    print("Syntax error in input!")

# Build the parser
parser = yacc.yacc()


s = '''
coso hello;
coso 10;
'''
parser.parse(s)
