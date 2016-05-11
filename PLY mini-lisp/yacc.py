import ply.yacc as yacc

# Get the token map from the lexer.  This is required.

from lex import tokens

DEBUG = False

# Namespace & built-in functions

name = {}

global ast
ast = []


# BNF


def p_exp_atom(p):
   'exp : atom'
   p[0] = p[1]

# def p_exp_qlist(p):
#    'exp : quoted_list'
#    p[0] = p[1]
#
def p_exp_call(p):
   'exp : call'
   p[0] = p[1]


def p_items(p):
   'items : item items'
   p[0] = [p[1]] + p[2]

def p_items_empty(p):
   'items : empty'
   p[0] = []

def p_empty(p):
   'empty :'
   pass

def p_item_atom(p):
   'item : atom'
   p[0] = p[1]


def p_call(p):
   'call : PRINT CONTENTS'
   tree = []
   tree.append(p[1])
   tree.append(p[2])
   p[0] = tree


def p_true(p):
   'bool : TRUE'
   p[0] = True

def p_false(p):
   'bool : FALSE'
   p[0] = False

def p_nil(p):
    'atom : NIL'
    p[0] = None

# Error rule for syntax errors
def p_error(p):
    print "yacc.py: Syntax error: ", p

# Build the parser
# Use this if you want to build the parser using SLR instead of LALR
# yacc.yacc(method="SLR")
yacc.yacc()


