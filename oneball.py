#!/usr/bin/env python

from visual import *
from ball import Ball
from physics import *
import Image

scene.width=800
scene.height=600
scene.forward=(0,-1,0)

table_length = 365.8
table_width = 182.9

baize = Image.open("img/tabletop.png")
#baize = baize.resize((183,366), Image.ANTIALIAS)
table = box(pos=(0,-1,0), axis=(0,1,0), width=table_width, height = table_length, length = 2, material = materials.texture(data=baize, mapping="sign"), color=color.green)

from ball import r

balls = [
	Ball("10", "10small", pos = (table_length * .25, r, 0),
                          v = vector(80,0,80),
                          w = vector(0,0,100))
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

	# Ball-cushions collisions
	for ball in balls:
		if (ball.pos[0] + r > table_length / 2 and ball.v[0] > 0) or (ball.pos[0] - r < -table_length / 2 and ball.v[0] < 0):
			ball.v[0] = -cc * ball.v[0]
			ball.reset()
			
		if (ball.pos[2] + r > table_width / 2 and ball.v[2] > 0) or (ball.pos[2] - r < -table_width / 2 and ball.v[2] < 0):
			ball.v[2] = -cc * ball.v[2]
			ball.reset()


scene.kb.getkey()
while running:
	rate(240)
	
	check_collisions()
	
	for ball in balls: ball.step()
	
