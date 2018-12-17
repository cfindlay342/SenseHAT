from sense_hat import SenseHat
from time import sleep
sense = SenseHat()

white = (255,255,255)
red = (255,0,0)
purple = (255,0,255)
ball_position = [4,4]
ball_velocity = [1,1]
ball_velocity2 = [-1,-1]
ball_position2 = [3,3]
sense.set_pixel (0,0,purple)
       

bat_y = 4

def draw_bat():
    sense.set_pixel(0, bat_y, white)
    sense.set_pixel(0, bat_y + 1, white)
    sense.set_pixel(0, bat_y - 1, white)
    
def draw_ball():
   sense.set_pixel(ball_position[0], ball_position[1], red)
   ball_position[0] += ball_velocity[0]
   if ball_position[0] == 7 or ball_position[0] == 0:
       ball_velocity[0] = -ball_velocity[0]
   ball_position[1] += ball_velocity[1]
   if ball_position[1] == 7 or ball_position[1] == 0:
       ball_velocity[1] = -ball_velocity[1]
   if  ball_position[0] == 1 :
       ball_velocity[0] = -ball_velocity[0]
    
def draw_ball2():
   sense.set_pixel(ball_position2[0], ball_position2[1], red)
   ball_position2[0] += ball_velocity2[0]
   if ball_position2[0] == 7 or ball_position2[0] == 0:
       ball_velocity2[0] = -ball_velocity2[0]
   ball_position2[1] += ball_velocity2[1]
   if ball_position2[1] == 7 or ball_position2[1] == 0:
       ball_velocity2[1] = -ball_velocity2[1]
   if  ball_position2[0] == 1:
       ball_velocity2[0] = -ball_velocity2[0]
       
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
    sense.stick.direction_up = move_up
    sense.stick.direction_down = move_down
    sleep(0.25)
    sense.clear(0, 0, 0)
    draw_ball()
    sense.set_pixel (0,0,purple)
    draw_ball2()


