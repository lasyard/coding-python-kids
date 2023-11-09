import turtle as t

t.width(2)
t.ht()
t.speed(0)
for i in range(400):
    if i%2 == 0:
        t.color("green")
    else:
        t.color("blue")
    t.circle(i*5+5, 15)
    t.lt(200)
    t.fd(30)
t.done()
