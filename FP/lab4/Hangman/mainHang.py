from Hangman.repository.repoHang import HangmanWords, HangmanAscii
from Hangman.service.serviceHang import HangmanService
from Hangman.ui.uiHang import HangmanUI

def main():
    word_repo = HangmanWords("../words.txt")
    ascii_repo = HangmanAscii("../asciiHangman.txt")
    hangman_service = HangmanService(word_repo, ascii_repo)
    hangman_ui = HangmanUI(hangman_service)
    hangman_ui.play()

if __name__ == "__main__":
    main()
