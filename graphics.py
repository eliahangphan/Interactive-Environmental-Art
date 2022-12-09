'''
graphics.py
Hang (Elia) Phan
@eliahangphan
12/09/2022

------------------------------------
This file contains functions that use turtle object to draw graphics shapes.
------------------------------------
'''

import turtle
import tkinter as tk
import random as r


def goto(turt, xpos, ypos):
    '''Moves turtle object to (x,y) position.'''
    turt.up()
    turt.goto(xpos, ypos)
    turt.down()


'''
THIS PART BELOW IS FOR SCENE 2 ('What is a glacier?'):
----------------------------------------------------------------
'''


global stack
stack = []

def iceberg(turt, screen_width, screen_height, num):
    '''Creates a iceberg shape using recursion.'''
    colorlist = ['#1B526B', '#27779C', '#3196C4', '#39ADE3', '#40C2FF']
    turt.fillcolor(colorlist[num-1])
    turt.begin_fill()
    goto(turt, -screen_width*3/7, -screen_height*5.5/13)
    turt.setheading(90)
    for i in range(2):
        turt.forward((screen_height-100)/5*(num)*((num)/5))
        stack.append(turt.position())
        turt.rt(90)
        turt.forward(screen_width/2-50)
        turt.rt(90)
    turt.end_fill()

    if num > 0:
        iceberg(turt, screen_width, screen_height, num-1)   #RECURSION

    return stack
    

def iceberg_test():
    '''Test function for iceberg().'''
    screen = turtle.Screen()
    screen.screensize(400,600)
    turt = turtle.Turtle()

    iceberg(turt, 300, 300, 5)


'''
THIS PART BELOW IS FOR SCENE 3 ('Milk Glacier'):
----------------------------------------------------------------
'''


def rock_pattern(turt, list, num):
    '''Creates patterns for the mountain.'''
    list = sorted(list)
    turt.pencolor('black')

    def draw_pattern(x1, y1, x2, y2, num):
        '''Creates patterns for the mountain.'''
        xpos = x1
        ypos = y1
        while x1 <= xpos <= x2:
            goto(turt, xpos, list[0][1])
            turt.goto(xpos, ypos)
            xpos += abs((x2-x1))/num
            ypos = (y2-y1)/(x2-x1)*xpos+(y2-((y2-y1)/(x2-x1))*x2)

    for i in range(0,len(list)-1):
        draw_pattern(list[i][0], list[i][1], list[i+1][0], list[i+1][1], num-1)
    draw_pattern(list[-1][0], list[-1][1], list[0][0], list[0][1], num+4)


def rock1(turt, xpos, ypos, scale, num, fill = False, melt = False):
    '''Draws the first shape of mountain. 
    fill = True: Draws the shadow part of the mountain.
    melt = False: Draws the rock shape in blue color.'''
    list = []
    if melt == True:
        turt.fillcolor('#4193C8')
    else:
        turt.fillcolor('white')
    turt.begin_fill()
    goto(turt, xpos, ypos)
    list.append(turt.position())
    turt.setheading(80)
    turt.forward(16*scale)
    list.append(turt.position())
    turt.rt(63)
    turt.forward(10*scale)
    list.append(turt.position())
    turt.rt(20)
    turt.forward(16*scale)
    list.append(turt.position())
    turt.rt(60)
    turt.forward(20*scale)
    list.append(turt.position())
    turt.goto(xpos, ypos)
    turt.end_fill()

    if fill == True:
        rock_pattern(turt, list, num)


def rock2(turt, xpos, ypos, scale, num, fill = False, melt = False):
    '''Draws the second shape of mountain. 
    fill = True: Draws the shadow part of the mountain.
    melt = False: Draws the rock shape in blue color.'''
    list = []
    if melt == True:
        turt.fillcolor('#4193C8')
    else:
        turt.fillcolor('white')
    turt.begin_fill()
    goto(turt, xpos, ypos)
    list.append(turt.position())
    turt.setheading(60)
    turt.forward(18*scale)
    list.append(turt.position())
    turt.rt(40)
    turt.forward(10*scale)
    list.append(turt.position())
    turt.lt(35)
    turt.forward(8*scale)
    list.append(turt.position())
    turt.rt(120)
    turt.forward(19*scale)
    list.append(turt.position())
    turt.lt(21)
    turt.forward(12*scale)
    list.append(turt.position())
    turt.goto(xpos, ypos)
    turt.end_fill()

    if fill == True:
        rock_pattern(turt, list, num)


def rock3(turt, xpos, ypos, scale, num, fill = False, melt = False):
    '''Draws the third shape of mountain.
    fill = True: Draws the shadow part of the mountain.
    melt = False: Draws the rock shape in blue color.'''
    list = []
    if melt == True:
        turt.fillcolor('#4193C8')
    else:
        turt.fillcolor('white')
    turt.begin_fill()
    goto(turt, xpos, ypos)
    list.append(turt.position())
    turt.setheading(60)
    turt.forward(11*scale)
    list.append(turt.position())
    turt.rt(40)
    turt.forward(9*scale)
    list.append(turt.position())
    turt.lt(30)
    turt.forward(7*scale)
    list.append(turt.position())
    turt.rt(120)
    turt.forward(10*scale)
    list.append(turt.position())
    turt.lt(60)
    turt.forward(8*scale)
    list.append(turt.position())
    turt.rt(30)
    turt.forward(11*scale)
    list.append(turt.position())
    turt.goto(xpos, ypos)
    turt.end_fill()

    if fill == True:
        rock_pattern(turt, list, num)


def rock(turt, type, xpos, ypos, scale, num, ice, melt=False):
    '''A general function to draw a mountain of choice (type: 1,2,3).'''
    if type == 1:
        rock1(turt, xpos, ypos, scale, num, False, melt)
        if ice == False: rock1(turt, xpos+20, ypos, scale-1, num, True)
    if type == 2:
        rock2(turt, xpos, ypos, scale, num, False, melt)
        if ice == False: rock2(turt, xpos+20, ypos, scale-1, num, True)
    if type == 3:
        rock3(turt, xpos, ypos, scale, num, False, melt)
        if ice == False: rock3(turt, xpos+20, ypos, scale-1, num, True)


def rock_test():
    '''Test function for rock1(), rock2(), rock3().'''
    screen = turtle.Screen()
    screen.screensize(400,600)
    turt = turtle.Turtle()
    turt.speed(0)

    rock1(turt, -100, -100, 10, 5)
    rock2(turt, -100, -100, 10, 5)
    rock3(turt, -100, -100, 10, 5)


def tree(turt,x,y, scale):
    '''Draws a tree.'''
    goto(turt,x,y)
    turt.setheading(90)
    turt.pendown()
    turt.pensize(5)
    turt.begin_fill()
    for i in range (3):
        turt.setheading(90)
        turt.forward(10*scale)
        turt.setheading(0)
        for i in range(3):
            turt.fd(5*scale)
            for i in [10,10,5]:
                turt.lt(120)
                turt.fd(i*scale)
    turt.end_fill()
    turt.penup()
    turt.setheading(0)



'''
THIS PART BELOW IS FOR SCENE 1 (Main Scene):
----------------------------------------------------------------
'''

def cloud(turt, xpos, ypos, scale):
    '''Creates a cloud shape'''
    for i in range(2):
        turt.begin_fill()
        turt.setheading(90)
        turt.circle(30*scale)
        turt.end_fill()
        for i in range(2):
            turt.begin_fill()
            turt.penup()
            turt.setheading(150)
            turt.forward(40*scale)
            turt.pendown()
            turt.circle(30*scale)
            turt.end_fill()
        scale *= -1
    


def cloud_test():
    '''Test function for cloud().'''
    screen = turtle.Screen()
    screen.screensize(400,600)
    turt = turtle.Turtle()
    turt.speed(0)

    cloud(turt,250,200,1)


def water_drop(turt,xpos, ypos, scale):
    '''Creates water drop shape.'''
    turt.fillcolor('#A1C9D1')
    turt.begin_fill()
    goto(turt, xpos, ypos)
    turt.setheading(270)
    turt.rt(30)
    turt.forward(30*scale)
    turt.setheading(270)
    turt.circle(15*scale,180)
    turt.setheading(0)
    turt.goto(xpos, ypos)
    turt.end_fill()


def water_drop_test():
    '''Test function for water_drop().'''
    screen = turtle.Screen()
    screen.screensize(400,600)
    turt = turtle.Turtle()
    turt.speed(0)

    water_drop(turt, 0,0,3)


def triangle(turt, xpos, ypos):
    turt.fillcolor('#FCD62D')
    turt.begin_fill()
    goto(turt, xpos-100, ypos) #0,300
    turt.goto(xpos-230,ypos-700)
    turt.goto(xpos+230,ypos-700)
    turt.goto(xpos+100, ypos)
    turt.goto(xpos-100, ypos)
    turt.end_fill()


def smoke(turt, xpos, ypos, scale):
    '''Creates smoke shape.'''
    rad = 20*scale
    cloud(turt, xpos, ypos, scale)
    turt.setheading(0)
    goto(turt, xpos + 3*(8-scale), ypos + 3*(8-scale))
    cloud(turt, xpos, ypos, scale*0.8)
    scale -= 1


def smoke_test():
    '''Test function for smoke()'''
    screen = turtle.Screen()
    screen.screensize(400,600)
    turt = turtle.Turtle()
    turt.speed(0)

    smoke(turt, 0,0,1)


if __name__ == '__main__':
    #iceberg_test()
    #rock_test()
    #water_drop_test()
    #cloud_test()
    smoke_test()
