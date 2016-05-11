# -*- coding: utf-8 -*-
from yacc import yacc
import cmd
import Evaluator

class Print(cmd.Cmd):     # See https://docs.python.org/2/library/cmd.html

    def __init__(self):
        cmd.Cmd.__init__(self)
        self.prompt = "fp> "
        self.intro  = "Welcome to the Final Project. Input Swift print() statements."

    def do_exit(self, args):
        """Exits from the console"""
        return -1

    def do_EOF(self, args):
        """Exit on system end of file character"""
        print "Exiting final project."
        return self.do_exit(args)

    def emptyline(self):    
        """Do nothing on empty input line"""
        pass

    def default(self, line):       
        """Called on an input line when the command prefix is not recognized.
           In that case we execute the line as Python code.
        """
        result = yacc.parse(line)
        print "mini-lisp.py: AST is: ", result

        dirtyToken = Evaluator.tokenCleaner(result)
        f = lambda x, y, z : x[z][z:-z]
        cleanedToken = f(result, Evaluator.tokenCleaner(), 1)
        output = Evaluator.evaluate(cleanedToken)

        if output is not None:
           print output


if __name__ == '__main__':
        ml = Print()
        ml.cmdloop()     # See https://docs.python.org/2/library/cmd.html
