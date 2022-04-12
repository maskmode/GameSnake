from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 250)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score} Highscore: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset_game(self):
        # if self.score > self.high_score:
        #     self.high_score = self.score
        self.clear()
        self.score = 0
        self.update_scoreboard()


    #
    #
    # game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)
    #     self.score = 0

    def increase_score(self):
        self.clear()
        self.score += 1
        if self.score > self.high_score:
            self.clear()
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")


        self.update_scoreboard()



