from Hangman.repository.repoHang import HangmanWords, HangmanAscii
from Hangman.service.serviceHang import HangmanService
from Hangman.ui.uiHang import HangmanUI

from Rock_Paper_Scissors.repository.repoRPS import HighScoreTable, AsciiCode
from Rock_Paper_Scissors.service.serviceRPS import RPS
from Rock_Paper_Scissors.ui.uiRPS import UiJoc

def play_rock_paper_scissors():
    highscore_table = HighScoreTable()
    ascii_art = AsciiCode()
    game_service = RPS()
    game_ui = UiJoc()
    game_ui.play()

def play_hangman():
    word_repo = HangmanWords("words.txt")
    ascii_repo = HangmanAscii("asciiHangman.txt")
    hangman_service = HangmanService(word_repo, ascii_repo)
    hangman_ui = HangmanUI(hangman_service)
    hangman_ui.play()

def main():
    while True:
        print("\nAlege un joc:")
        print("1. Rock Paper Scissors")
        print("2. Hangman")
        print("3. Iesire")

        choice = input("Jocul pe care doresti sa il joci: ")

        if choice == "1":
            play_rock_paper_scissors()
        elif choice == "2":
            play_hangman()
        elif choice == "3":
            print("Te pup")
            break
        else:
            print("Optiunea aleasa nu este valida!")


if __name__ == "__main__":
    main()