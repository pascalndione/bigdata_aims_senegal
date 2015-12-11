#------ file pascalndione.py -------
#  code starts below this
#-------------------------------------------
import numpy as np
import os
import sys


functions=['my_guess_constant','my_guess_random']

def my_guess_constant(History=None):
    return 50

def my_guess_random(History=None):
    return np.random.randint(1,100)

for i in range (100):
	c1 = my_guess_constant()
	c2 = my_guess_random()
	cw = [c1, c2]

print c1, c2, np.mean(cw)

c = np.min(np.abs(cw-np.mean(cw)))

print 'winner c '

#------ code ends here -----
