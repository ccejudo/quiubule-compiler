from utils import yacc

from quiubule_lexer import tokens

variables = {
    "cosos" : {},
    "juntitos": {},
    "chafiretes": {}
}

def p_instrucciones(p):
    '''instrucciones : instruccion instrucciones
                     | lambda'''

def p_instruccion(p):
    '''instruccion : declaraciones'''

def p_declaraciones(p):
    '''declaraciones : declaracion declaraciones
                     | lambda'''

def p_declaracion(p):
    '''declaracion : dvar'''

def p_dvar(p):
    '''dvar : COSO CARACTER PYC
                  | COSO CARACTER IGUAL REAL PYC
                  | COSO CARACTER IGUAL ENTERO PYC'''
    val = None
    if len(p) >= 5:
        val = p[4]

    if p[2] not in variables['cosos']:
        variables["cosos"][p[2]] = val
    else:
        print("Error: variable", p[2], "ya definida en la línea", p.lineno(1))
        exit(1)

def p_dvar_error(p):
    'dvar : COSO error PYC'
    print("Error al definir caracter en la línea", p.lineno(1))

def p_lambda(p):
    '''lambda : ''' 

def p_error(p):
    print("Syntax error in input!")

# Build the parser
parser = yacc.yacc()


s = '''coso hello;
coso foo = 10;
coso oo = 10.45;
'''
parser.parse(s)
print(variables)
