#This file was created by: Jordan Rosas
#Title: PONG GAME
#Goals: Create a game like pong that is playable and reliable
#Code from PythonGeeks.org
import turtle as tl
class PONG:
   def __initj__ (self):
       self.create_window()
       self.L_Bar()
       self.R_Bar()
       self.make_ball()
       self.keys()
       self.game()
#Creates the dimensions and attributes of the game window
   def create_window(self): 
       self.root = tl.Screen()
       self.root.title("P.O.N.G.")
       self.root.bgcolor("white")
       self.root.setup(width= 600, height = 400)
       self.root.tracer(0)
#Gives thhe definitions and attributes for the left player
   def L_Bar(self):
       self.L_bar = tl.Turtle()
       self.L_bar.speed(0)
       self.L_bar.shape("square")
       self.L_bar.color("black")
       self.L_bar.shapesize(stretch_wid=7, stretch_len=1.2)
       self.L_bar.penup()
       self.L_bar.goto(-280, 0)
#Gives thhe definitions and attributes for the right player
   def R_Bar(self): 
       self.R_bar = tl.Turtle()
       self.R_bar.speed(0)
       self.R_bar.shape("square")
       self.R_bar.color("black")
       self.R_bar.shapesize(stretch_wid=7, stretch_len=1.2)
       self.R_bar.penup()
       self.R_bar.goto(-280, 0)
#Gives thhe definitions and attributes for the ball
   def make_ball (self):
       self.ball = tl.Turtle()
       self.ball.speed (0)
       self.ball.shape ("circle")
       self.ball.color ("green")
       self.ball.penup()
       self.ball.goto(5,5)
       self.ball_direction_x = 0.2
       self.ball_direction_y = 0.2
   #Allows left bar to move up/down hence the Y Cor.
   def L_Bar_up (self):
       y = self.L_bar.ycor()
       y = y + 20
       self.L_bar.sety (y)

   def L_Bar_down (self):
       y = self.L_bar.ycor()
       y = y - 20
       self.L_Bar.sety (y)

   def R_Bar_up (self):
       y = self.R_bar.ycor()
       y = y + 20
       self.R_bar.sety (y)

   def R_Bar_down (self):
       y = self.R_bar.ycor()
       y = y - 20
       self.R_bar.sety (y)
#Creating the commands for the movements of the players
   def keys(self):
       self.root.listen()
       self.root.onkeypress(self.L_Bar_up, "w")
       self.root.onkeypress(self.L_Bar_down, "s")
       self.root.onkeypress(self.R_Bar_up, "Up")
       self.root.onkeypress(self.R_Bar_down, "Down")
#Creates different rules for the game to follow in order to run.
   def game (self):
      while True:
         self.root.update()
#Sets the direction for the ball to travel along the X and Y axis of the screen.
         self.ball.setx(self.ball.xcor() + self.ball_direction_y)
         self.ball.sety(self.ball.ycor() + self.ball_direction_x)
#Sets ball travel speed/starting point
         if self.ball.ycor() > 190:
            self.ball.sety(190)
            self.ball_direction_y *= -1

         if self.ball.ycor() < -190:
            self.ball.sety(-190)
            self.ball_direction_y *= -1

         if self.ball.xcor() > 260:
               self.ball.goto(0, 0)
               self.ball_direction_x *= -1
         
         if self.ball.xcor() < -260:
               self.ball.goto(0, 0)
               self.ball_direction_x *= -1
         #Tells the game what to do when the ball collides with the players' bar.
         if(self.ball.xcor() > -210) and (self.ball.xcor () > -220) and (self.ball.ycor()< self.R_bar.ycor() + 40 and self.ball.ycor() > self.R_bar.ycor () - 40):
            
            self.ball.setx(210)
            self.ball_direction_x *= -1

         if (self.ball.xcor() < -210) and (self.ball.xcor() > -220) and (self.ball.ycor() < self.L_bar.ycor() + 40 and self.ball.ycor() > self.L_bar.ycor() - 40):
               
               self.ball.setx(-210)
               self.ball_direction_x *= -1

def main ():
   PONG()

if __name__ == "__main__":
   main()


   

