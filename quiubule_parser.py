from utils import yacc

from quiubule_lexer import tokens

variables = {
    "cosos" : {},
    "juntitos": {},
    "chafiretes": {}
}

def p_instruction(p):
    '''instruction : instruction definicion
                   | definicion'''

def p_dvar(p):
    '''definicion : COSO CARACTER PYC
                  | COSO CARACTER IGUAL ENTERO PYC'''
    val = None
    if len(p) >= 5:
        val = p[4]

    variables["cosos"][p[2]] = val

def p_dvar_error(p):
    'definicion : COSO error PYC'
    print("Error al definir caracter en la línea", p.lineno(1))

def p_error(p):
    print("Syntax error in input!")

# Build the parser
parser = yacc.yacc()


s = '''coso hello;
coso foo = 10;
'''
parser.parse(s)
print(variables)
