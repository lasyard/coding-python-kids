import turtle as t

t.width(10)
for i in range(20):
    if i%2 == 0:
        t.color("red")
    else:
        t.color("blue")
    t.circle(i*5+5, 45)
t.done()
