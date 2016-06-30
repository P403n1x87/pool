from visual import *
scene = display ( range = 65 )
#scene.fullscreen = true
scene.forward = vector(0, -1, 0)
#scene.userspin = false
#scene.userzoom = false

import sys
print sys.path

#texture info
import Image
width=128
height=128

fileName = "1small"
ball1 = Image.open(fileName+".jpg")
ball1 = ball1.resize((width,height), Image.ANTIALIAS)
ballTex1 = materials.texture(data=ball1, mapping="spherical", interpolate = False)

fileName = "2small"
ball1 = Image.open(fileName+".jpg")
ball1 = ball1.resize((width,height), Image.ANTIALIAS)
ballTex2 = materials.texture(data=ball1, mapping="spherical", interpolate = False)

fileName = "3small"
ball1 = Image.open(fileName+".jpg")
ball1 = ball1.resize((width,height), Image.ANTIALIAS)
ballTex3 = materials.texture(data=ball1, mapping="spherical", interpolate = False)

fileName = "4small"
ball1 = Image.open(fileName+".jpg")
ball1 = ball1.resize((width,height), Image.ANTIALIAS)
ballTex4 = materials.texture(data=ball1, mapping="spherical", interpolate = False)

fileName = "5small"
ball1 = Image.open(fileName+".jpg")
ball1 = ball1.resize((width,height), Image.ANTIALIAS)
ballTex5 = materials.texture(data=ball1, mapping="spherical", interpolate = False)

fileName = "6small"
ball1 = Image.open(fileName+".jpg")
ball1 = ball1.resize((width,height), Image.ANTIALIAS)
ballTex6 = materials.texture(data=ball1, mapping="spherical", interpolate = False)

fileName = "7small"
ball1 = Image.open(fileName+".jpg")
ball1 = ball1.resize((width,height), Image.ANTIALIAS)
ballTex7 = materials.texture(data=ball1, mapping="spherical", interpolate = False)

fileName = "8small"
ball1 = Image.open(fileName+".jpg")
ball1 = ball1.resize((width,height), Image.ANTIALIAS)
ballTex8 = materials.texture(data=ball1, mapping="spherical", interpolate = False)

fileName = "9small"
ball1 = Image.open(fileName+".jpg")
ball1 = ball1.resize((width,height), Image.ANTIALIAS)
ballTex9 = materials.texture(data=ball1, mapping="spherical", interpolate = False)

fileName = "10small"
ball1 = Image.open(fileName+".jpg")
ball1 = ball1.resize((width,height), Image.ANTIALIAS)
ballTex10 = materials.texture(data=ball1, mapping="spherical", interpolate = False)

fileName = "11small"
ball1 = Image.open(fileName+".jpg")
ball1 = ball1.resize((width,height), Image.ANTIALIAS)
ballTex11 = materials.texture(data=ball1, mapping="spherical", interpolate = False)

fileName = "12small"
ball1 = Image.open(fileName+".jpg")
ball1 = ball1.resize((width,height), Image.ANTIALIAS)
ballTex12 = materials.texture(data=ball1, mapping="spherical", interpolate = False)

fileName = "13small"
ball1 = Image.open(fileName+".jpg")
ball1 = ball1.resize((width,height), Image.ANTIALIAS)
ballTex13 = materials.texture(data=ball1, mapping="spherical", interpolate = False)

fileName = "14small"
ball1 = Image.open(fileName+".jpg")
ball1 = ball1.resize((width,height), Image.ANTIALIAS)
ballTex14 = materials.texture(data=ball1, mapping="spherical", interpolate = False)

fileName = "15small"
ball1 = Image.open(fileName+".jpg")
ball1 = ball1.resize((width,height), Image.ANTIALIAS)
ballTex15 = materials.texture(data=ball1, mapping="spherical", interpolate = False)

# VARIABLE LIST
#Colors and Materials
marble = materials.marble
rough = materials.rough
wood = materials.wood
emissive = materials.emissive
plastic = materials.plastic
white = color.white
black = color.black
bumper = vector(.5, .75, .25)
trimColor = vector(.55, .27, .07)
#Dimensions and Directions
tableLength = 96
tableWidth = 48
up = (0, 1, 0)
dimTile = 10
ballRadius = 1.125
pocketHeight = .01#2.1
#Location
posY = -30
labelPlayer1 = (-48, 25, -24)
labelPlayer2 = (48, 25, 24)
ballLine1 = vector(-48, 22, -24)
ballLine2 = vector(48, 22, 24)
#Misc
centerDisplay = vector(0, 10, 0)
sideDisplay = vector(0, 10, -30)
numBalls = 16
massBalls = 1
epsilon = .9
dt = .05
gravity = 5
friction = .1
fricForce = friction * massBalls * gravity
playerTurn = 1
flashTime = 20
bFriction = 0.8
pocketRadius = 1.75
inPockets = []
player1Off = 0
player2Off = 0
ballsMoving = false
numIn = 0
cueHit = false
isNotOver = true
power = 0

#Scoreboards and other labels
label ( pos = labelPlayer1, text = 'Player 1')
label ( pos = labelPlayer2, text = 'Player 2')
turnDisplay1 = label ( pos = sideDisplay, text = 'Player 1 Turn')
turnDisplay2 = label ( pos = sideDisplay, text = 'Player 2 Turn')
turnDisplay1.visible = false
turnDisplay2.visible = false

player1win = label (pos = centerDisplay, text = 'Player 1 Wins!!!')
player2win = label (pos = centerDisplay, text = 'Player 2 Wins!!!')
player1win.visible = false
player2win.visible = false


table = frame ()
#Felt
box ( frame = table, color = color.green, length = tableLength, width = tableWidth )
#Underbox
box ( frame = table, color = trimColor, material = wood, length = 104, width = 56, pos = vector(0, -.5, 0) )
curve( frame = table, pos=[(-52, -.5, -28), (52, -.5, -28), (52, -.5, 28), (-52, -.5, 28), (-52, -.5, -28)], radius = 0.5, color = trimColor, material = wood)
# Old Bumpers
#box ( frame = table, color=vector(.5, .75, .25), length = 96, width = 2, height = 2, pos = vector(0, 1, 25) )
#box ( frame = table, color=vector(.5, .75, .25), length = 96, width = 2, height = 2, pos = vector(0, 1, -25) )
#box ( frame = table, color=vector(.5, .75, .25), length = 2, width = 52, height = 2, pos = vector(49, 1, 0) )
#box ( frame = table, color=vector(.5, .75, .25), length = 2, width = 52, height = 2, pos = vector(-49, 1, 0) )
#New Bumpers
#Long Bottom
cylinder ( frame = table, color = bumper, length = 2, axis = up, radius = 1, pos = vector(-46.25, 0, 25) )
box ( frame = table, color = bumper, length = 44.5, width = 2, height = 2, pos = vector(-24, 1, 25) )
cylinder ( frame = table, color = bumper, length = 2, axis = up, radius = 1, pos = vector(-1.75, 0, 25) )
cylinder ( frame = table, color = bumper, length = 2, axis = up, radius = 1, pos = vector(46.25, 0, 25) )
box ( frame = table, color = bumper, length = 44.5, width = 2, height = 2, pos = vector(24, 1, 25) )
cylinder ( frame = table, color = bumper, length = 2, axis = up, radius = 1, pos = vector(1.75, 0, 25) )
#Long Top
cylinder ( frame = table, color = bumper, length = 2, axis = up, radius = 1, pos = vector(-46.25, 0, -25) )
box ( frame = table, color = bumper, length = 44.5, width = 2, height = 2, pos = vector(-24, 1, -25) )
cylinder ( frame = table, color = bumper, length = 2, axis = up, radius = 1, pos = vector(-1.75, 0, -25) )
cylinder ( frame = table, color = bumper, length = 2, axis = up, radius = 1, pos = vector(46.25, 0, -25) )
box ( frame = table, color = bumper, length = 44.5, width = 2, height = 2, pos = vector(24, 1, -25) )
cylinder ( frame = table, color = bumper, length = 2, axis = up, radius = 1, pos = vector(1.75, 0, -25) )
#Short Left
cylinder ( frame = table, color = bumper, length = 2, axis = up, radius = 1, pos = vector(-49, 0, -22.25) )
box ( frame = table, color = bumper, length = 2, width = 44.5, height = 2, pos = vector(-49, 1, 0) )
cylinder ( frame = table, color = bumper, length = 2, axis = up, radius = 1, pos = vector(-49, 0, 22.25) )
#Short Right
cylinder ( frame = table, color = bumper, length = 2, axis = up, radius = 1, pos = vector(49, 0, -22.25) )
box ( frame = table, color = bumper, length = 2, width = 44.5, height = 2, pos = vector(49, 1, 0) )
cylinder ( frame = table, color = bumper, length = 2, axis = up, radius = 1, pos = vector(49, 0, 22.25) )
#Pockets
cylinder ( frame = table, color=black, radius = 1.75, length = pocketHeight, axis = up, pos = vector( 0, 0, 24) )
cylinder ( frame = table, color=black, radius = 1.75, length = pocketHeight, axis = up, pos = vector( 0, 0, -24) )
cylinder ( frame = table, color=black, radius = 1.75, length = pocketHeight, axis = up, pos = vector( 48, 0, -24) )
cylinder ( frame = table, color=black, radius = 1.75, length = pocketHeight, axis = up, pos = vector( -48, 0, -24) )
cylinder ( frame = table, color=black, radius = 1.75, length = pocketHeight, axis = up, pos = vector( 48, 0, 24) )
cylinder ( frame = table, color=black, radius = 1.75, length = pocketHeight, axis = up, pos = vector( -48, 0, 24) )
#Wood Trim
box ( frame = table, color = trimColor, material = wood, length = 100, width = 4, height = 2, pos = vector(0, 1, 28) )
box ( frame = table, color = trimColor, material = wood, length = 100, width = 4, height = 2, pos = vector(0, 1, -28) )
box ( frame = table, color = trimColor, material = wood, length = 4, width = 52, height = 2, pos = vector(52, 1, 0) )
box ( frame = table, color = trimColor, material = wood, length = 4, width = 52, height = 2, pos = vector(-52, 1, 0) )
cylinder ( frame = table, color = trimColor, material = wood, radius = 4, length = 1.99, axis = up, pos = vector(50, 0, 26) )
cylinder ( frame = table, color = trimColor, material = wood, radius = 4, length = 1.99, axis = up, pos = vector(50, 0, -26) )
cylinder ( frame = table, color = trimColor, material = wood, radius = 4, length = 1.99, axis = up, pos = vector(-50, 0, 26) )
cylinder ( frame = table, color = trimColor, material = rough, radius = 4, length = 1.99, axis = up, pos = vector(-50, 0, -26) )
#Emitters
cylinder ( frame = table, color = color.gray(.6), material = plastic, radius = 3.5, length = .5, axis = up, pos = vector (-48, -1.25, -24) )
cylinder ( frame = table, color = color.gray(.9), material = rough, radius = 3.3, length = .01, axis = up, pos = vector (-48, -1.255, -24) )
cylinder ( frame = table, color = color.gray(.6), material = plastic, radius = 3.5, length = .5, axis = up, pos = vector (-48, -1.25, 24) )
cylinder ( frame = table, color = color.gray(.9), material = rough, radius = 3.3, length = .01, axis = up, pos = vector (-48, -1.255, 24) )
cylinder ( frame = table, color = color.gray(.6), material = plastic, radius = 3.5, length = .5, axis = up, pos = vector (48, -1.25, -24) )
cylinder ( frame = table, color = color.gray(.9), material = rough, radius = 3.3, length = .01, axis = up, pos = vector (48, -1.255, -24) )
cylinder ( frame = table, color = color.gray(.6), material = plastic, radius = 3.5, length = .5, axis = up, pos = vector (48, -1.25, 24) )
cylinder ( frame = table, color = color.gray(.9), material = rough, radius = 3.3, length = .01, axis = up, pos = vector (48, -1.255, 24) )
#Markers
ellipsoid( frame = table, color = white, material = plastic, pos=(-24, 2.01, 28), axis=(0, 0, 1), height = .01, width = .5)
ellipsoid( frame = table, color = white, material = plastic, pos=(-tableLength * .125, 2.01, 28), axis=(0, 0, 1), height = .01, width = .5)
ellipsoid( frame = table, color = white, material = plastic, pos=(-tableLength * .375, 2.01, 28), axis=(0, 0, 1), height = .01, width = .5)
ellipsoid( frame = table, color = white, material = plastic, pos=(-24, 2.01, -28), axis=(0, 0, 1), height = .01, width = .5)
ellipsoid( frame = table, color = white, material = plastic, pos=(-tableLength * .125, 2.01, -28), axis=(0, 0, 1), height = .01, width = .5)
ellipsoid( frame = table, color = white, material = plastic, pos=(-tableLength * .375, 2.01, -28), axis=(0, 0, 1), height = .01, width = .5)
ellipsoid( frame = table, color = white, material = plastic, pos=(24, 2.01, 28), axis=(0, 0, 1), height = .01, width = .5)
ellipsoid( frame = table, color = white, material = plastic, pos=(tableLength * .125, 2.01, 28), axis=(0, 0, 1), height = .01, width = .5)
ellipsoid( frame = table, color = white, material = plastic, pos=(tableLength * .375, 2.01, 28), axis=(0, 0, 1), height = .01, width = .5)
ellipsoid( frame = table, color = white, material = plastic, pos=(24, 2.01, -28), axis=(0, 0, 1), height = .01, width = .5)
ellipsoid( frame = table, color = white, material = plastic, pos=(tableLength * .125, 2.01, -28), axis=(0, 0, 1), height = .01, width = .5)
ellipsoid( frame = table, color = white, material = plastic, pos=(tableLength * .375, 2.01, -28), axis=(0, 0, 1), height = .01, width = .5)
ellipsoid( frame = table, color = white, material = plastic, pos=(52, 2.01, 0), axis=(1, 0, 0), height = .01, width = .5)
ellipsoid( frame = table, color = white, material = plastic, pos=(52, 2.01, tableWidth * .25), axis=(1, 0, 0), height = .01, width = .5)
ellipsoid( frame = table, color = white, material = plastic, pos=(52, 2.01, tableWidth * -.25), axis=(1, 0, 0), height = .01, width = .5)
ellipsoid( frame = table, color = white, material = plastic, pos=(-52, 2.01, 0), axis=(1, 0, 0), height = .01, width = .5)
ellipsoid( frame = table, color = white, material = plastic, pos=(-52, 2.01, tableWidth * .25), axis=(1, 0, 0), height = .01, width = .5)
ellipsoid( frame = table, color = white, material = plastic, pos=(-52, 2.01, tableWidth * -.25), axis=(1, 0, 0), height = .01, width = .5)

#Create pockets
pockets = [cylinder, cylinder, cylinder, cylinder, cylinder, cylinder]
for iPocket in range(6):
    pockets[iPocket] = cylinder(color = black, radius = pocketRadius, length = 2.1, axis = up)

pockets[0].pos = vector( 0, 0, 24)
pockets[1].pos = vector( 0, 0, -24)
pockets[2].pos = vector( 48, 0, -24)
pockets[3].pos = vector( -48, 0, -24)
pockets[4].pos = vector( 48, 0, 24)
pockets[5].pos = vector( -48, 0, 24)


#Stick
stick = frame () #axis = (-1, 1, 0)
cylinder ( frame = stick, material = wood, color=vector(.63, .32, .18), radius = .3, length = 58, axis = (-1, 0, 0), pos = vector(-28.0, 1.625, 0.0) )
cylinder ( frame = stick, color = white, radius = .3, axis = (-1, 0, 0), pos = vector(-27, 1.625, 0) )
cylinder ( frame = stick, color = color.blue, radius = .3, axis = (-1, 0, 0), pos = vector(-26.8, 1.625, 0), length = .2 )
#stick.axis = (-1, -1, 0)
stick.pos.y = 1

#Create Balls, even numbers are solids, odds stripes
balls =[sphere, sphere, sphere, sphere, sphere, sphere, sphere, sphere, sphere, sphere, sphere, sphere, sphere, sphere, sphere, sphere]
shadows = [cylinder, cylinder, cylinder, cylinder, cylinder, cylinder, cylinder, cylinder, cylinder, cylinder, cylinder, cylinder, cylinder, cylinder, cylinder, cylinder]
for iBall in range(numBalls):
    balls[iBall] = sphere(radius = ballRadius, velocity = vector(0,0,0), material = plastic, lifeSpan = flashTime, inPlay = 1, ballNum = iBall, axis = (0,1,0))
    balls[iBall].rotate ( angle= -(90*pi)/180, axis= ( -1, 0, 0 ))
    shadows[iBall] = cylinder(color = black, radius = ballRadius, pos = vector(0,0,0), length = .01, axis = up)



#ball[0] will be the cue ball
balls[0].pos = vector (-26, 1.625, 0)
balls[1].pos = vector ( 26, 1.625, 0)
balls[2].pos = vector ( 28.25, 1.625, 1.125 )
balls[3].pos = vector ( 28.25, 1.625, -1.125 )
balls[4].pos = vector ( 30.5, 1.625, 2.25 )
balls[5].pos = vector ( 30.5, 1.625, 0 )
balls[6].pos = vector ( 30.5, 1.625, -2.25 )
balls[7].pos = vector ( 32.75, 1.625, 1.125 )
balls[8].pos = vector ( 32.75, 1.625, -1.125 )
balls[9].pos = vector ( 32.75, 1.625, 3.375 )
balls[10].pos = vector ( 32.75, 1.625, -3.375 )
balls[11].pos = vector ( 35, 1.625, 0 )
balls[12].pos = vector ( 35, 1.625, 2.25 )
balls[13].pos = vector ( 35, 1.625, -2.25 )
balls[14].pos = vector ( 35, 1.625, 4.5 )
balls[15].pos = vector ( 35, 1.625, -4.5 )
#Colors
balls[0].color = white
##balls[1].color = vector ( .75, .75, .15 )
##balls[2].color = vector ( 0, 0, 1 )
##balls[3].color = vector ( 1, 0, 0 )
##balls[4].color = vector ( .75, .15, .75 )
##balls[5].color = vector ( .01, .01, .01 )#eight
##balls[6].color = vector ( .5, .75, .25 )
##balls[7].color = vector ( .25, .75, .5 )
##balls[8].color = vector ( .35, .75, .60 )
##balls[9].color = vector ( .75, .5, .25 )
##balls[10].color = vector ( .25, .5, .75 )
##balls[11].color = vector ( .5, .25, .75 )
##balls[12].color = vector ( .75, .5, .75 )
##balls[13].color = vector ( .5, .75, .75 )
##balls[14].color = vector ( .75, .75, .5 )
##balls[15].color = vector ( .5, .75, .15 )


balls[1].material = ballTex1
balls[2].material = ballTex2
balls[3].material = ballTex3
balls[4].material = ballTex4
balls[5].material = ballTex8#eight
balls[6].material = ballTex5
balls[7].material = ballTex6
balls[8].material = ballTex7
balls[9].material = ballTex9
balls[10].material = ballTex10
balls[11].material = ballTex11
balls[12].material = ballTex12
balls[13].material = ballTex13
balls[14].material = ballTex14
balls[15].material = ballTex15

#numRingsInStack = 4
numRings = 16#4 * numRingsInStack
#Create Rings
rings = [ring, ring, ring, ring, ring, ring, ring, ring, ring, ring, ring, ring, ring, ring, ring, ring]
for iRing in range(numRings):
    rings[iRing] = ring(axis = up, radius = 3, thickness = 0.35, color = vector(1, .65, 0), material = emissive, opacity = .4)
#    for iRing in range(numRings):
#        rings[iRing].pos = vector(ringPosX, (posY * .5 - 1.5)/ ( (numRingsInStack * iRing) % numRingsInStack), ringPosZ)

#(posY * .5 - 1.5)/ numRingsInStack

rings[0].pos = vector (-48, -3.75, -24)
rings[1].pos = vector (-48, -7.5, -24)
rings[2].pos = vector (-48, -11.25, -24)
rings[3].pos = vector (-48, -15, -24)
rings[4].pos = vector (48, -3.75, -24)
rings[5].pos = vector (48, -7.5, -24)
rings[6].pos = vector (48, -11.25, -24)
rings[7].pos = vector (48, -15, -24)
rings[8].pos = vector (-48, -3.75, 24)
rings[9].pos = vector (-48, -7.5, 24)
rings[10].pos = vector (-48, -11.25, 24)
rings[11].pos = vector (-48, -15, 24)
rings[12].pos = vector (48, -3.75, 24)
rings[13].pos = vector (48, -7.5, 24)
rings[14].pos = vector (48, -11.25, 24)
rings[15].pos = vector (48, -15, 24)

junk = 0
turnDisplay1.visible = true
stick.pos.x = balls[0].pos.z - 5
stick.pos.z = balls[0].pos.x - 5

for iBall in range(numBalls):
    thisBall = balls[iBall]
    shadows[iBall].pos = thisBall.pos - (0, ballRadius, .2)

while isNotOver:
    rate(100)

    if(ballsMoving == false and cueHit == false):
       #if (math.fabs(mag(balls[0].velocity)) > 1.0):
            #stick.visible = false
        stick.visible = true
        stick.axis = norm(balls[0].pos - scene.mouse.pos)
        stick.pos = balls[0].pos + (stick.axis * 1)
        
        if scene.kb.keys:
            s = scene.kb.getkey()
##            if (s == 'left'):
##                stick.rotate( angle= -(1*pi)/180, axis= ( 0, 1, 0 ), origin = balls[0].pos )
##            if (s == 'right'):
##                stick.rotate( angle= (1*pi)/180, axis= ( 0, 1, 0 ), origin = balls[0].pos )
##            if (s == 'up'):
##                stick.pos.x += balls[0].pos.z - 2
##                power -= 5
##            if (s == 'down'):
##                stick.pos.x += balls[0].pos.z + 2
##                power += 5
            if (s == 'w'):
                cueHit = true
                balls[0].velocity += norm(balls[0].pos - scene.mouse.pos) * 16.0
                balls[0].velocity.y = 0 
                #balls[0].velocity += norm(balls[0].pos - stick.pos) * power
                
    else:
        stick.visible = false
        
        
##        if scene.kb.keys:
##            s = scene.kb.getkey()
##
##            if (s == 'w'):
##                balls[0].velocity += norm(balls[0].pos - scene.mouse.pos) * 16.0
##                balls[0].velocity.y = 0 
        
        
        

    for iRing in range(numRings):
        rings[iRing].pos.y -= .1
        rings[iRing].radius *= .998
        rings[iRing].opacity *= .98
        if rings[iRing].pos.y < posY * .5 - 1.5:
            rings[iRing].pos.y = -1.5
            rings[iRing].radius = 3
            rings[iRing].opacity = .4

    #if (math.fabs(mag(balls[0].pos - scene.mouse.pos)) > 1.0):
        stick.axis = norm(balls[0].pos - scene.mouse.pos)
        stick.pos = balls[0].pos + (stick.axis * 1)

    #stick.axis.y = 0.1
    #stick.pos.y = 2.0

    #Check for collisions with other ball and pockets
    for iBall in range(numBalls - 1):
        thisBall = balls[iBall]

        #Ball vs Ball check
        for iBall2 in range(iBall + 1, numBalls):
            otherBall = balls[iBall2]
            n = otherBall.pos - thisBall.pos

            if ( mag(n) < (ballRadius + ballRadius) ):
                nhat = norm (n)
                v1n = dot ( thisBall.velocity, nhat )
                v2n = dot ( otherBall.velocity, nhat )
                if v2n - v1n > 0:
                    junk += 1
                else:
                    vcm = (massBalls * thisBall.velocity) + (massBalls * otherBall.velocity )
                    vcm = vcm / (massBalls * 2 )
                    # translate v1 and v2 to cm frame
                    v1cm_pre = thisBall.velocity - vcm
                    v2cm_pre = otherBall.velocity - vcm
                    # in CM, balls just bounce backwards with eps* incoming
                    v1cm_post = nhat * -mag(v1cm_pre) * epsilon
                    v2cm_post = nhat * mag(v2cm_pre) * epsilon
                    # now go back to lab frame
                    thisBall.velocity = v1cm_post + vcm
                    otherBall.velocity = v2cm_post + vcm

        #check for collisions with pockets
        for iPocket in range(6):
            thisPocket = pockets[iPocket]
            n = thisPocket.pos - thisBall.pos
            if( mag(n) < (ballRadius + pocketRadius)):
                thisBall.velocity = vector(0,0,0)
                thisBall.pos = vector(0, -50, 0)
                shadows[iBall].pos = thisBall.pos
                inPockets.append(thisBall)
                inPlay = 0
                numIn += 1
                        
    ballsMoving = false
    #Moving Balls and Shadows
    for iBall in range(numBalls):
        thisBall = balls[iBall]
        thisShadow = shadows[iBall]
        #Check to see if the ball is in play and if the ball has a velocity
        if(thisBall.inPlay):
            if(mag(thisBall.velocity) > 0.01):
                ballsMoving = true
                #get angular velocity
                angVelX = thisBall.velocity.x / ballRadius
                angVelZ = thisBall.velocity.z / ballRadius

                #Rotate ball
                thisBall.rotate(angle = ((angVelZ * pi)/180), axis = (1, 0, 0), origin = thisBall.pos)
                thisBall.rotate(angle = ((-angVelX * pi)/180), axis = (0, 0, 1), origin = thisBall.pos)

                #get direction of friction force
                AccX = -1 * (math.copysign(fricForce, thisBall.velocity.x))
                AccZ = -1 * (math.copysign(fricForce, thisBall.velocity.z))

                #find velocity
                thisBall.velocity.x = thisBall.velocity.x + AccX * dt
                thisBall.velocity.z = thisBall.velocity.z + AccZ * dt

                #lock balls on y
                thisBall.velocity.y = 0

                #Move balls
                thisBall.pos = thisBall.pos + thisBall.velocity * dt
                thisShadow.pos = thisBall.pos - (0, ballRadius, .2)

                #Ball Flashes on bumper hit
##                if (thisBall.material == emissive):
##                    thisBall.lifeSpan -= 1
##                    if (thisBall.lifeSpan < 0):
##                        thisBall.lifeSpan = flashTime
##                        thisBall.material = plastic

                #Bumper Checks
                if thisBall.pos.x > (.5 * tableLength - 1):
                    thisBall.velocity.x = fabs(thisBall.velocity.x) * -1 * bFriction
                    #thisBall.material = emissive
                    
                if thisBall.pos.x < -(.5 * tableLength - 1):
                    thisBall.velocity.x = fabs(thisBall.velocity.x) * bFriction
                    #thisBall.material = emissive

                if thisBall.pos.z > (.5 * tableWidth - 1):
                    thisBall.velocity.z = fabs(thisBall.velocity.z) * -1 * bFriction
                    #thisBall.material = emissive

                if thisBall.pos.z < -(.5 * tableWidth - 1):
                    thisBall.velocity.z = fabs(thisBall.velocity.z) * bFriction
                    #thisBall.material = emissive
            else:
                thisBall.velocity = vector(0,0,0)

    #Post movement processing
    if(ballsMoving == false and cueHit == true):
        if(numIn != 0):
            for iPocket in range(numIn):
                thisBall = inPockets.pop()
                #thisBall.material = plastic
                if(thisBall.ballNum == 0):
                    #scratch!
                    thisBall.pos = vector (-26, 1.625, 0)
                    shadow[0].pos = thisBall.pos - (0, ballRadius, .2)
                    thisBall.inPlay = 1               
                    if(playerTurn == 1):
                        playerTurn = 2
                        turnDisplay2.visible = true
                        turnDisplay1.visible = false
                    else:
                        playerTurn = 1
                        turnDisplay1.visible = true
                        turnDisplay2.visible = false
                elif(thisBall.ballNum == 5):
                    #game over
                    if(player1Off == 7):
                        #player 1 wins!
                        player1win.visible = true
                        isNotOver = false
                    else:
                        #player 1 loses
                        player2win.visible = true
                        isNotOver = false
                    if(player2Off == 7):
                        #player 2 wins!
                        player2win.visible = true
                        isNotOver = false
                    else:
                        #player 2 loses
                        player1win.visible = true
                        isNotOver = false
                elif((thisBall.ballNum % 2) == 0):
                    #solid, player 1 ball
                    player1Off += 1
                    thisBall.pos = ballLine1 - vector(0, (player1Off * (ballRadius * 2.1)), 0)
                    if(playerTurn == 1):
                        turnDisplay1.visible = true
                    else:
                        turnDisplay1.visible = true
                        turnDisplay2.visible = false
                        playerTurn = 1
                else:
                    #stripe, player 2 ball
                    player2Off += 1
                    thisBall.pos = ballLine2 - vector(0, (player2Off * (ballRadius * 2.1)), 0)
                    if(playerTurn == 2):
                        turnDisplay2.visible = true
                    else:
                        turnDisplay2.visible = true
                        turnDisplay1.visible = false
                        playerturn = 2
            numIn = 0
            cueHit = false
        else:
            if(playerTurn == 1):
                playerTurn = 2
                turnDisplay2.visible = true
                turnDisplay1.visible = false
            else:
                playerTurn = 1
                turnDisplay1.visible = true
                turnDisplay2.visible = false

        cueHit = false
        stick.visible = true
	
