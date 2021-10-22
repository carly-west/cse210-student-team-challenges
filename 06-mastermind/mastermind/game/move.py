'''takes the guess and compares it to the generated number'''


class Move:
    def __init__(self):
        self.number_list = []
        self.rand_to_print = ['*', '*', '*', '*']

    def number_to_list(self, number1):
        # Sets number to ['4', '5', '3', '2']
        number_to_string = str(number1)
        self.number_list = list(number_to_string)
        return self.number_list

    def compare_guess(self, guess, rand_num):
        guess_list = self.number_to_list(guess)
        rand_num_list = self.number_to_list(rand_num)
        if guess_list == rand_num_list:
            return True
        if guess_list != rand_num_list:
            # rand_num = ['4', '5', '3', '2']
            # guess = ['3', '7', '2', '9']
            # rand_to_print = ['*', '*', '*', '*']
            # Compare guess to list
            for i in guess:
                if i in rand_num:
                    rand_to_print.replace(i, "O")
            print(rand_to_print)
