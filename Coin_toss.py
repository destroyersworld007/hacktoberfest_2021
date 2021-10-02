import random

samples = [ random.randint(1, 2) for i in range(100) ]
heads = samples.count(1)
tails = samples.count(2)

for s in samples:
    msg = 'Heads' if s==1 else 'Tails'
    print msg

print "Heads count=%d, Tails count=%d" % (heads, tails)