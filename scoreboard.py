from turtle import Turtle
FONT = ("Arial", 20, "normal")
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.r_score = 0
        self.l_score = 0

    def right_score(self):
        self.write(f"{self.r_score}",False, "center",font=FONT)

    def left_score(self):
        self.write(f"{self.l_score}",False, "center",font=FONT)

    def right_updated_score(self):
        self.clear()
        self.r_score += 1
        self.right_score()

    def left_updated_score(self):
        self.clear()
        self.l_score += 1
        self.left_score()


