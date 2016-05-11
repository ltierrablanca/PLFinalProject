import Eval
global token

def tokenCleaner(input = None):
    global token
    token = input
    def cleanToken(dirtyToken):
        if dirtyToken is None:
            return
        else:
            f = lambda x,y,z : x[y][z:-z]
            s = f(dirtyToken, 1, 1)
            return s
    return cleanToken

def evaluate(input):
    expr = input
    print ("Expression to be evaluated: ", expr)
    if '"' in expr:
        expr = expr[1:-1]
        return expr
    else:
        expr = Eval.evaluate(expr)
        return expr