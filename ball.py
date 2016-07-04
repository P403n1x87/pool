from visual import *
from physics import *
import Image

#r = 5.71 / 2
r = 7.5 # Ball radius
R = - r * j

class Ball(sphere):
    def __init__(self, name, texture, pos=(0, r, 0), v = zero, w = zero):
        # Ball's name
        self.name = name
        
        # Ball's texture
        tex = Image.open("img/" + texture + ".jpg")
        tex = tex.resize((256,512), Image.ANTIALIAS)

        # Kinematic variables
        self.v = v
        self.w = w
        self.a = self.alpha = zero
        
        # Boolean status vars
        self.isStopping = False
        self.isRolling = False
        self.isMoving = True
        
        # Tracing aids
        self.spin = arrow()
        self.arr_alpha = arrow()
        self.arr_alpha.color = color.red
        self.arr_a = arrow()
        self.arr_a.color = color.green
        self.arr_v = arrow()
        self.arr_v.color = color.blue

        self.trail = curve(color=color.white)

        super(sphere, self).__init__(material = materials.texture(data=tex, mapping="spherical", interpolate = False),
                                     pos = pos,
                                     radius = r)

    def step(self):
        '''Integrates the equation of motion. For the details of the
           currently implemented physics have a look at the
           documentation provided with the source code'''

        # If the ball is not moving then do nothing
        if self.v == zero and self.w == zero:
            self.isMoving = False
            return
        else:
            self.isMoving = True
        
        # [Kinematics] Integrate velocities
        self.pos = self.pos + self.v * dt
        self.rotate(angle = mag(self.w) * dt, axis = self.w)

        # [Dynamics] Friction around the vertical axis
        self.w[1] = self.w[1] - fs * g * dt * self.w[1]


        # Determine if the ball is rolling or slipping
        wperp = vector(self.w)
        wperp[1] = 0
        
        # This is the actual condition for rolling within the given
        # threshold
        if mag( wperp * r - cross(j, self.v) ) <  th * ( mag( wperp ) * r + mag(self.v) ) and not self.isRolling:
            self.isRolling = True
            print self.name, "rolling"

        if not self.isRolling:
            # The ball is slipping
            v = vector(self.v)
            w = vector(self.w)
            
            # Velocity of the contact point
            vc = v + cross(self.w, R)
            
            # Friction force opposes the motion of the contact point
            self.a = - g * fd * norm (vc)
            
            # If the magnitude of acceleration is below threshold then
            # kill it
            if mag(self.a) < th: self.a = zero
            
            # Angular acceleration
            self.alpha = - ( 5 / (2 * r) ) * cross(j, self.a)
            
            # If below threshold, kill it
            if mag(self.alpha) < th: self.alpha = zero

            # [Kinematics] Integrate the angular acceleration
            self.w = w + self.alpha * dt

        else:
            # The ball is rolling
            self.a = - g * fr * norm(self.v)
            
            # Angular velocity is now a function of the velocity of the
            # centre of mass
            self.w = cross(j, self.v / r) + dot(self.w,j) * j
        
        # [Kinematics] Integrate the acceleration
        self.v = self.v + self.a * dt

        # Trace trajectory and kinematical variables directions. Used
        # for debugging purposes
        # self.trace()
        
        # If the vertical component of the angular velocity is below
        # threshold then kill it 
        if -Th < self.w[1] < Th: self.w[1] = 0
        
        # This is modelling a ball that rock a bit when is coming to a
        # halt
        # if mag(self.v) < Th and mag(cross(self.w, j)) < Th:
        #    # Ball is coming to rest. Harmonic potential
        #    if not self.isStopping:
        #        print self.name, "stopping"
        #        self.isStopping = True
        #        self.ref = vector(self.pos)
        #
        #    self.a = (k * (self.ref - self.pos) - fg * self.v)
        #    self.v = self.v + dt * self.a
        
        if mag(self.v) < th: self.v = zero
        if mag(self.w) < th: self.w = zero

    def reset(self):
        '''Reset the ball's status'''
        self.isStopping = self.isRolling = False
        print self.name, "resetting"
        
    def trace(self):
        '''Traces ball's trajectory and depicts the direction of the
           kinematical variables'''
           
        self.arr_alpha.pos = self.pos
        self.arr_alpha.axis = norm(self.alpha) * 2 * r
        self.arr_a.pos = self.pos
        self.arr_a.axis = norm(self.a) * 2 * r
        
        self.arr_v.pos = self.pos
        self.arr_v.axis = norm(self.v) * 2 * r
        self.trail.append(pos=self.pos)
        self.spin.pos = self.pos
        self.spin.axis = norm(self.w) * 2 * r
