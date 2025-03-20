class HangmanService:
    def __init__(self, wordshg, asciihg):
        self.wordshg = wordshg
        self.asciihg = asciihg
        self.reset_game()

    def reset_game(self):
        self.word = self.wordshg.get_random_word()
        self.hidden_word = ["_"] * len(self.word) if self.word else []
        self.guesses = set()
        self.attempts = 0
        self.max_attempts = len(self.asciihg.stages) - 1

    def guess_letter(self, letter):
        if not self.word:
            return "Nu exista cuvinte in fisierul words.txt."

        if letter in self.guesses:
            return "Litera a fost ghicita deja."

        self.guesses.add(letter)

        if letter in self.word:
            for i, char in enumerate(self.word):
                if char == letter:
                    self.hidden_word[i] = letter
            return "Litera este coreta."
        else:
            self.attempts += 1
            return "Litera nu se afla in cuvant."

    def is_won(self):
        return "_" not in self.hidden_word

    def is_lost(self):
        return self.attempts >= self.max_attempts

    def get_game_state(self):
        return {
            "hidden_word": " ".join(self.hidden_word),
            "attempts": self.attempts,
            "max_attempts": self.max_attempts,
            "ascii_stage": self.asciihg.get_stage(self.attempts),
            "guessed_letters": ", ".join(sorted(self.guesses)),
        }
