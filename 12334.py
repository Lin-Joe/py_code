import time
from Transbot_Lib import Transbot
from ipywidgets import interact
import ipywidgets as widgets
bot = Transbot()
bot.create_receive_threading()

enable = True
bot.set_auto_report_state(enable, forever=False)
enable=False
bot.clear_auto_report_data()

bot.set_car_motion(0,0)

x = 100
y = 200
z = 100

while(1):
    a = input("请输入")

    print(a)
    if a=="s":
        bot.set_car_motion(-1, 0)
    elif a=="w":
        bot.set_car_motion(1, 0)
    elif a=="a":
        bot.set_car_motion(0, 1)
    elif a == "d":
        bot.set_car_motion(0, -1)

    elif a=="u":
        x = x-10
        bot.set_uart_servo_angle(7,x,800)
    elif a=="j":
        x = x+10
        bot.set_uart_servo_angle(7,x,800)

    elif a == "i":
        y = y - 10
        bot.set_uart_servo_angle(8, y, 800)
    elif a == "k":
        y = y + 10
        bot.set_uart_servo_angle(8, y, 800)

    elif a=="o":
        z = z-10
        bot.set_uart_servo_angle(9,z,400)
    elif a=="l":
        z = z+10
        bot.set_uart_servo_angle(9,z,400)

    elif a == " ":
        bot.set_car_motion(0, 0)

while True:
    i=input("getkey")
    if i==“q”:
        line =-line
        bot. set_car_motion(line/100.0, angular/100.0)
    elif i=="z":
        angular= -angular
        bot. set_car_motion(line/100, angular/100.0)
    elif i=="w":
        line =line*9.9
        angular = angular*9.9
        bot. set_car_motion(line/100, angular/100)