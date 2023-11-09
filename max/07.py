import turtle as t

t.width(12)
for i in range(20):
    if i%2 == 0:
        t.color("blue")
    else:
        t.color("red")
    t.circle(5+i*5, 45)
t.done()
