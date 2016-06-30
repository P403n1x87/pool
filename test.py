#!/usr/bin/env python

from visual import *
from ball import Ball
from physics import *
import Image

scene.width=800
scene.height=600

table_length = 365.8
table_width = 182.9

baize = Image.open("tabletop.jpg.png")
#baize = baize.resize((183,366), Image.ANTIALIAS)
table = box(pos=(0,-1,0), axis=(0,1,0), width=table_width, height = table_length, length = 2, material = materials.texture(data=baize, mapping="sign"), color=color.green)

from ball import r

balls = [
	Ball("cueball", "cueball", pos=(-table_length * .35,r,0), v=vector(500,0,10), w=vector(0,0,-20)),
	Ball("10", "10small", pos=(table_length * .25, r, 0)),
	Ball("8", "8small", pos=(table_length * .25 + 1.72 * r, r, r)),
	Ball("1", "1small", pos=(table_length * .25 + 1.73 * r, r, -r)),
	Ball("3", "3small", pos=(table_length * .25 + 2 * 1.73 * r, r, 0))
]


running = True

def check_collisions():
	
	# Ball-ball collisions
	N = len(balls)
	for i in range(N):
		for j in range(i,N):
			if dist(balls[i], balls[j]) < 2 * r and dot(balls[i].v-balls[j].v, balls[j].pos - balls[i].pos) > 0:
				v = dot((balls[i].v - balls[j].v), norm(balls[j].pos - balls[i].pos)) * norm(norm(balls[j].pos - balls[i].pos))
				balls[j].v = balls[j].v + v
				balls[i].v = balls[i].v - v
				balls[j].reset()
				balls[i].reset()

			
#	if dist(cueball, objball) < 2 * r and dot(cueball.v-objball.v, objball.pos - cueball.pos) > 0:
#		v = dot((cueball.v - objball.v), norm(objball.pos - cueball.pos)) * norm(norm(objball.pos - cueball.pos))
#		objball.v = objball.v + v
#		cueball.v = cueball.v - v
#		objball.reset()
#		cueball.reset()

	# Ball-cushions collisions
	for ball in balls:
		if (ball.pos[0] + r > table_length / 2 and ball.v[0] > 0) or (ball.pos[0] - r < -table_length / 2 and ball.v[0] < 0):
			ball.v[0] = -cc*ball.v[0]
			ball.reset()
			
		if (ball.pos[2] + r > table_width / 2 and ball.v[2] > 0) or (ball.pos[2] - r < -table_width / 2 and ball.v[2] < 0):
			ball.v[2] = -cc*ball.v[2]
			ball.reset()

while running:
	rate(120)
	
	check_collisions()
	
	for ball in balls: ball.step()
	
	#print mag(cueball.v + objball.v), "\r",
	
