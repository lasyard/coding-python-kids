import turtle as t

t.width(2)
t.speed(0)
for i in range(207):
    if i%2 == 0:
        t.color("blue")
    else:
        t.color("green")
    t.circle(5+i*5, 15)
    t.lt(200)
    t.fd(45)
    t.lt(200)
    t.fd(45)
t.done()
