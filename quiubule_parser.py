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


# ------------------------- Asignaciones -------------------------- #


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


def p_error_after_id(p):
    '''a_arreglo : ID error'''
    print("Error! El símbolo",
          p[2].value,
          "ubicado en la línea",
          p.lineno(2),
          "es incorrecto en dicha posición. Se esperaba un = un [ o un ."
    )

# ---- Errores en la asignación de arreglo ---#

def p_a_arreglo_error_after_corchete_izq(p):
    '''a_arreglo : ID CORCHETE_IZQ error'''
    print("Error! El símbolo",
          p[3].value,
          "ubicado en la línea",
          p.lineno(3),
          "es incorrecto en dicha posición. Se esperaba un entero"
    )

def p_a_arreglo_error_after_index(p):
    '''a_arreglo : ID CORCHETE_IZQ ENTERO error'''
    print("Error! El símbolo",
          p[4].value,
          "ubicado en la línea",
          p.lineno(4),
          "es incorrecto en dicha posición. Se esperaba un ]"
    )

def p_a_arreglo_error_corchete_der(p):
    '''a_arreglo : ID CORCHETE_IZQ ENTERO CORCHETE_DER error'''
    print("Error! El símbolo",
          p[5].value,
          "ubicado en la línea",
          p.lineno(5),
          "es incorrecto en dicha posición. Se esperaba un ="
    )

def  p_a_arreglo_error_after_equal(p):
    '''a_arreglo : ID CORCHETE_IZQ ENTERO CORCHETE_DER IGUAL error'''
    print("Error! El símbolo",
          p[6].value,
          "ubicado en la línea",
          p.lineno(6),
          "es incorrecto en dicha posición.",
          "Se esperaba un valor válido para asignar"
    )

def  p_a_arreglo_error_after_data(p):
                                                                    # TODO: Cambiar por DATO
    '''a_arreglo : ID CORCHETE_IZQ ENTERO CORCHETE_DER IGUAL ENTERO error'''
    print("Error! El símbolo",
          p[7].value,
          "ubicado en la línea",
          p.lineno(7),
          "es incorrecto en dicha posición.",
          "Se esperaba un ;"
    )


def p_astruct(p):
                           #TODO: Resolver STRUCT_ID
                                          #TODO: Cambiar por DATO
    '''a_struct : ID PUNTO ID IGUAL ENTERO PYC'''

# ---- Errores en la asignación de struct ----#

def p_astruct_error_after_id(p):
    '''a_struct : ID error'''
    print("Error! El símbolo",
          p[2].value,
          "ubicado en la línea",
          p.lineno(2),
          "es incorrecto en dicha posición."
    )

def p_astruct_error_after_dot(p):
    '''a_struct : ID PUNTO error'''
    print("Error! El símbolo",
          p[3].value,
          "ubicado en la línea",
          p.lineno(3),
          "es incorrecto en dicha posición.",
          "Se esperaba una estructura válida"
    )

def p_astruct_error_after_struct_id(p):
                           # TODO: Resolver STRUCT_ID
    '''a_struct : ID PUNTO ID error'''
    print("Error! El símbolo",
          p[4].value,
          "ubicado en la línea",
          p.lineno(4),
          "es incorrecto en dicha posición.",
          "Se esperaba ="
    )

def p_astruct_error_after_equal(p):
    '''a_struct : ID PUNTO ID IGUAL error'''
    print("Error! El símbolo",
          p[5].value,
          "ubicado en la línea",
          p.lineno(5),
          "es incorrecto en dicha posición.",
          "Se esperaba un valor válido para asignar"
    )

def p_astruct_error_after_data(p):
                                    # TODO: Cambiar por DATO
    '''a_struct : ID PUNTO ID IGUAL ENTERO error'''
    print("Error! El símbolo",
          p[6].value,
          "ubicado en la línea",
          p.lineno(6),
          "es incorrecto en dicha posición.",
          "Se esperaba un ;"
    )


def p_avar(p):
                        # TODO: Cambiar por DATO
    '''a_var : ID IGUAL ENTERO PYC
             | ID IGUAL ID PYC'''

# ------ Errores en la asignación de var -----#

def p_avar_error_after_id(p):
    '''a_var : ID error'''
    print("Error! El símbolo",
          p[2].value,
          "ubicado en la línea",
          p.lineno(2),
          "es incorrecto en dicha posición."
    )

def p_avar_error_after_equal(p):
    '''a_var : ID IGUAL error'''
    print("Error! El símbolo",
          p[3].value,
          "ubicado en la línea",
          p.lineno(3),
          "es incorrecto en dicha posición.",
          "Se esperaba un valor válido para asignar"
    )

def p_avar_error_after_data(p):
                        # TODO: Cambiar por DATO
    '''a_var : ID IGUAL ENTERO error'''
    print("Error! El símbolo",
          p[4].value,
          "ubicado en la línea",
          p.lineno(4),
          "es incorrecto en dicha posición.",
          "Se esperaba un ;"
    )


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
    print("Error! La declaración de chance es incorrecta. Línea:",
          p.lineno(len(p)-1)
    )
    sys.exit()

def p_if_else_error(p):
    '''if_else : if error
               | if HIJOLE error
               | if HIJOLE BRACKET_IZQ error BRACKET_DER
               | if HIJOLE BRACKET_IZQ instrucciones error
    '''
    print("Error! La declaración de hijole es incorrecta. Línea:",
          p.lineno(len(p)-1)
    )
    sys.exit()

def p_condicion_logica_error(p):
    # TODO: ¿Cambiar ENTERO por NUM?
    '''condicion_logica : ENTERO error
                        | CARACTER error
                        | BOOL error
                        | ID error'''
    print("Error! El símbolo",
          p[2].value,
          "ubicado en la línea",
          p.lineno(2),
          "es incorrecto en dicha posición.",
          "Se esperaba un operador lógico válido."
    )
    sys.exit()

# ---------------------- Entradas y salidas ----------------------- #

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


# --------------------- Llamada a funciones ----------------------- #

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


def p_lambda(p):
    '''lambda : '''

def p_error(p):
    print("Syntax error in input!")

# Build the parser
parser = yacc.yacc()


s = '''
chance(1 < 2){
    coso a = 10;
}false
'''
parser.parse(s)
print(memory)
