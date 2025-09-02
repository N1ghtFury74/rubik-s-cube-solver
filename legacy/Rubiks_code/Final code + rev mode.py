from tkinter import *
from tkinter import colorchooser
import tkinter as tk
from rubik_solver import utils
import serial

import time


root = Tk()
root.title("Rubik's cube solver")
#root.geometry("575x575")
# bg = PhotoImage(file="D:/project/momentum.JPG")
#root.iconbitmap(r"C:\Users\aboha\OneDrive\Pictures")
SOLVED = "L2B2R2B2F2R2D'U2B2R2BU'L'RD'B2UBRU'R"
# 1/Taking colors of inputs :
cube_sol =  ["" for i in range(0,6)] # making array of 6faces of colors
cube_state = 'wbwbygrygoogwbwgrbybwgrgowwoygrgobybrwbyooyooyrrbwrygr'
#cube_state = ''
serial_data = ''
temp = 0
def grid_yellow(): #position of grid with center yellow
    global cube_sol
    cube_sol[0] = " "
    for x in range(2,5):
        for(y) in range(50,53):
            color_yellow = colorchooser.askcolor()[1]
            sol = color_yellow
            cube_sol[0] += sol
            cube_sol[0] += " "
            canvsa_yellow = Canvas(root,width=50,height=50,bg=color_yellow).grid(row=x,column=y)
                            
def grid_blue():# position of grid with center blue
    global cube_sol
    cube_sol[1] = " "
    for x in range(6,9):
        for(y) in range(40,43):
            color_blue = colorchooser.askcolor()[1]
            sol = color_blue
            cube_sol[1] += sol
            cube_sol[1] += " "
            canvsa_blue = Canvas(root,width=50,height=50,bg=color_blue).grid(row=x,column=y)

def grid_red():# position of grid with center red
    global cube_sol
    cube_sol[2] = " "
    for x in range(6,9):
        for(y) in range(50,53):
            color_red = colorchooser.askcolor()[1]
            sol = color_red
            cube_sol[2] += sol
            cube_sol[2] += " "
            canvsa_red = Canvas(root,width=50,height=50,bg=color_red).grid(row=x,column=y)

def grid_white():# position of grid with center white
    global cube_sol
    cube_sol[5] = " "
    for x in range(9,12):
        for(y) in range(50,53):
            color_white = colorchooser.askcolor()[1]
            sol = color_white
            cube_sol[5] += sol
            cube_sol[5] += " "
            canvsa_white = Canvas(root,width=50,height=50,bg=color_white).grid(row=x,column=y)  

def grid_green():# position of grid with center green
    global cube_sol
    cube_sol[3] = " "
    for x in range(6,9):
        for(y) in range(54,57):
            color_green = colorchooser.askcolor()[1]
            sol = color_green
            cube_sol[3] += sol
            cube_sol[3] += " "
            canvsa_green = Canvas(root,width=50,height=50,bg=color_green).grid(row=x,column=y)

def grid_orange(): # position of grid with center green
    global cube_sol
    cube_sol[4] = " "
    for x in range(6,9):
        for(y) in range(58,61):
            color_orange = colorchooser.askcolor()[1]
            sol = color_orange
            cube_sol[4] += sol
            cube_sol[4] += " "
            canvsa_orange = Canvas(root,width=50,height=50,bg=color_orange).grid(row=x,column=y) 

def convert_hex():
     global cube_state
     cube_state = ""
     face1 = cube_sol[0].split()
     face2 = cube_sol[1].split()
     face3 = cube_sol[2].split()
     face4 = cube_sol[3].split()
     face5 = cube_sol[4].split()
     face6 = cube_sol[5].split()
     for i in range(0,9):
            #face 1 :
            if face1[i] ==  "#ffffff" : cube_state += 'w'
            if face1[i] == "#ff0000" : cube_state += 'r'
            if face1[i] == "#ffff00" : cube_state += 'y'
            if face1[i] == "#00ff00" : cube_state += 'g'
            if face1[i] == "#ff8000" : cube_state += 'o'
            if face1[i] == "#0000ff" : cube_state += 'b'
     for i in range(0,9):        
            #face 2 :
            if face2[i] ==  "#ffffff" : cube_state += 'w'
            if face2[i] == "#ff0000" : cube_state += 'r'
            if face2[i] == "#ffff00" : cube_state += 'y'
            if face2[i] == "#00ff00" : cube_state += 'g'
            if face2[i] == "#ff8000" : cube_state += 'o'
            if face2[i] == "#0000ff" : cube_state += 'b'
     for i in range(0,9):
            #face 3 :
            if face3[i] ==  "#ffffff" : cube_state += 'w'
            if face3[i] == "#ff0000" : cube_state += 'r'
            if face3[i] == "#ffff00" : cube_state += 'y'
            if face3[i] == "#00ff00" : cube_state += 'g'
            if face3[i] == "#ff8000" : cube_state += 'o'
            if face3[i] == "#0000ff" : cube_state += 'b'
     for i in range(0,9):
            #face 4 :
            if face4[i] ==  "#ffffff" : cube_state += 'w'
            if face4[i] == "#ff0000" : cube_state += 'r'
            if face4[i] == "#ffff00" : cube_state += 'y'
            if face4[i] == "#00ff00" : cube_state += 'g'
            if face4[i] == "#ff8000" : cube_state += 'o'
            if face4[i] == "#0000ff" : cube_state += 'b'
     for i in range(0,9):
            #face 5 :
            if face5[i] ==  "#ffffff" : cube_state += 'w'
            if face5[i] == "#ff0000" : cube_state += 'r'
            if face5[i] == "#ffff00" : cube_state += 'y'
            if face5[i] == "#00ff00" : cube_state += 'g'
            if face5[i] == "#ff8000" : cube_state += 'o'
            if face5[i] == "#0000ff" : cube_state += 'b'
     for i in range(0,9):
             #face 6 :
            if face6[i] ==  "#ffffff" : cube_state += 'w'
            if face6[i] == "#ff0000" : cube_state += 'r'
            if face6[i] == "#ffff00" : cube_state += 'y'
            if face6[i] == "#00ff00" : cube_state += 'g'
            if face6[i] == "#ff8000" : cube_state += 'o'
            if face6[i] == "#0000ff" : cube_state += 'b'





def test() :
     global cube_state 
     global cube_sol  
     print(cube_state)


def solve():
    global cube_state
    global serial_data
    print(cube_state)
    serial_data = utils.solve(cube_state, 'Kociemba') # 'Beginner' - 'CFOP' - Kociemba
    print(serial_data)


def send_arduino():
    global serial_data
    ser = serial.Serial('COM6',9600)  # write port on which you connected your Arduino
    time.sleep(3)
    ser.write("".join(map(str, serial_data)).encode())
    
    while ser.in_waiting == 0:
        pass
    time.sleep(1)
    while ser.in_waiting > 0:
        print(ser.read().decode('"utf-8"','strict'), end="")
    ser.close()

def send_reversed():
    moves = "".join(map(str, serial_data))
    reversed_moves = list(reversed(moves))
    reversed_str = ""
    for i in range(len(reversed_moves)):
        if reversed_moves[i] == '2':
            reversed_str += reversed_moves[i+1] + reversed_moves[i]
        elif i > 0 and reversed_moves[i - 1] == '2':
            continue
        elif reversed_moves[i] == '\'':
            reversed_str += reversed_moves[i + 1]
        elif i > 0 and reversed_moves[i - 1] == '\'':
            continue
        else:
            reversed_str += reversed_moves[i] + '\''

    ser = serial.Serial('COM6',9600)  # write port on which you connected your Arduino
    time.sleep(3)
    ser.write(reversed_str.encode())
    
    while ser.in_waiting == 0:
        pass
    time.sleep(1)
    while ser.in_waiting > 0:
        print(ser.read().decode('"utf-8"','strict'), end="")
    ser.close()



Button_yellow  = Button(root,text="Grid:yellow",command=grid_yellow,bg="#FFFF00").grid(row=0,column=1)  
Button_blue  = Button(root,text="Grid:blue",command=grid_blue,bg="#0000FF").grid(row=0,column=2)  
Button_red  = Button(root,text="Grid:RED",command=grid_red,bg="#FF0000").grid(row=0,column=3)  
Button_white  = Button(root,text="Grid:White",command=grid_white,bg="#FFFFFF").grid(row=0,column=6)  
Button_green  = Button(root,text="Grid:Green",command=grid_green,bg="#00FF00").grid(row=0,column=4)  
Button_orange  = Button(root,text="Grid:Orange",command=grid_orange,bg="#FFA500").grid(row=0,column=5)
Button_sol  = Button(root,text="Get solution ->",command=solve,bg="#00a0b0").grid(row=0,column=67)
Button_send  = Button(root,text="Send to arduino ->",command=send_arduino,bg="#006069").grid(row=0,column=68)
Button_send  = Button(root,text="Send Reversed ->",command=send_reversed,bg="#0060DD").grid(row=0,column=69)
Button_command  = Button(root,text="test_code -> terminal",command=test,bg="#26c2e3").grid(row=0,column=66)
Button_command2  = Button(root,text="convert first -> ",command=convert_hex,bg="#006069").grid(row=0,column=65)





root.mainloop()

