from visual import vector, mag, dot

zero = vector(0,0,0)
j = vector(0,1,0)

dt = 0.01
g = 1

ff = 1
fr = 5
fd = 50
fs = 2
fg = 0.1

th = 0.01
Th = .5

k = 1

cc = 0.8

def proj(a,b):
	return dot(a,b)*b

def dist(a,b):
	return( mag(a.pos - b.pos) )
