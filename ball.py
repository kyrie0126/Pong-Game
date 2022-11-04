from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move = 5
        self.y_move = 5

    def move(self):
        x_new = self.xcor() + self.x_move
        y_new = self.ycor() + self.y_move
        self.goto(x_new, y_new)

    def wall_bounce(self):
        self.y_move *= -1

# 50 above/below x_cor
    def paddle_bounce(self):
        self.x_move *= -1

    def respawn(self):
        self.clear()
        self.goto(0, 0)
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move = 5
        self.y_move = 5
        self.move()



