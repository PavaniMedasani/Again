import turtle as t
import random as r
t.tracer(8,25)
t.colormode(255)
for i in range(25):
 t.pencolor("black")
 x=0
 for i in range(4):
  a = r.randint(0,255)
  b = r.randint(0,255)
  c = r.randint(0,255)
  t.color(a,b,c)
  t.begin_fill()
  for i in range(0,180):
    t.lt(0.5)
    t.forward(1)
  t.lt(90)
  for j in range(0,180):
    t.lt(0.5)
    t.fd(1)
  t.end_fill()
 t.lt(x+5)
t.ht()
t.done()
