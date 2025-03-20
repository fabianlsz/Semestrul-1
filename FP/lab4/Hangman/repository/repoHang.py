import random

class HangmanWords:
    def __init__(self, file_path="words.txt"):
        self.file_path = file_path
        self.words = self.load_words()

    def load_words(self):
        try:
            with open(self.file_path, "r") as file:
                return [line.strip().lower() for line in file if line.strip()]
        except FileNotFoundError:
            return ["pisica", "caine","animal"]

    def get_random_word(self):
        return random.choice(self.words) if self.words else None


class HangmanAscii:
    def __init__(self, file_path="asciiHangman.txt"):
        self.file_path = file_path
        self.stages = self.load_ascii_stages()

    def load_ascii_stages(self):
        try:
            with open(self.file_path, "r") as file:
                return file.read().split("\n\n")
        except FileNotFoundError:
            return ["stage1", "st2", "st3","st4","st5"]

    def get_stage(self, attempt):
        if 0 <= attempt < len(self.stages):
            return self.stages[attempt]
        return ""
