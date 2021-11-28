from utils import yacc

from quiubule_lexer import tokens

import sys

memory = {
    "cosos" : {},
    "juntitos": {},
    "chafiretes": {},
    "funciones": {}
}

# ---------------------- Instrucciones (S) ------------------------ #

def p_instrucciones(p):
    '''instrucciones : instruccion instrucciones
                     | lambda'''

def p_instruccion(p):
    '''instruccion : declaraciones
                   | asignaciones
                   | condicionales
                   | entradas_salidas
                   | llamada_funciones'''


# ------------------------ Declaraciones -------------------------- #


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


# ------------------------- ASIGNACIONES -------------------------- #


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
    '''a_struct : ID PUNTO ID IGUAL ENTERO PYC'''

def p_avar(p):
                        # TODO: Cambiar por DATO
    '''a_var : ID IGUAL ENTERO PYC
             | ID IGUAL ID PYC'''

# --- Errores --- #

def p_id_error(p):
    '''a_arreglo : ID error'''
    print("Se esperaba una declaración o una asignación. Línea:",
          p.lineno(len(p)-1)
    )
    sys.exit()

def p_a_arreglo_error(p):
    '''a_arreglo : ID CORCHETE_IZQ error
                 | ID CORCHETE_IZQ ENTERO error
                 | ID CORCHETE_IZQ ENTERO CORCHETE_DER error
                 | ID CORCHETE_IZQ ENTERO CORCHETE_DER IGUAL error
                 | ID CORCHETE_IZQ ENTERO CORCHETE_DER IGUAL ENTERO error
    '''
    print("La asignacion al arreglo es incorrecta. Línea:",
          p.lineno(len(p)-1)
    )
    sys.exit()

def p_astruct_error(p):
    '''a_struct : ID error
                | ID PUNTO error
                | ID PUNTO ID error
                | ID PUNTO ID IGUAL error
                | ID PUNTO ID IGUAL ENTERO error
    '''
    print("La asignacion a la estructura es incorrecta. Línea:",
          p.lineno(len(p)-1)
    )
    sys.exit()

def p_avar_error(p):
    '''a_var : ID error
             | ID IGUAL error PYC
             | ID IGUAL ENTERO error
    '''
    print("La asignacion a la variable es incorrecta. Línea:",
          p.lineno(len(p)-1)
    )
    sys.exit()

# ------------------------- CONDICIONALES ------------------------- #

def p_condicionales(p):
    '''condicionales : condicional condicionales
                     | lambda'''

def p_condicional(p):
    '''condicional : if
                   | if_else'''

def p_if(p):
    "if : CHANCE PAREN_IZQ condiciones PAREN_DER BRACKET_IZQ instrucciones BRACKET_DER"

def p_if_else(p):
    '''if_else : if HIJOLE BRACKET_IZQ instrucciones BRACKET_DER'''

def p_condiciones(p):
    '''condiciones : condicion OPLOG condiciones
                   | condicion'''

def p_condicion(p):
    '''condicion : condicion_logica
                 | OPNOT condicion_logica'''

def p_condicion_logica(p):
    #TODO: ¿Cambiar ENTERO por NUM?
    '''condicion_logica : BOOL
                        | ENTERO OPREL ENTERO
                        | CARACTER OPREL CARACTER
                        | BOOL OPREL BOOL
                        | ID OPREL ID'''

# --- Errores --- #

def p_if_error(p):
    '''if : CHANCE error
          | CHANCE PAREN_IZQ error
          | CHANCE PAREN_IZQ condiciones error
          | CHANCE PAREN_IZQ condiciones PAREN_DER error
          | CHANCE PAREN_IZQ condiciones PAREN_DER BRACKET_IZQ error
          | CHANCE PAREN_IZQ condiciones PAREN_DER BRACKET_IZQ instrucciones error
    '''
    print("La declaración de chance es incorrecta. Línea:",
          p.lineno(len(p)-1)
    )
    sys.exit()

def p_if_else_error(p):
    '''if_else : if error
               | if HIJOLE error
               | if HIJOLE BRACKET_IZQ error BRACKET_DER
               | if HIJOLE BRACKET_IZQ instrucciones error
    '''
    print("La declaración de hijole es incorrecta. Línea:",
          p.lineno(len(p)-1)
    )
    sys.exit()

def p_condicion_logica_error(p):
    # TODO: ¿Cambiar ENTERO por NUM?
    '''condicion_logica : ENTERO error
                        | CARACTER error
                        | BOOL error
                        | ID error'''
    print("El símbolo",
          p[2].value,
          "ubicado en la línea",
          p.lineno(2),
          "es incorrecto en dicha posición.",
          "Se esperaba un operador lógico válido."
    )
    sys.exit()

# ---------------------- ENTRADAS Y SALIDAS ----------------------- #

def p_entradas_salidas(p):
    '''entradas_salidas : entrada_salida entradas_salidas
                        | lambda'''

def p_entrada_salida(p):
    '''entrada_salida : lee
                      | escribe
                      | escribe_nl'''

def p_lee(p):
    '''lee : LEETE lista_variables PYC'''

def p_escribe(p):
    '''escribe : ESCRIBETE lista_variables PYC'''

def p_escribe_nl(p):
    '''escribe_nl : ESCRIBETEL lista_variables PYC'''

def p_lista_variables(p):
    '''lista_variables : entrada COMA lista_variables
                       | entrada'''

def p_entrada(p):
    # TODO: ¿ARREGLO?
    # TODO: Cambiar ENTERO por DATO
    '''entrada : ENTERO
               | ID'''

# --- Errores --- #

def p_lee_error(p):
    '''lee : LEETE error
           | LEETE lista_variables error
    '''
    print("La declaración de leete es incorrecta. Línea:",
          p.lineno(len(p)-1)
    )
    sys.exit()

def p_escribe_error(p):
    '''escribe : ESCRIBETE error
               | ESCRIBETE lista_variables error
    '''
    print("La declaración de escribete es incorrecta. Línea:",
          p.lineno(len(p)-1)
    )
    sys.exit()

def p_escribe_nl_error(p):
    '''escribe_nl : ESCRIBETEL error
                  | ESCRIBETEL lista_variables error
    '''
    print("La declaración de escribetel es incorrecta. Línea:",
          p.lineno(len(p)-1)
    )
    sys.exit()

def p_lista_variables_errpr(p):
    '''lista_variables : entrada error'''
    print("La declaración de la lista de variables es incorrecta. Línea:",
          p.lineno(len(p)-1)
    )
    sys.exit()

# --------------------- LLAMADA A FUNCIONES ----------------------- #

def p_llamada_funciones(p):
    '''llamada_funciones : llamada_funcion llamada_funciones
                         | lambda'''

def p_llamada_funcion(p):
    # TODO: Definir IDFuncion
    '''llamada_funcion : ID PAREN_IZQ ll_params PAREN_DER PYC'''

def p_ll_params(p):
    # TODO: Revisar grámatica para ll_params
    '''ll_params : ll_param
                 | ll_param COMA ll_params
                 | lambda'''

def p_ll_param(p):
    # TODO: Definir DATO
    '''ll_param : ID'''

# --- Errores --- #

def p_llamada_funcion_error(p):
    '''llamada_funcion : ID error
                       | ID PAREN_IZQ error PAREN_DER PYC
                       | ID PAREN_IZQ ll_params error PYC
                       | ID PAREN_IZQ ll_params PAREN_DER error
    '''
    print("La declaración de la función es incorrecta. Línea:",
          p.lineno(len(p)-1)
    )
    sys.exit()

def p_ll_params_error(p):
    '''ll_params : ll_param error'''
    print("La declaración de los parámetros de la función es incorrecta. Línea:",
          p.lineno(len(p)-1)
    )
    sys.exit()


def p_lambda(p):
    '''lambda : '''

def p_error(p):
    print("¡Error de sintáxis! en línea", p.lineno)

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
coso key;
chance(5 <= 10){
    chance("hola" != "adios"){
        key = 5;
    }hijole{
        coso new_key = 10;
    }
}
leete id, 5, 10;
coso name_1 = "Max";
coso name_2 = "Lewis";
hello(name_1; name_2);
'''
parser.parse(s)
print(memory)
