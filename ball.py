from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.ball_speed = 0.1
        self.move()


    def move(self):
        new_x = self.xcor()+self.x_move
        new_y = self.ycor()+self.y_move
        self.goto(new_x, new_y)

    def ball_reverse(self):
        self.x_move *= -1
        self.y_move *= -1
        self.move()

    def bounce_y(self):
        self.y_move *= -1
        self.move()

    def bounce_x(self):
        self.x_move *= -1
        self.move()

