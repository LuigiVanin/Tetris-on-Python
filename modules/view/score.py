import csv
from numpy import ndarray

class score():
    def __init__(self):
        pass

def printBoard(table: ndarray):
        print('\n' * 20)
        for i in table:
            for item in i:
                if item == 0:
                    print('\x1b[%sm %s \x1b[0m' % ("0;37;47" ,"" ), end="")
                elif item == 1:
                    print('\x1b[%sm %s \x1b[0m' % ("0;37;45" ,"" ), end="")
                elif item == 2:
                    print('\x1b[%sm %s \x1b[0m' % ("0;37;44" ,"" ), end="")
                elif item == 3:
                    print('\x1b[%sm %s \x1b[0m' % ("0;37;42" ,"" ), end="")
                elif item == 4:
                    print('\x1b[%sm %s \x1b[0m' % ("0;37;43" ,"" ), end="")
                else:
                    print('\x1b[%sm %s \x1b[0m' % ("0;37;41" ,"" ), end="")
            print()
            
            
