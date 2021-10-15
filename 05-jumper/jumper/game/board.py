from game.word_bank import Word_Bank


class Board:
    def __init__(self):
        self.word_bank = Word_Bank()

    def print(self):
        self.word_bank.get_random_word()
        print(f"This is the random word: {self.word_bank.rand_word}")

    def word_to_list(self):
        print(f"{self.word_bank.rand_word}")
        # word = self.word_bank.get_random_word()
        # list_of_letters = list(word)
        # print(list_of_letters)
