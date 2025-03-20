class HangmanUI:
    def __init__(self, hangman_service):
        self.service = hangman_service

    def display_state(self):
        state = self.service.get_game_state()
        print("\n" + state["ascii_stage"])
        print(f"Cuvant: {state['hidden_word']}")
        print(f"Litere: {state['guessed_letters']}")
        print(f"Incercari ramase: {state['max_attempts'] - state['attempts']}")

    def play(self):
        print("Bine ai venit la 'Hangman'!")
        while True:
            self.display_state()
            if self.service.is_won():
                print("\nFelicitari!Ai castigant")
                break
            if self.service.is_lost():
                print("\nAi pierdut! Cuvantul era:", self.service.word)
                break

            letter = input("Introdu o litera: ").lower()
            if len(letter) != 1 or not letter.isalpha():
                print("Trebuei sa introduci o singura litera!")
                continue

            message = self.service.guess_letter(letter)
            print(message)
