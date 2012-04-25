from visual import *
x = 0
y = 0
z = 0

yaxistop = arrow(pos=(0,0,0), axis=(0,100,0), shaftwidth=.2,color=color.blue)
yaxisbottom = arrow(pos=(0,0,0), axis=(0,-100,0), shaftwidth=.2,color=color.blue)
xaxisright = arrow(pos=(0,0,0), axis=(100,0,0), shaftwidth=.2,color=color.red)
xaxisleft = arrow(pos=(0,0,0), axis=(-100,0,0), shaftwidth=.2,color=color.red)
ball = sphere(pos=(x,y,z), radius=5, color=color.green)
label(pos=(-75,20,0), text='X-Axis')
label(pos=(25,80,0), text='Y-Axis')


while True:
    rate(100)
    if scene.kb.keys:
        s = scene.kb.getkey() 
    
        if s == 'up':
            y = y + 3
            ball.pos = (x,y,z)

        if s == 'down':
            y = y - 3 
            ball.pos = (x,y,z)

        if s == 'right':
            x = x + 3
            ball.pos = (x,y,z)
        if s == 'left':
            x = x - 3
            ball.pos = (x,y,z)
            
        loc = ball.pos
        locstr = str(loc)
        label(pos=(60,-70,0), text=locstr,box=false)
