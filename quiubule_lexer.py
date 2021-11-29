# --------------------------------------- #
# Para utilizar el lexer desde el parser:
# from quiubule_lexer import lexer
# lexer.input(data)
# lexer.token()
# --------------------------------------- #

#https://www.dabeaz.com/ply/ply.html
from utils import lex

tokens = [
    'ID',
    'PYC',
    'CORCHETE_IZQ',
    'CORCHETE_DER',
    'BRACKET_IZQ',
    'BRACKET_DER',
    'PAREN_IZQ',
    'PAREN_DER',
    'COMA',
    'PUNTO',
    'IGUAL',
    'OPAR',
    'OPREL',
    'OPLOG',
    'OPNOT',
    'CARACTER',
    'ENTERO',
    'REAL',
    'BOOL',
    #'ERR',
]

reserved = {
    'juntitos' : 'JUNTITOS',
    'chafirete' : 'CHAFIRETE',
    'coso' : 'COSO',
    'rifate' : 'RIFATE',
    'chance' : 'CHANCE',
    'hijole' : 'HIJOLE',
    'chambea' : 'CHAMBEA',
    'leete' : 'LEETE',
    'escribete': 'ESCRIBETE',
    'escribetel': 'ESCRIBETEL',
    'ahiteva': 'AHITEVA',
 }

tokens = tokens + list(reserved.values())

# Expresiones regulares para tokens simples
t_PYC    = r'\;'
t_CORCHETE_IZQ  = r'\['
t_CORCHETE_DER  = r'\]'
t_BRACKET_IZQ  = r'\{'
t_BRACKET_DER  = r'\}'
t_PAREN_IZQ  = r'\('
t_PAREN_DER  = r'\)'
t_COMA  = r'\,'
t_PUNTO = r'[.]'
t_IGUAL = r'\='
t_OPAR = r'\+|-|[*]|/%?'
t_OPREL = r'\<=?|>=?|==|!='
t_OPLOG = r'\&&|\|\|'
t_OPNOT = r'\!'
t_CARACTER = r'"\s*((?:\w(?!\s+")+|\s(?!\s*"))+\w)\s*"'

def t_BOOL(t):
    r'(simio) | (nel)'
    t.type = 'BOOL'
    return t

# Revisar si es palabra reservada o caracter
def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    if t.value in reserved:
        t.type = reserved.get(t.value,'IDENTIFIER')
    else:
        t.type = 'ID'
    return t

def t_REAL(t):
    r'\b(([1-9][0-9]*)?[0-9]\.[0-9]+)\b'
    t.value = float(t.value)
    return t

def t_ENTERO(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Nueva linea
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_COMMENT(t):
     r'\#.*'
     pass
     # No return value. Token discarded

# Ignorar espacios y tabs
t_ignore  = ' \t'

def t_error(t):
 print("Token Invalido '%s'" % t.value[0])
 t.lexer.skip(1)

# Constuir lexer
lexer = lex.lex()
