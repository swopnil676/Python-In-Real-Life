import turtle as t
t.speed(0)
t.setposition(-40,-30)
t.bgcolor("black")
t.color("aqua")

for i in range(160):
    t.rt(i)     #Rotate turtle right by i degrees
    t.circle(170, i)    #Radius = 170 and Angle = i

    t.fd(100)   #Moves turtle forward by 100 units and Extends the pattern outward
    t.right(240)    #Moves turtle forward by 100 units and Extends the pattern outward

    t.fd(i)     #Moves forward by i
                # Distance increases each loop:
                # 1st → 0
                # 50th → 50
                # 100th → 100
    t.lt(1)     #Helps avoid repeating same shape Smooths the spiral
    t.hideturtle()  #Makes drawing look clean
t.done()