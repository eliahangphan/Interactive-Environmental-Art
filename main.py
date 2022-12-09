'''
main.py
Hang (Elia) Phan
@eliahangphan
12/09/2022

------------------------------------
This file contains the functions to create the final scenes.
------------------------------------
'''

import tkinter as tk
import graphics
import database
import lsystem
import screen
import random as r


'''
THIS PART BELOW IS FOR SCENE 2 ('What is glacier?'):
----------------------------------------------------------------
'''

def screen2_sub(root):
    '''Creates a sub screen for scene 2.'''
    screen2sub = screen.TurtleInterpreter(root, 400,600, TopScreen=True)
    
    #Draws a snowflake
    lsys = lsystem.Lsystem('lsystem_snowflake.txt')
    screen2sub.myturtle.pencolor('#FFFFF9')
    screen2sub.turtle_setting(0,-50, color = '#7394DE')
    screen2sub.drawString(lsys.buildString(5),4)

    #Insert the description text
    text1 = 'Glaciers form when it snows in the same area year round.' 
    text2 = 'New snow layers compress previous layers, forming grains.' 
    text3 = 'The air pockets between grains get smaller, forming crystals.'
    text4 = 'Large crystals become compressed that can be in adult-fist size.' 
    text5 = 'For most glaciers, this process takes more than 1,000 years.'
    text6 = '(Source: National Snow and Ice Data Center)'
    list = [text1, text2, text3, text4, text5, text6]
    ypos = -200

    #Put the text onto the screen2sub object
    for i in list:
        label1 = tk.Label(screen2sub.mycanvas.master, text=i, highlightthickness=0, background='#686F82', font='Courier, 9')
        screen2sub.mycanvas.create_window(-170, ypos, window = label1, anchor='w')
        ypos += 20


def button4(root, screen2):
    '''Creates the 'Get info' button in scene 2.'''
    button4 = tk.Button(screen2.mycanvas.master, text='Get info', highlightthickness=0, background='#7E8793', command=lambda: screen2_sub(root))
    screen2.mycanvas.create_window(80, 250, window = button4, height = 40, width = 80)


def screen2(root):
    '''Creates screen2 object.'''
    screen2 = screen.TurtleInterpreter(root, 400,600, TopScreen=True)

    #Draws five growing snowflakes using L-system
    lsys = lsystem.Lsystem('lsystem_snowflake.txt')
    screen2.myturtle.pencolor('#FFFFF9')

    def draw_lystem2(screen2, num):
        '''Draws five snowflakes from L-system using recursion.'''
        if num > 0:
            screen2.turtle_setting(screen2.width/5,num*100-310, color = '#7394DE')
            screen2.drawString(lsys.buildString(num),4)
            draw_lystem2(screen2, num-1)

    draw_lystem2(screen2, 5)
    
    #Draws an iceberg.
    screen2.myturtle.pencolor('#000000')
    stack = graphics.iceberg(screen2.myturtle, screen2.width, screen2.height, 5)

    #Draws the pattern inside the iceberg
    i = 5
    for ypos1, ypos2, num in [(-245,-240,40), (-220,-180,30), (-150,-90,20),(-50,50,10), (100,225,5)]:
        for j in range(num):
            screen2.turtle_setting(r.uniform(-150, -40), r.uniform(ypos1, ypos2), color = '#FFF8F7', pencolor='#FFF8F7', penwidth=1)
            screen2.drawString(lsys.buildString(6-i),1)
        i -= 1

    button4(root, screen2)



'''
THIS PART BELOW IS FOR SCENE 3 ('Milk Glacier'):
----------------------------------------------------------------
'''


def draw_mountain(screen3, x, y, ice = False):
    '''Draws mountains on screen3.'''
    #Two big mountains at the back
    graphics.rock(screen3.myturtle, 2, x, y-30, 9, 10, ice)
    graphics.rock(screen3.myturtle, 1, x-250, y-70, 8, 10, ice)

    #Patterns in the inside area
    ypos = -40
    for i in range(200):
        if ice == True:
            screen3.myturtle.pencolor('#E6E6E1')
            graphics.rock(screen3.myturtle, 1, r.randrange(-100,150), ypos, r.randrange(2,3), 5, ice = True, melt=False)
        elif ice == False:
            screen3.myturtle.pencolor('#23B5CC')
            graphics.rock(screen3.myturtle, 1, r.randrange(-100,150), ypos, r.randrange(2,3), 5, ice = True, melt=True)
        ypos -= 1.3
    screen3.myturtle.pencolor('black')

    #Three big mountains in the front
    graphics.rock(screen3.myturtle, 2, x-350, y-250, 10, 10, ice)
    graphics.rock(screen3.myturtle, 3, x-220, y-290, 10, 10, ice)
    graphics.rock(screen3.myturtle, 1, x+90, y-290, 8, 8, ice)

    graphics.rock(screen3.myturtle, 1, -40, -600, 2, 5, ice)


def draw_tree(screen3):
        '''Draws trees for scene 3.'''
        screen3.myturtle.pencolor('green')
        xpos, ypos = 15, -40
        for i in range(5):
            graphics.tree(screen3.myturtle, xpos,ypos,1)
            xpos += 15
            ypos += 10
        xpos = 60
        for i in range(5):
            graphics.tree(screen3.myturtle, xpos,-20,1)
            xpos += 20
        xpos, ypos = -90, -50
        for i in range(4):
            graphics.tree(screen3.myturtle, xpos,ypos,1)
            xpos += 15
            ypos -= 25
        xpos, ypos = 0, -200
        for i in range(6):
            graphics.tree(screen3.myturtle, xpos,ypos,1)
            xpos += 20
            ypos -= 5


def draw_scene3(screen3, ice = False):
    '''Draw the whole scene for screen3.'''
    draw_mountain(screen3, 0, 0, ice)

    #This is the picture of the melted Milk Lake Glacier (which is drawn in screen3_sub) 
    if ice == False: 
        draw_tree(screen3)

    
def screen3_sub(root):
    '''Creates the subscreen for screen3 object.'''
    screen3sub = screen.Screen(root, 400,600, TopScreen=True)

    #Draw scene with glacier melted
    draw_scene3(screen3sub, False)

    #Insert description text
    text1 = 'Though it can take 1,000 years to form a glacier,'
    text2 = 'Milk Lake Glacier (1st picture in 1988) melted so rapidly' 
    text3 = 'that was entirely gone in 2009 (2nd picture)!'
    list = [text1, text2, text3]

    #Put text onto the screen3sub object
    ypos = -250
    for i in list:
        label1 = tk.Label(screen3sub.mycanvas.master, text=i, highlightthickness=0, background='#686F82', font='Courier, 10')
        screen3sub.mycanvas.create_window(-150, ypos, window = label1, anchor='w')
        ypos += 20


def screen3(root):
    '''Creates screen3 object.'''
    screen3 = screen.Screen(root, 400,600, TopScreen=True)
    draw_scene3(screen3, True)
   
    #Creates 'Get info' button
    button5 = tk.Button(screen3.mycanvas.master, text='Get info', highlightthickness=0, background='#7E8793', command= lambda: screen3_sub(root))
    screen3.mycanvas.create_window(-100, -250, window = button5, height = 40, width = 80)



'''
THIS PART BELOW IS FOR SCENE 1 (Main Scene):
----------------------------------------------------------------
'''

def screen1sub(root):
    screen1sub = screen.Screen(root, width = 500, height = 250, TopScreen=True)
    '''Draws the sub screen for scene 1.'''
    #Intro text
    text1 = '       This interactive environmental art depicts global climate change reality'
    text2 = 'and hope to call for actions. The graph illustrates the  global temperature'
    text3 = 'animolies from 1880 to 2021, rising especially rapidly from the start of the'
    text4 = '21st century. Experience this art piece for more information.'
    text5 = ''
    text6 = 'User guide: Use mouse to control the slider at the bottom of  the  main'
    text7 = 'scene to see the global temperature anomaly for each year. Click on any'
    text8 = 'button in any order to see more informative graphics or descriptions.'
    text9 = ''
    text10 = 'Data reference: NOAA National Centers for Environmental information.' 
    text11 = 'Hang Phan, 2022, made by Python 3.9.1.'
    list = [text1, text2, text3, text4, text5, text6, text7, text8, text9, text10, text11]
    
    #Put text onto the screen1sub object
    ypos = -100
    for i in list:
        label1 = tk.Label(screen1sub.mycanvas.master, text=i, highlightthickness=0, background='#686F82', font='Courier, 9')
        screen1sub.mycanvas.create_window(-210, ypos, window = label1, anchor='w')
        ypos += 20


def year_to_temp(year, data):
    '''Converts the year chosen by the slide to the associated temperature written in button1.'''
    return data[year] 


def draw_lsystem(screen1):
    '''Draws the part of the main scene that is related to lsystem.py onto screen1 object.'''
    lsys = lsystem.Lsystem('lsystem_snowflake.txt')
    screen1.turtle_setting(xpos= -350, ypos= 130, color= '#7394DE')
    screen1.drawString(lsys.buildString(5),5)


def draw_data(root, screen1):
    '''Draws the part of the main scene that is related to database.py onto screen1 object.'''
    data = database.Database('1880-2022.csv')
    screen1.graph(data.data_dict, data.vertical_pos, data.vertical_neg, data.horizontal)
    screen1.connect_point(data, data.vertical_pos, data.vertical_neg, data.horizontal)

    def button1(var):
        '''Creates button1 (associated with the slider).'''
        text = 'Global anomaly in ' + str(slide1.get()) + ' is ' + str(year_to_temp(slide1.get(), data.data_dict))
        button1 = tk.Button(screen1.mycanvas.master, text=text, highlightthickness=0, background='#7E8793')
        screen1.mycanvas.create_window(0, screen1.height/2-50, window = button1, height = 40, width = 200)

    #Creates a slider for user to get the keys and values of the data dictionary using mouse (sliding)
    slide1 = tk.Scale(screen1.mycanvas.master, from_= data.horizontal[0], to= data.horizontal[-1], orient='horizontal', command= button1, highlightthickness=0, background='#7E8793', activebackground='#7E8793')
    screen1.mycanvas.create_window(0, 260, window = slide1, width=screen1.width)
    
    #Creates button2 to open screen2 (About the glacier formation process)
    button2 = tk.Button(screen1.mycanvas.master, text='What is a glacier? Click here!', command=lambda: screen2(root=root), highlightthickness=0, background='#7E8793')
    screen1.mycanvas.create_window(-350, -230, window = button2, height = 40, width = 160)

    #Creates button3 to open screen3 (About the Milk Lake Glacier)
    button3 = tk.Button(screen1.mycanvas.master, text='Milk Glacier 1988-2009: Click here!', command=lambda: screen3(root=root), highlightthickness=0, background='#7E8793')
    screen1.mycanvas.create_window(350, 200, window = button3, height = 40, width = 190)


def draw_waterdrop(screen1):
    '''Draws water drop for scene1.'''
    screen1.myturtle.pensize(2)
    screen1.myturtle.pencolor('black')
    ypos = 220
    scale = 3
    for i in range(3):
        graphics.water_drop(screen1.myturtle, 350, ypos, scale)
        ypos -= 15
        scale -= 0.5
    screen1.myturtle.pencolor('black')


def draw_smoke(screen1):
    '''Draws smoke for scene1.'''
    scale = 0.5
    for xpos, ypos in [(0,1), (90,2), (-70,-10), (70,-15), (-5,2), (60,-20), (-70,30), (70,-35)]:
        screen1.turtle_setting(xpos = xpos, ypos = ypos, color='black', pencolor = 'black')
        graphics.smoke(screen1.myturtle, xpos, ypos, scale)
        scale -= 0.05


def draw_cloud(screen1):
    '''Draws cloud for scene1.'''
    screen1.myturtle.fillcolor('black')
    screen1.myturtle.pencolor('black')
    screen1.turtle_setting(xpos = 30, ypos = 120)
    graphics.cloud(screen1.myturtle, 30, 120, 0.9)


def screen1(root):
    '''Creates scene1 object.'''
    screen1 = screen.TurtleInterpreter(root, width = 1000, height = 550, column=1,  row=1)
    graphics.triangle(screen1.myturtle, 0, 300)

    draw_lsystem(screen1)
    draw_data(root, screen1)
    draw_waterdrop(screen1)
    draw_cloud(screen1)
    draw_smoke(screen1)
    screen1sub(root)

    screen1.myscreen.tracer(True)


def main():
    root = tk.Tk()
    root.geometry('1000x550')
    root.title('Interactive Environmental Art')
    root.config(background='#E4E8F0')

    screen1(root)
    root.mainloop()


if __name__ == '__main__':
    main()