from visual import vector, mag, dot, norm

zero = vector(0,0,0)
j = vector(0,1,0)

dt = 0.001

g = 1                  # Gravity

ff = 100
fr = 100
fd = 5000                # Dynamic friction coefficient
fs = 2                 # Static friction coefficient
fg = 0.1

th = 0.5              # Zero threshold
Th = .5

k = 1

cc = 0.95

def proj(a,b):
    '''Projects the vector a along the direction of b.'''
       
    return vector(dot(a, norm(b)) * norm(b))

def dist(a,b):
    '''Returns the linear distance between a and b, i.e. the magnitude
       of the vector a - b.'''
       
    return( mag(a.pos - b.pos) )
