from game.word_bank import Word_Bank


class Board:
    def __init__(self):
        self.word_bank = Word_Bank()

    def word_to_list(self):
        word = str(self.word_bank.get_random_word())
        list_of_letters = list(word)
        return list_of_letters

    def put_user_guess(self):
        amount_guesses = 0
        list_of_letters = self.word_to_list()
        all_guesses = []
        word_printed = []
        while amount_guesses < 100:

            user_guess = input("Make a guess: ").lower()

            all_guesses.append(user_guess)
            print(all_guesses)

            for letter in list_of_letters:
                if user_guess == letter:
                    print(user_guess)
                else:
                    amount_guesses += 1
                    print("_")
