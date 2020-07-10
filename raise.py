#! python3

import traceback

def boxPrint(symbol, width, height):

    if(len(symbol) != 1):
        raise Exception('Symbol needs to be length of 1')

    print(symbol*width)

    for x in range(0, height - 2):
        print(symbol + ' ' * (width - 2) + symbol)

    print(symbol*width)

boxPrint('*', 5, 5)
boxPrint('t', 15, 5)
#boxPrint('tt', 15, 5) # Traceback (most recent call last):
                      # File ".\raise.py", line 17, in <module>
                      # boxPrint('tt', 15, 5)
                      # File ".\raise.py", line 6, in boxPrint
                      # raise Exception('Symbol needs to be length of 1')
                      # Exception: Symbol needs to be length of 1

# Fancy error handling
try:
    boxPrint('tt', 15, 5)
except:
    errorFile = open('.\\error_log.txt', 'a')
    errorFile.write(traceback.format_exc())
    errorFile.write('\n\n')
    errorFile.close()
    print('Exception handled and written to error_log.txt')