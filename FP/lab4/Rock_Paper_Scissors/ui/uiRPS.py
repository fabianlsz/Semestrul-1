from Rock_Paper_Scissors.service.serviceRPS import RPS

class UiJoc:
    def __init__(self):
        self.game = RPS()

    def display_ascii_art(self, choice):
        print(self.game.ascii_art.art[choice])

    def display_scores(self):
        print("\nHighscores:")
        for entry in self.game.highscore_table.get_highscores():
            print(f"{entry['name']} - {entry['score']}")

    def play(self):
        print(
            "Scrie 'rock', 'paper' sau 'scissors' pentru a incepe, sau 'quit' pentru a iesi din joc.\n"
        )

        while True:
            player_choice = input("Alegerea ta: ").lower()
            if player_choice == "quit":
                break
            if player_choice not in self.game.options:
                print("Alegerea ta nu este valida, incearca din nou!.")
                continue

            computer_choice = self.game.computer_choice()

            print("\nAi ales:")
            self.display_ascii_art(player_choice)
            print("\nComputer-ul a ales:")
            self.display_ascii_art(computer_choice)
            result = self.game.winner(player_choice, computer_choice)
            if result == "draw".lower():
                print("\nRemiza!")
            elif result == "player":
                print("\nAi castigat aceasta runda!")
                self.game.score += 1
            else:
                print("\nAi pierdut!")
                print(f"Scorul tau final: {self.game.score}\n")
                save_score = input("Doresti sa iti salvezi scorul?(Da/Nu): ").lower()
                if save_score.lower() == "da":
                    name = input("Introdu numele: ")
                    (self.game.highscore_table.
                    add_hs(name, self.game.score))
                self.game.reset_score()
                self.display_scores()
                break

            print(f"Scor curent: {self.game.score}\n")
