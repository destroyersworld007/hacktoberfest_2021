# python 2 implementation of bellman ford algorithm


from array import *

MAX = 999

adjacencyArray = [

    [ 0, 6, MAX, 4, MAX ],
    [ MAX, MAX, 3, 2, MAX ],
    [ MAX, MAX, MAX, MAX, 4 ],
    [ MAX, 1, 9, MAX, 3 ],
    [ 7, MAX, 5, MAX, MAX ]

]

shortest = [0, MAX, MAX, MAX, MAX, MAX]
pred = [None, None, None, None, None]

# Relax Functions
for u in range(0, 5):
    for v in range(0, 5):

        if shortest[u] + adjacencyArray[u][v] < shortest[v]:
            shortest[v] = shortest[u] + adjacencyArray[u][v]
            pred[v] = u

for x in range(0, 5):

    v = x

    print 'Path for vertex ' + str(v)

    path = ''

    while pred[v] != None:
        v = pred[v]
        path += ' >- ' + str(v)
        
    print path[::-1] + '' + str(x)
