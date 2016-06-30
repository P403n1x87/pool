from visual import *
from physics import *
import Image

#r = 5.71 / 2
r = 7.5

class Ball(sphere):
	def __init__(self, name, texture, pos=(0, r, 0), v = zero, w = zero):
		self.name = name
		tex = Image.open(texture+".jpg")
		tex = tex.resize((256,512), Image.ANTIALIAS)

		self.v = v
		self.w = w
		self.a = zero
		
		self.isStopping = False
		self.isRolling = False

		super(sphere, self).__init__(material=materials.texture(data=tex, mapping="spherical", interpolate = False), pos=pos, radius=r)

	def step(self):
		if self.v == zero and self.w == zero: return
		
		self.pos = self.pos + self.v * dt
		self.rotate(angle = mag(self.w) * dt, axis = self.w)
		#trail.append(pos=self.pos)
		#spin.pos = self.pos
		#spin.axis = norm(self.w) * 2 * r

		self.w[1] = self.w[1] - fs * g * dt * self.w[1]

		wperp = vector(self.w)
		wperp[1] = 0
		if mag(wperp - cross(j, self.v) / r) < th and not self.isRolling:
			self.isRolling = True
			print self.name, "rolling"

		if not self.isRolling:
			print self.name, mag(self.v), mag(self.w)
			# The ball is slipping
			v = vector(self.v)
			w = vector(self.w)
			self.a = - g * (fd * norm(proj(v, norm(cross(w, j))) - r * cross(w,j)) + ff * norm(v))
			self.v = v + self.a * dt
			
			self.w = w + g / (2./5*r) * dt * (fd * norm(cross(j, v - r * cross(w, j))) - ff * norm(wperp))

		else:
			# The ball is rolling
			#self.rotate(angle = mag(self.v * dt) / r, axis = cross(j, self.v))
			
			self.a = - g * fr * norm(self.v)
			self.v = self.v + self.a * dt
			self.w = cross(j, self.v / r) + dot(self.w,j) * j
			
		if -th < self.w[1] < th: self.w[1] = 0
		
		if mag(self.v) < Th and mag(cross(self.w, j)) < th:
			# Ball is coming to rest. Harmonic potential
			if not self.isStopping:
				print self.name, "stopping"
				self.isStopping = True
				self.ref = vector(self.pos)
			
			self.a = (k * (self.ref - self.pos) - fg * self.v)
			self.v = self.v + dt * self.a
			
		if mag(self.v) < th and mag(self.a) < th and mag(self.w) < th:
			self.v = self.w = zero
			print self.name, "halt"

	def reset(self):
		self.isStopping = False
		self.isRolling = False
		print self.name, "resetting"
		
