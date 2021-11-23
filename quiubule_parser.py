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
                  | COSO CARACTER IGUAL REAL PYC
                  | COSO CARACTER IGUAL ENTERO PYC'''
    val = None
    if len(p) >= 5:
        val = p[4]

    if p[2] not in variables['cosos']:
        variables["cosos"][p[2]] = val
    else:
        print("Error: variable", p[2], "ya definida. Línea:", p.lineno(1))
        exit(1)

def p_dvar_error(p):
    'definicion : COSO error PYC'
    print("Error al definir caracter en la línea", p.lineno(1))

def p_error(p):
    print("Syntax error in input!")

# Build the parser
parser = yacc.yacc()


s = '''coso hello;
coso foo = 10;
coso foo = 10.45;
'''
parser.parse(s)
print(variables)
