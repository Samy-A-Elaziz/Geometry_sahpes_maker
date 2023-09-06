# imports we use
import turtle as point
import colorama 
from colorama import Fore

"""
function to ask user if he want to repeat using app or not
"""
def drawing_again():
    again_or_not = input(f"{Fore.WHITE}For drawing again press (1)\nFor not press (2)\nEnter")
    while again_or_not != "1" and again_or_not != "2":
        again_or_not = input(f"{Fore.WHITE}For drawing again press (1)\nFor not press (2)\nEnter: ")
    if again_or_not == "1":
        point.clear()
        drawing()
    if again_or_not == "2":
        print(f"{Fore.WHITE}See you soon \U0001F618 \n BYE!!")

"""
function to start drawing 
"""
def drawing():
    no_of_points = int(input(f"{Fore.WHITE}Enter the number of points: "))
    no_of_repeat, begin_point = 0, 0
    while no_of_repeat != no_of_points:
        if begin_point == 0:
            begin_point += 1
            begin_point_or_not = input("For begin from origin point press (1)\n For begin from another point press(2)\nEnter: ")
            while begin_point_or_not != "1" and begin_point_or_not != "2":
                input("For begin from origin point press (1)\n For begin from another point press(2)\nEnter: ")
            if begin_point_or_not == "1":
                point.penup()
                point.goto(0,0)
                point.pendown()
            elif begin_point_or_not == "2":
                no_of_repeat += 1
                print(f"{Fore.RED}set x cordinate to begin\n x=")
                x_cordinate = int(input())
                print(f"{Fore.BLUE}set y cordinate to begin\n y=")
                y_cordinate = int(input())
                point_cordinate = print(f"{Fore.WHITE}Point {no_of_repeat} cordinate (x={x_cordinate},y={y_cordinate})")
                point.speed(1)
                point.penup()
                point.color("black")
                point.goto(x_cordinate,y_cordinate)
                point.pendown()
        else:
            no_of_repeat += 1
            print(f"{Fore.RED}set x cordinate \n x=")
            x_cordinate = int(input())
            print(f"{Fore.BLUE}set y cordinate \n y=")
            y_cordinate = int(input())
            point_cordinate = print(f"{Fore.WHITE}Point {no_of_repeat} cordinate (x={x_cordinate},y={y_cordinate})")
            point.speed(1)
            point.color("black")
            point.goto(x_cordinate,y_cordinate)
    if no_of_repeat == no_of_points:
            drawing_again()
# start drawing
drawing()
