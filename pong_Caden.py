from sense_hat import SenseHat
from time import sleep
sense = SenseHat()

white = (255,255,255)

bat_y = 4

def draw_bat():
    sense.set_pixel(0, bat_y, white)
    sense.set_pixel(0, bat_y + 1, white)
    sense.set_pixel(0, bat_y - 1, white)

draw_bat()

def move_up(event):
    global bat_y
    if event.action == 'pressed' and bat_y > 1:
        bat_y -= 1
    

while True:
    draw_bat()
    sense.stick.direction_up = move_up
    
