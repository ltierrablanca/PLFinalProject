#------------------------------------------------------------
# lex.py
#
# tokenizer
# ------------------------------------------------------------

import ply.lex as lex

# List of token names.   
tokens = [
    'NIL',
    'PRINT',
    'CONTENTS',
    'TRUE',
    'FALSE',
]

# Reserved words
reserved = {
    'nil' : 'NIL',
}


# # Regular expression rules for simple tokens

t_TRUE = r'\#t'
t_FALSE = r'\#f'


def t_PRINT(t):
    r'print'
    t.type = reserved.get(t.value, 'PRINT')
    print ("Lex.py: PRINT token found.")
    return t

def t_CONTENTS(t):
    r'\(.*\)'
    t.type = reserved.get(t.value, 'CONTENTS')
    print ("Lex.py: CONTENTS token found.")
    return t



# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

# Error handling rule
def t_error(t):
    print "Illegal character '%s'" % t.value[0]
    t.lexer.skip(1)

# Build the lexer
lex.lex()

if __name__ == '__main__':
    lex.runmain()
