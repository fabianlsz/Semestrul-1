class HighScoreTable:
    hs_file = "highscore.txt"

    def __init__(self):
        self.scores = self.load_scores()

    def load_scores(self):
        scores = []
        try:
            with open(self.hs_file, "r") as file:
                for line in file:
                    name, score = line.strip().split(":")
                    scores.append({"name": name, "score": int(score)})
        except FileNotFoundError:
            pass
        return scores

    def save_score(self):
        with open(self.hs_file, "w") as file:
            for entry in self.scores:
                file.write(f"{entry['name']}:{entry['score']}\n")

    def get_highscores(self):
        return sorted(self.scores, key=lambda x: x["score"], reverse=True)

    def add_hs(self, name, score):
        for entry in self.scores:
            if entry["name"] == name:
                if score > entry["score"]:
                    entry["score"] = score
                break
        else:
            self.scores.append({"name": name, "score": score})

        self.save_score()


class AsciiCode:
    ascii_file = "asciiRPS.txt"

    def __init__(self):
        self.art = self.load_ascii()

    def load_ascii(self):
        ascii_dict = {}
        try:
            with open(self.ascii_file, "r") as file:
                art = file.read().split(
                    "\n\n"
                )  # doua randuri distanta intre desenele ascii ca sa fie distincte
                keys = ["rock", "paper", "scissors"]
                for i in range(len(keys)):
                    ascii_dict[keys[i]] = art[i]
        except FileNotFoundError:
            ascii_dict = {
                "rock": "rock in cod ascii",
                "paper": "hartie in cod ascii",
                "scissors": "foarcefa in cod ascii",
            }
        return ascii_dict