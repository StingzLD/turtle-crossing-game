from turtle import Turtle

FONT = ("Courier", 24, "normal")
POSITION = (-280, 260)


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.setposition(POSITION)
        self.color("white")
        self.display_level(1)

    def display_level(self, level):
        self.clear()
        self.write(f"Level: {level}",
                   align="Left",
                   font=FONT)

    def game_over(self):
        self.setposition(x=0, y=-20)
        self.write("YOU DIED",
                   align="center",
                   font=FONT)
