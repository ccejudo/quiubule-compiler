from utils import yacc

from quiubule_lexer import tokens

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
                | ciclos
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
            | COSO ID IGUAL dato PYC'''
    val = None
    if len(p) > 5:
        dato_val, dato_type = p[4]
        if dato_type == "ID":
            if dato_val not in memory['cosos']:
                print("Error: variable", dato_val, "no definida. Línea:", p.lineno(1))
                exit(1)
        val = (dato_val, dato_type)

    if p[2] not in memory['cosos']:
        memory['cosos'][p[2]] = val
    else:
        print("Error: variable", p[2], "ya definida. Línea:", p.lineno(1))
        exit(1)
    
    p[0] = [p[2]]

def p_dvar_error(p):
    'dvar : COSO error PYC'
    print("Error al definir coso. Línea", p.lineno(1))

def p_darreglo(p):
    '''darreglo : JUNTITOS ID CORCHETE_IZQ ENTERO CORCHETE_DER PYC
                | JUNTITOS ID IGUAL BRACKET_IZQ darr_body BRACKET_DER PYC'''
    val_arr = []

    if len(p) == 8:
        val_arr = p[5]
    else:
        val_arr = ["null" for _ in range(p[4])]

    if p[2] not in memory['juntitos']:
        for i in range(len(val_arr)):
            if val_arr[i] == "ID":
                if val_arr[i-1] not in memory['cosos']:
                    print("Error: variable", val_arr[i-1], "no definida. Línea:", p.lineno(1))
                    exit(1)
        try:
            val_arr.remove("ID")
        except:
            pass
        memory['juntitos'][p[2]] = list(filter(None, val_arr))
    else:
        print("Error: juntitos", p[2], "ya definido. Línea:", p.lineno(1))
        exit(1)

    p[0] = [p[2]]

def p_darr_body(p):
    '''darr_body : dato COMA darr_body
                | dato
                | lambda'''

    p[0] = []        
    for i in range(1,len(p)):
        if p[i] != "," and p[i]:
            p[0] += p[i]

def p_dstruct(p):
    '''dstruct : CHAFIRETE ID BRACKET_IZQ dstruct_body BRACKET_DER PYC'''

    if p[2] not in memory['chafiretes']:
        memory['chafiretes'][p[2]] = p[4]
    else:
        print("Error: chafirete", p[2], "ya definido. Línea:", p.lineno(1))
        exit(1)
    
    p[0] = p[2]

def p_dstruct_body(p):
    '''dstruct_body : dvar dstruct_body
                | darreglo dstruct_body
                | lambda'''
    
    p[0] = []
    for i in range(1,len(p)):
        if p[i]:
            p[0] += p[i]

def p_dfuncion(p):
    '''dfuncion : RIFATE ID PAREN_IZQ dparams PAREN_DER BRACKET_IZQ instrucciones BRACKET_DER
                | RIFATE ID PAREN_IZQ dparams PAREN_DER BRACKET_IZQ instrucciones AHITEVA dato PYC BRACKET_DER'''

    if p[2] not in memory['funciones']:
        memory['funciones'][p[2]] = p[4]
    else:
        print("Error: funcion", p[2], "ya definida. Línea:", p.lineno(1))
        exit(1)
    
    p[0] = p[2]

def p_dparams(p):
    '''dparams : dparam COMA dparams
                | dparam
                | lambda'''
    p[0] = []
    for i in range(1,len(p)):
        if p[i] != "," and p[i]:
            p[0] += p[i]

def p_dparam(p):
    '''dparam : ID'''
    p[0] = p[1]

# ------------------------- ASIGNACIONES -------------------------- #

def p_asignaciones(p):
    '''asignaciones : asignacion asignaciones
                    | lambda'''

def p_asignacion(p):
    '''asignacion : a_arreglo
                | a_struct
                | a_var'''

def p_a_arreglo(p):
    '''a_arreglo : ID CORCHETE_IZQ ENTERO CORCHETE_DER IGUAL dato PYC'''
    if p[1] not in memory['juntitos']:
        print("Error: arreglo", p[1], "no definido. Línea:", p.lineno(1))
        exit(1)
    if p[3] > len(memory['juntitos'][p[1]]):
        print("Error: arreglo", p[1], "no tiene tantos elementos. Línea:", p.lineno(1))
        exit(1)
    memory['juntitos'][p[1]][p[3]-1] = (p[6][0], p[6][1])

def p_astruct(p):
    '''a_struct : ID PUNTO ID IGUAL dato PYC'''

    if p[1] not in memory['chafiretes']:
        print("Error: chafirete", p[1], "no definido. Línea:", p.lineno(1))
        exit(1)
    if p[3] not in memory['chafiretes'][p[1]]:
        print("Error: campo", p[3], "no definido en chafirete", p[1] + ".","Línea:", p.lineno(1))
        exit(1)

def p_avar(p):
    '''a_var : ID IGUAL dato PYC'''
    if p[1] not in memory['cosos']:
        print("Error: variable", p[1], "no fue definida. Línea:", p.lineno(1))
        exit(1)
    memory['cosos'][p[1]] = (p[3][0], p[3][1])

# --- Errores --- #

def p_id_error(p):
    '''a_arreglo : ID error'''
    print("Se esperaba una declaración o una asignación. Línea:",
        p.lineno(len(p)-1)
    )
    exit(1)

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
    exit(1)

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
    exit(1)

def p_avar_error(p):
    '''a_var : ID error
            | ID IGUAL error PYC
            | ID IGUAL ENTERO error
    '''
    print("La asignacion a la variable es incorrecta. Línea:",
        p.lineno(len(p)-1)
    )
    exit(1)

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
    '''condicion_logica : BOOL
                        | dato OPREL dato'''
    try:
      if memory["cosos"][p[1][0]][1] != memory["cosos"][p[3][0]][1]:
        print("Los tipos de comparación son incompatibles, en", p[3][0], p[2][0], p[1][0])
        exit(1)
    except:
      pass

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
    exit(1)

def p_if_else_error(p):
    '''if_else : if error
            | if HIJOLE error
            | if HIJOLE BRACKET_IZQ error BRACKET_DER
            | if HIJOLE BRACKET_IZQ instrucciones error
    '''
    print("La declaración de hijole es incorrecta. Línea:",
        p.lineno(len(p)-1)
    )
    exit(1)

def p_condicion_logica_error(p):
    '''condicion_logica : num error
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
    exit(1)

# ---------------------- CICLOS ----------------------------------- #

def p_ciclos(p):
  '''ciclos : ciclo ciclos
              | lambda'''

def p_ciclo(p):
  '''ciclo : for
          | lambda'''

def p_for(p):
  '''for : CHAMBEA PAREN_IZQ inicializacion PYC condicion PYC actualizacion PAREN_DER BRACKET_IZQ instrucciones BRACKET_DER
        | CHAMBEA PAREN_IZQ inicializacion PYC PYC actualizacion PAREN_DER BRACKET_IZQ instrucciones BRACKET_DER '''

def p_inicializacion(p):
  '''inicializacion : COSO ID IGUAL ENTERO
                    | COSO ID IGUAL ID
                    | ID IGUAL ID
                    | lambda'''

def p_actualizacion(p):
  '''actualizacion : ID OPAR ENTERO
                    | ID IGUAL ID OPAR ENTERO
                    | ID IGUAL ID OPAR ID
                    | lambda '''

# Errores ciclos

def p_inicializacion_error(p):
  '''inicializacion : COSO error
                    | COSO ID error
                    | COSO ID IGUAL error
                    | ID error
                    | ID IGUAL error
                    '''
  print("La declaración de chambea inicializacion es incorrecta. Línea:",
      p.lineno(len(p)-1)
  )
  exit(1)

def p_actualizacion_error(p):
  '''
  actualizacion : ID error
                | ID OPAR error
                | ID IGUAL error
                | ID IGUAL ID error
                | ID IGUAL ID OPAR error
  '''
  print("La declaración de chambea actualización es incorrecta. Línea:",
      p.lineno(len(p)-1)
  )
  exit(1)

# def p_for_error(p):
#   '''for : CHAMBEA error
#         | CHAMBEA PAREN_IZQ error
#         | CHAMBEA PAREN_IZQ inicializacion error
#         | CHAMBEA PAREN_IZQ inicializacion PYC error
#         | CHAMBEA PAREN_IZQ inicializacion PYC condicion error
#         | CHAMBEA PAREN_IZQ inicializacion PYC condicion PYC error
#         | CHAMBEA PAREN_IZQ inicializacion PYC condicion PYC actualizacion error
#         | CHAMBEA PAREN_IZQ inicializacion PYC condicion PYC actualizacion PAREN_DER error
#         | CHAMBEA PAREN_IZQ inicializacion PYC condicion PYC actualizacion PAREN_DER BRACKET_IZQ error
#         | CHAMBEA PAREN_IZQ inicializacion PYC condicion PYC actualizacion PAREN_DER BRACKET_IZQ instrucciones error
#     '''

#   print("La declaración de chambea es incorrecta. Línea:",
#       p.lineno(len(p)-1)
#   )
#   exit(1)

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
    '''entrada : dato'''

# --- Errores --- #

def p_lee_error(p):
    '''lee : LEETE error
        | LEETE lista_variables error
    '''
    print("La declaración de leete es incorrecta. Línea:",
        p.lineno(len(p)-1)
    )
    exit(1)

def p_escribe_error(p):
    '''escribe : ESCRIBETE error
            | ESCRIBETE lista_variables error
    '''
    print("La declaración de escribete es incorrecta. Línea:",
        p.lineno(len(p)-1)
    )
    exit(1)

def p_escribe_nl_error(p):
    '''escribe_nl : ESCRIBETEL error
                | ESCRIBETEL lista_variables error
    '''
    print("La declaración de escribetel es incorrecta. Línea:",
        p.lineno(len(p)-1)
    )
    exit(1)

def p_lista_variables_error(p):
    '''lista_variables : entrada error'''
    print("La declaración de la lista de variables es incorrecta. Línea:",
        p.lineno(len(p)-1)
    )
    exit(1)

# --------------------- LLAMADA A FUNCIONES ----------------------- #

def p_llamada_funciones(p):
    '''llamada_funciones : llamada_funcion llamada_funciones
                        | lambda'''

def p_llamada_funcion(p):
    '''llamada_funcion : ID PAREN_IZQ ll_params PAREN_DER PYC'''
    
    if p[1] not in memory['funciones']:
        print("Error: funcion", p[1], "no definida. Línea:", p.lineno(1))
        exit(1)
    
    if len(memory['funciones'][p[1]]) != len(p[3]):
        print("Error: cantidad de parámetros incorrecta. Línea:", p.lineno(1))
        exit(1)
    

def p_ll_params(p):
    '''ll_params : ll_param
                | ll_param COMA ll_params
                | lambda'''
    p[0] = []
    for i in range(1, len(p)):
        if p[i] != ",":
            p[0] += p[i]

def p_ll_param(p):
    '''ll_param : dato'''
    p[0] = [p[1][0]]

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
    exit(1)

def p_ll_params_error(p):
    '''ll_params : ll_param error'''
    print("La declaración de los parámetros de la función es incorrecta. Línea:",
        p.lineno(len(p)-1)
    )
    exit(1)

# --------------------- Dato ----------------------- #

def p_dato(p):
    '''dato : num
            | CARACTER
            | BOOL'''
    temp = ''
    if str(type(p[1])) == "<class 'int'>" or str(type(p[1])) == "<class 'float'>":
      temp = "num"
    elif str(type(p[1])) == "<class 'str'>":
      if p[1] == "simio" or p[1] == "nel":
        temp = "BOOL"
      else:
        temp = "CARACTER"
    else:
      temp = "None"
    p[0] = (p[1], temp)

def p_dato_2(p):
    '''dato : ID'''
    p[0] = (p[1], "ID")

def p_dato_3(p):
    '''dato : operacion_aritmetica'''
    p[0] = ("opar", None)

# --------------------- Num ----------------------- #

def p_num(p):
    '''num : ENTERO
           | REAL'''
    p[0] = p[1]

# --------------------- Operación Aritmética ----------------------- #

def p_operacion_aritmetica(p):
    '''operacion_aritmetica : dato OPAR dato
                            | dato OPAR PAREN_IZQ operacion_aritmetica PAREN_DER'''

# --------------------- Lambda ----------------------- #

def p_lambda(p):
    '''lambda : '''

# --------------------- Error de Sintáxis ----------------------- #

def p_error(p):
  try:
    print("¡Error de sintáxis! Línea:", p.lineno)
  except:
    print("EOF sin encontrar símbolo válido. Ya valio jóven")

# Build the parser
parser = yacc.yacc()

