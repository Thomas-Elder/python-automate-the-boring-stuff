#! python3

import logging
logging.basicConfig(filename='factorial_log.txt', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# There are different logging levels, debug, info, warning, error and critical (from least important to most)
# We can disable logging at different levels, by calling disable, and passing it the desired level. 
# This will disable messages at that level or lower. 
# So this line disables **all** logging messages, so we can just comment this out if we want them back.
#logging.disable(logging.CRITICAL)

# Or we could just disable DEBUG messages
#logging.disable(logging.DEBUG)

logging.info('Start of program')

# buggy factorial function to fix...
def factorial(n):
    logging.info('Start of factorial %s' % (n))
    if n <= 0: 
        logging.error('Function doesn\'t handle %s as a parameter' % (n))
        return 0 

    total = 1 

    for i in range(1, n + 1):
        total *= i
        logging.debug('i is %s and total is %s' % (i, total))
    
    logging.debug('Return value is %s' % (total))
    return total

assert factorial(0) == 0
assert factorial(4) == 24
assert factorial(5) == 120

logging.info('End of program')