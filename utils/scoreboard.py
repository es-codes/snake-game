from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.score = 0
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.scoreboard()
    
    def scoreboard(self):
        self.write(f'Score: {self.score}', align='center', font=('Arial', 16, 'normal'))

    def game_over(self):
        self.goto(0, 0)
        self.write(f'GAME OVER', align='center', font=('Arial', 16, 'normal'))
    
    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f'Score: {self.score}', align='center', font=('Arial', 16, 'normal'))
