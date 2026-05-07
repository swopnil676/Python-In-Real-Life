# import PySimpleGUI as sg
# class Hangman:
#     def __init__(self) -> None:
#         self._window = sg.Window(
#             title="Hangman",
#             layout=[[]],
#             finalize=True,
#             margins=(100,100),
#         )
#     def read_event(self):
#         event = self._window.read()
#         event_id = event[0] if event is not None else None
#         return event_id
#     def close(self):
#         self._window.close()

import PySimpleGUI as sg
import random

WORDS = ["python", "programming", "hangman", "computer", "keyboard", "software", "algorithm", "variable"]
MAX_WRONG = 6

HANGMAN_STAGES = [
    """
  +---+
  |   |
      |
      |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
      |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
  |   |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========""",
    """
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
========="""
]


class Hangman:
    def __init__(self) -> None:
        self._word = random.choice(WORDS)
        self._guessed = set()
        self._wrong = 0

        layout = self._build_layout()

        self._window = sg.Window(
            title="Hangman",
            layout=layout,
            finalize=True,
            margins=(20, 20),
            font=("Courier New", 12),
        )
        self._update_display()

    def _build_layout(self):
        # Alphabet buttons (2 rows)
        alpha_row1 = [sg.Button(c.upper(), key=f"LETTER_{c}", size=(3, 1)) for c in "abcdefghijklm"]
        alpha_row2 = [sg.Button(c.upper(), key=f"LETTER_{c}", size=(3, 1)) for c in "nopqrstuvwxyz"]

        return [
            [sg.Text("HANGMAN", font=("Courier New", 20, "bold"), justification="center", expand_x=True)],
            [sg.HorizontalSeparator()],
            [
                sg.Multiline(
                    HANGMAN_STAGES[0],
                    key="GALLOWS",
                    size=(20, 10),
                    disabled=True,
                    no_scrollbar=True,
                    font=("Courier New", 14),
                ),
                sg.Column([
                    [sg.Text("Word:", font=("Courier New", 12, "bold"))],
                    [sg.Text("", key="WORD_DISPLAY", font=("Courier New", 22, "bold"))],
                    [sg.Text("Wrong guesses:", font=("Courier New", 12, "bold"))],
                    [sg.Text("", key="WRONG_DISPLAY", font=("Courier New", 12))],
                    [sg.Text("", key="STATUS_MSG", font=("Courier New", 13, "bold"), text_color="red")],
                ], vertical_alignment="top", pad=(20, 0))
            ],
            [sg.HorizontalSeparator()],
            [alpha_row1],
            [alpha_row2],
            [sg.Button("New Game", key="NEW_GAME"), sg.Button("Quit", key="QUIT")],
        ]

    def _update_display(self):
        # Update gallows drawing
        self._window["GALLOWS"].update(HANGMAN_STAGES[self._wrong])

        # Update word display
        display = " ".join(
            letter if letter in self._guessed else "_"
            for letter in self._word
        )
        self._window["WORD_DISPLAY"].update(display)

        # Update wrong guesses
        wrong_letters = sorted(l for l in self._guessed if l not in self._word)
        self._window["WRONG_DISPLAY"].update(", ".join(l.upper() for l in wrong_letters) or "—")

        # Check win/loss
        if all(letter in self._guessed for letter in self._word):
            self._window["STATUS_MSG"].update("🎉 You win!", text_color="green")
            self._disable_buttons()
        elif self._wrong >= MAX_WRONG:
            self._window["STATUS_MSG"].update(f"💀 You lose! Word: {self._word.upper()}", text_color="red")
            self._disable_buttons()
        else:
            self._window["STATUS_MSG"].update("")

    def _disable_buttons(self):
        for c in "abcdefghijklmnopqrstuvwxyz":
            self._window[f"LETTER_{c}"].update(disabled=True)

    def _reset(self):
        self._word = random.choice(WORDS)
        self._guessed = set()
        self._wrong = 0
        for c in "abcdefghijklmnopqrstuvwxyz":
            self._window[f"LETTER_{c}"].update(disabled=False)
        self._update_display()

    def read_event(self):
        event_data = self._window.read()
        event_id = event_data[0] if event_data is not None else None
        return event_id

    def handle_event(self, event_id):
        if event_id is None or event_id == "QUIT" or event_id == sg.WIN_CLOSED:
            return False  # Signal to quit

        if event_id == "NEW_GAME":
            self._reset()

        elif event_id.startswith("LETTER_"):
            letter = event_id.split("_")[1].lower()
            if letter not in self._guessed:
                self._guessed.add(letter)
                if letter not in self._word:
                    self._wrong += 1
                self._window[f"LETTER_{letter}"].update(disabled=True)
                self._update_display()

        return True  # Continue running

    def close(self):
        self._window.close()


def main():
    game = Hangman()
    while True:
        event = game.read_event()
        if not game.handle_event(event):
            break
    game.close()


if __name__ == "__main__":
    main()