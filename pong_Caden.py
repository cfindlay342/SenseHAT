from sense_hat import SenseHat
from time import sleep
sense = SenseHat()

white = (255,255,255)
red = (255,0,0)
       

bat_y = 4

def draw_bat():
    sense.set_pixel(0, bat_y, white)
    sense.set_pixel(0, bat_y + 1, white)
    sense.set_pixel(0, bat_y - 1, white)
    
def draw_ball():
    sense.set_pixel(ball_position[0],ball_position[1], red)
    ball_position[0] += ball_velocity[0]
    if ball_position == 7:
        ball_velocity[0] =- ball_velocity[0]

draw_bat()
draw_ball()

sense.clear(0,0,0)

def move_up(event):
    global bat_y
    if event.action == 'pressed' and bat_y > 1:
        bat_y -= 1

def move_down(event):
    global bat_y
    if event.action == 'pressed' and bat_y > 1:
        bat_y -= -1
    

while True:
    draw_bat()
    draw_ball()
    sense.stick.direction_up = move_up
    sense.stick.direction_down = move_down
    
