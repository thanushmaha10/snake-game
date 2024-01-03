from turtle import Turtle
ALIGNMENT = "center"
FONT = ("arial", 10, "bold")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.points = 0
        with open("data.txt") as file:
            self.high_score = int(file.read())
        self.color("white")
        self.penup()
        self.goto(0, 280)
        self.update()
        self.hideturtle()

    def update(self):
        self.clear()
        self.write(arg=f"Score : {self.points} High Score : {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset_game(self):
        if self.points > self.high_score:
            self.high_score = self.points
            with open("data.txt", mode="w") as file:
                file.write(f"{self.high_score}")
        self.points = 0
        self.update()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(arg="GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.points += 1
        self.update()
