'''takes the guess and compares it to the generated number'''
import sys


class Move:
    def __init__(self):
        self.number_list = []
        self.rand_to_print = ['*', '*', '*', '*']

    def number_to_list(self, number1):
        # Sets number to ['4', '5', '3', '2']
        # number_to_string = str(number1)
        self.number_list = [int(x) for x in str(number1)]

        return self.number_list

    def compare_guess(self, guess, rand_num):

        if guess == rand_num:
            print('\nYou Won!!!')
            exit()
        elif guess != rand_num:
            for i in guess:
                if i in rand_num:
                    spot = -1
                    rand_to_print = ['*', '*', '*', '*']

                    for i in guess:
                        spot += 1
                        if i in rand_num:
                            rand_to_print[spot] = "O"

                            if rand_num[spot] == guess[spot]:
                                rand_to_print[spot] = 'X'

            return rand_to_print
