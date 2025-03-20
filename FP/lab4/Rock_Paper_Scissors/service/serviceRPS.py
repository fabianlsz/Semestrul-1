import random

from Rock_Paper_Scissors.repository.repoRPS import HighScoreTable, AsciiCode


class RPS:
    def __init__(self):
        self.score = 0
        self.options = ["rock", "paper", "scissors"]
        self.highscore_table = HighScoreTable()
        self.ascii_art = AsciiCode()

    def computer_choice(self):
        return random.choice(self.options)

    def winner(self, player_choice, computer_choice):
        if player_choice == computer_choice:
            return "Draw".lower()
        elif (
            (player_choice == "rock" and computer_choice == "scissors")
            or (player_choice == "scissors" and computer_choice == "paper")
            or (player_choice == "paper" and computer_choice == "rock")
        ):
            return "player"
        else:
            return "computer"

    def reset_score(self):
        self.score = 0
