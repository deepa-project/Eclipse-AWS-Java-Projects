import turtle
from time import sleep

t=turtle.Pen();
print("Drawing a square");
t.forward(50);
t.left(90);
t.forward(50);
t.left(90);
t.forward(50);
t.left(90);
t.forward(50);
t.left(90);
t.reset();
t.clear();

sleep(10);
print("Drawing two lines");
t.reset();
t.backward(100);
sleep(10);
t.up();
sleep(10);
t.right(90);
sleep(10);
t.forward(20);
sleep(10);
t.left(90);
sleep(10);
t.down();
t.forward(100);
sleep(10);
t.reset();
t.clear();

