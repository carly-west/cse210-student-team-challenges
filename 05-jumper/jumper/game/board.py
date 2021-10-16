from game.word_bank import Word_Bank
from game.jumper import Jumper


class Board:
    def __init__(self):
        self.word_bank = Word_Bank()
        self.word = ""
        self.jumper = Jumper()

    def word_to_list(self):
        self.word = str(self.word_bank.get_random_word())
        list_of_letters = list(self.word)
        return list_of_letters

    def put_user_guess(self):
        amount_turns = 3
        amount_guesses = 0
        list_of_letters = self.word_to_list()
        all_guesses = []
        letter_dashed = []
        gameOver = False

        while not gameOver:

            for i in list_of_letters:
                letter_dashed.append("_")

            while not gameOver:
                if letter_dashed == list_of_letters:
                    print()
                    print(f"Great job! You guessed the word!")
                    print()
                    gameOver = True
                elif amount_guesses > amount_turns:
                    gameOver = True
                    self.jumper.print_jumper(amount_guesses)

                    print("The jumper has drowned!")
                    print()
                    print(f"The word was: {self.word}")
                    print()
                else:
                    print()
                    print(' '.join(letter_dashed))
                    print()
                    self.jumper.print_jumper(amount_guesses)

                    print()
                    user_guess = input("Make a guess: ").lower()
                    print()

                if not gameOver:
                    if user_guess.isnumeric():
                        print("Silly goose, you need to input a letter!")
                    elif not user_guess or user_guess.isspace():
                        print("Please provide a letter.")

                    elif user_guess in all_guesses:
                        print("Silly goose, you have already guessed that!")

                    elif len(user_guess) > 1:
                        print("Silly goose, only input one letter!")

                    else:
                        all_guesses.append(user_guess)
                        # print(list_of_letters)

                        if user_guess in list_of_letters:
                            for i in range(len(list_of_letters)):
                                if user_guess == list_of_letters[i]:
                                    letterIndex = i
                                    letter_dashed[letterIndex] = user_guess

                        else:
                            print(
                                f"The letter '{user_guess}' was not in the word.")
                            amount_guesses += 1
