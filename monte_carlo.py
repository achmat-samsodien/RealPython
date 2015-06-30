from __future__ import division
from random import randint



for trial in range(0, 1000):
    while randint(0,1) == 0:
        tails = tails + 1
    heads = heads + 1

print "heads / tails = ", heads/tails