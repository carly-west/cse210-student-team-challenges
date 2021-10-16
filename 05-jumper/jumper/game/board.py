from game.word_bank import Word_Bank
from game.welcome import Welcome


class Board:
    def __init__(self):
        self.word_bank = Word_Bank()
        self.welcome = Welcome()

    def word_to_list(self):
        word = str(self.word_bank.get_random_word())
        list_of_letters = list(word)
        return list_of_letters

    def put_user_guess(self):
        amount_turns = 9
        amount_guesses = 0
        list_of_letters = self.word_to_list()
        all_guesses = []
        letter_dashed = []
        gameOver = False

        while amount_guesses < amount_turns and not gameOver:
            for i in list_of_letters:
                letter_dashed.append("_")

            while not gameOver:

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
                    print(letter_dashed)
                    print(list_of_letters)
                    if user_guess in list_of_letters:
                        for i in range(len(list_of_letters)):
                            if user_guess == list_of_letters[i]:
                                letterIndex = i
                                letter_dashed[letterIndex] = user_guess
                            if letter_dashed == list_of_letters:
                                print("heyyyy")
                                print(
                                    f"Great job, {self.welcome.welcome_user()}")
                                gameOver = True

                    else:
                        print(f"{user_guess} was not in the word.")
                        amount_guesses += 1
                    print()
                    print(' '.join(letter_dashed))
                    print()
