'''
screen.py
Hang (Elia) Phan
@eliahangphan
12/09/2022

------------------------------------
This file contains the Screen Class and its Child Classes, the TurtleInterpreter Class.
------------------------------------
'''

import turtle
import tkinter as tk


class Screen:
    def __init__(self, root, width, height, column= None, row= None, bgcolor = None, TopScreen = False):
        '''Initializes Screen object.'''
        if TopScreen == True:
            top_screen = tk.Toplevel(root)
            self.canvas = tk.Canvas(top_screen)
        else:
            self.canvas = tk.Canvas(root, highlightthickness=0)
        
        self.canvas.grid(column=column, row=row, padx=0, pady=0)
        self.canvas.config(width=width, height=height, bg='#686F82')
        self.width = width
        self.height = height

        self.myscreen = turtle.TurtleScreen(self.canvas)
        self.myscreen.bgcolor('#686F82')
        self.myscreen.tracer(False)
        self.myturtle = turtle.RawTurtle(self.myscreen)
        self.myturtle.hideturtle()
        self.myturtle.pensize(2)
        
        self.mycanvas = self.myscreen.getcanvas()
        self.mycanvas.config(background='#686F82')

        self.stack = []

        if bgcolor != None:
            self.myscreen.bgcolor(bgcolor)


    def turtle_setting(self, xpos=None, ypos=None, angle=None, penwidth=None, speed=None, color = None, pencolor = None):
        '''Mutate the Turtle object associated with the Screen object.'''
        if xpos !=None:
            self.myturtle.penup()
            self.myturtle.setx(xpos)
            self.myturtle.pendown()
        if ypos != None:
            self.myturtle.penup()
            self.myturtle.sety(ypos)
            self.myturtle.pendown()
        if angle != None:
            self.myturtle.setheading(angle)
        if penwidth != None:
            self.myturtle.width(penwidth)
        if speed != None:
            self.myturtle.speed(speed)
        if color != None:
            self.myturtle.fillcolor(color)
        if pencolor != None:
            self.myturtle.pencolor(color)
    


    def graph(self, data, data_ver_pos, data_ver_neg, data_hor, xpos = None, ypos = None):
        '''Creates a graph on the Screen object using given dict of database with the Turtle object.'''
        global unit_ver_neg
        unit_ver_neg = 0
        global unit_ver_pos
        unit_ver_pos = 0

        #Set the position for the turtle
        if xpos == None:
            self.turtle_setting(xpos = (-self.width/2))
        else:
            self.turtle_setting(xpos = xpos)
        if ypos == None:
            self.turtle_setting(ypos = (-self.height/6))
        else:
            self.turtle_setting(ypos = ypos)
            
        #Calculate the x-unit and y-unit of the graph
        if len(data_ver_pos)>0:
            unit_ver_pos = (self.height*4)/(9*max(data_ver_pos))
        if len(data_ver_neg)>0:
            unit_ver_neg = (self.height*2)/(9*min(data_ver_neg))
        
        unit_hor = (self.width/len(data_hor))
        
        #Draw the graph by matching dict keys (horizontal graph values) with dict values (vertical graph values)
        stack = []
        for i in data.keys():
            self.myturtle.forward(unit_hor)
            if data[i] > 0: #If the vertical graph values is positive, turtle goes upward
                self.myturtle.setheading(90)
                self.myturtle.forward(unit_ver_pos * data[i])
                stack.append(self.myturtle.position())
                self.myturtle.backward(unit_ver_pos * data[i])
            elif data[i] < 0: #If the vertical graph values is negative, turtle goes downward
                self.myturtle.setheading(270)
                self.myturtle.forward(unit_ver_neg * data[i])
                stack.append(self.myturtle.position())
                self.myturtle.backward(unit_ver_neg * data[i])
            self.myturtle.setheading(0)
        self.stack = stack #set stack as the list of the top vertical points in the graph


    def connect_point(self, data, data_ver_pos, data_ver_neg, data_hor):
        '''Draws lines matching top points in the graph of the given dict of database 
        on the Screen object with the Turtle object.'''
        
        #First third of the database: matching top points in the graph
        self.turtle_setting(xpos=self.stack[0][0], ypos=self.stack[0][1], color='#2C1C75')
        self.myturtle.begin_fill()
        for i in self.stack[:int(len(self.stack)/3)]:
            self.myturtle.goto(x=i[0], y =i[1]) #go to the next top point
        self.myturtle.end_fill()
        
        #Last third of the database: matching top points in the graph
        self.turtle_setting(xpos=self.stack[int(len(self.stack)*2/3)][0], ypos=self.stack[int(len(self.stack)*2/3)][1], color='#B2C4D9')
        self.myturtle.begin_fill()
        for i in self.stack[int(len(self.stack)*2/3):]:
            self.myturtle.goto(x=i[0], y =i[1]) #go to the next top point
        self.myturtle.end_fill()

        #Second third of the database: 
        self.turtle_setting(penwidth=5)
                #Trace the second third of the graph again with penwidth = 5
        self.graph(data.data2, data_ver_pos, data_ver_neg, data_hor, ypos = (-self.height/6+3), xpos=(-self.width/6-5)) 


class TurtleInterpreter(Screen):
    def __init__(self, root, width, height, column= None, row= None, bgcolor = None, TopScreen = False):
        '''Initializes Turtle Interpreter Screen object.'''
        super().__init__(root, width, height, column, row, bgcolor, TopScreen)


    def drawString(self, dstring, distance):
        """ Interpret the characters in string dstring as a series of turtle commands.
        F: go forward a distance
        +: turn right 60 degree
        -: turn left 60 degree
        [: store the position of the turtle
        ]: restore the last position of the turtle"""
        stack = []
        self.myturtle.begin_fill()
        for char in dstring:
            if char == 'F':
                self.myturtle.forward(distance)
            elif char == '+':
                self.myturtle.right(60)
            elif char == '-':
                self.myturtle.left(60)
            elif char == '[':
                stack.append(self.myturtle.position())
                stack.append(self.myturtle.heading())
            elif char == ']':
                self.myturtle.penup()
                self.myturtle.setheading(stack.pop())
                self.myturtle.goto(stack.pop())
                self.myturtle.pendown()
        self.myturtle.end_fill()