from game.word_bank import Word_Bank

class Board:
    def __init__(self):


        self.word_bank = Word_Bank()

    def print(self):
        self.word_bank.get_random_word()
        print(f"This is the random word: {self.word_bank.rand_word}")