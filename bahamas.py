import turtle as t

t.fillcolor("#2962ff")
t.begin_fill()
t.right(90)
t.forward(40)
t.left(90)
t.forward(200)
t.left(90)
t.forward(40)
t.left(90)
t.forward(200)
t.end_fill()

t.fillcolor("yellow")
t.begin_fill()
t.left(90)
t.forward(80)
t.left(90)
t.forward(200)
t.left(90)
t.forward(40)
t.left(90)
t.forward(200)
t.end_fill()

t.fillcolor("#2962ff")
t.begin_fill()
t.left(90)
t.forward(80)
t.left(90)
t.forward(200)
t.left(90)
t.forward(40)
t.left(90)
t.forward(200)
t.end_fill()

t.home()
t.fillcolor("black")
t.begin_fill()
t.right(90)
for i in range(3):
    t.forward(120)
    t.left(120)
t.end_fill()

t.done()