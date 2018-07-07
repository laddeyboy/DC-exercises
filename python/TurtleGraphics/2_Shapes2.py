from turtle import *


def triangle(size, fill, my_color):
    if fill:
      color(my_color)
      begin_fill()
      for i in range(3):
          forward(size)
          left(120)
      end_fill()
    else:
      for i in range(3):
          forward(size)
          left(120)
    
def square(size, fill, my_color):
  if fill:
    color(my_color)
    begin_fill()
    for i in range(4):
      forward(size)
      left(90)
    end_fill()
  else:
    for i in range(4):
      forward(size)
      left(90)
    
def pentagon(size, fill, my_color):
    if fill:
      color(my_color)
      begin_fill()
      for i in range(5):
          forward(size)
          left(72)
      end_fill()
    else:
      for i in range(5):
          forward(size)
          left(72)
    
def hexagon(size, fill, my_color):
    if fill:
      color(my_color)
      begin_fill()
      for i in range(6):
          forward(size)
          left(60)
      end_fill()
    else:
      for i in range(6):
          forward(size)
          left(60)
        
def octagon(size, fill, my_color):
  if fill:
    color(my_color)
    begin_fill()
    for i in range(8):
        forward(size)
        left(45)
    end_fill()
  else:
    for i in range(8):
        forward(size)
        left(45)
        
def star(size, fill, my_color):
  if fill:
    color(my_color)
    begin_fill()
    for i in range(5):
        forward(size)
        right(144)
    end_fill()
  else:
    for i in range(5):
        forward(size)
        right(144)

def my_circle(size, fill, my_color):
  if fill:
    color(my_color)
    begin_fill()
    circle(size)
    end_fill()
  else:
    circle(size)
