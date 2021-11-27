from utils import yacc

from quiubule_lexer import tokens

memory = {
    "cosos" : {},
    "juntitos": {},
    "chafiretes": {},
    "funciones": {}
}

def p_instrucciones(p):
    '''instrucciones : instruccion instrucciones
                     | lambda'''

def p_instruccion(p):
    '''instruccion : declaraciones
                   | asignaciones'''

def p_declaraciones(p):
    '''declaraciones : declaracion declaraciones
                     | lambda'''

def p_declaracion(p):
    '''declaracion : dvar
                  | darreglo
                  | dstruct
                  | dfuncion'''

def p_dvar(p):
    '''dvar : COSO ID PYC
            | COSO ID IGUAL REAL PYC
            | COSO ID IGUAL ENTERO PYC
            | COSO ID IGUAL CARACTER PYC'''
    val = None
    if len(p) >= 5:
        val = p[4]

    if p[2] not in memory['cosos']:
        memory["cosos"][p[2]] = val
    else:
        print("Error: variable", p[2], "ya definida en la línea", p.lineno(1))
        exit(1)

def p_dvar_error(p):
    'dvar : COSO error PYC'
    print("Error al definir coso en la línea", p.lineno(1))

def p_darreglo(p):
    '''darreglo : JUNTITOS ID PYC
                  | JUNTITOS ID IGUAL BRACKET_IZQ darr_body BRACKET_DER PYC'''

def p_darr_body(p):
    '''darr_body : darr_dato COMA darr_body
                  | lambda'''

def p_darr_dato(p):
    '''darr_dato : CARACTER
                  | ENTERO
                  | BOOL
                  | REAL'''

def p_dstruct(p):
    '''dstruct : CHAFIRETE ID BRACKET_IZQ dstruct_body BRACKET_DER PYC'''

def p_dstruct_body(p):
    '''dstruct_body : dvar dstruct_body
                  | darreglo dstruct_body
                  | lambda'''

def p_dfuncion(p):
    '''dfuncion : RIFATE ID PAREN_IZQ dparams PAREN_DER BRACKET_IZQ instrucciones BRACKET_DER'''

def p_dparams(p):
    '''dparams : dparam COMA dparams
                  | lambda'''
def p_dparam(p):
    '''dparam : ID'''

def p_asignaciones(p):
    '''asignaciones : asignacion asignaciones
                     | lambda'''

def p_asignacion(p):
    '''asignacion : a_arreglo
                  | a_struct
                  | a_var'''

def p_a_arreglo(p):
                                                             #TODO: Cambiar por DATO
    '''a_arreglo : ID CORCHETE_IZQ ENTERO CORCHETE_DER IGUAL ENTERO PYC
                 | ID CORCHETE_IZQ ENTERO CORCHETE_DER IGUAL ID PYC'''

def p_astruct(p):
                           #TODO: Resolver STRUCT_ID
                                          #TODO: Cambiar por DATO
    '''a_struct : ID PUNTO CARACTER IGUAL ENTERO PYC'''

def p_avar(p):
                        # TODO: Cambiar por DATO
    '''a_var : ID IGUAL ENTERO PYC
             | ID IGUAL ID PYC'''

def p_lambda(p):
    '''lambda : '''

def p_error(p):
    print("Syntax error in input!")

# Build the parser
parser = yacc.yacc()


s = '''coso hello;
coso foo = 10;
coso oo = 10.45;
juntitos hi;
juntitos a = {1,2,3,4,};
chafirete b {
    coso h = 5;
    coso j = 3;
    juntitos l = {1,2,3,4,};
    };
rifate f(a,b,c,){
    coso m = 5;
    juntitos n = {1,2,3,4,};
    chafirete c {
    coso p = 5;
    };
}
arr[0] = 10;
'''
parser.parse(s)
print(memory)
