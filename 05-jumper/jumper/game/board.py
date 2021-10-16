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
        letter_dashed = []

        for i in list_of_letters:
            letter_dashed.append("_")

        while list_of_letters != letter_dashed:

            user_guess = input("Make a guess: ").lower()

            if user_guess.isnumeric():
                print("Silly goose, you need to input a letter!")

            elif user_guess in all_guesses:
                print("Silly goose, you have already guessed that!")

            elif len(user_guess) > 1:
                print("Silly goose, only input one letter!")

            else:
                all_guesses.append(user_guess)
                print(all_guesses)


                if user_guess in list_of_letters:
                    for i in range(len(list_of_letters)):
                        if user_guess == list_of_letters[i]:
                            letterIndex = i
                            letter_dashed[letterIndex] = user_guess
                print()
                print(' '.join(letter_dashed))
                print()
