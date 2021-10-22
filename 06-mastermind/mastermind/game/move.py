'''takes the guess and compares it to the generated number'''

class Move:
    def __init__(self):
        self.number_list = []

    def number_to_list(self, number1):
        number_to_string = str(number1)
        self.number_list = list(number_to_string)
        print(self.number_list)
        return self.number_list
    
    def compare_guess(self, guess, rand_num):
        guess_list = self.number_to_list(guess)
        rand_num_list = self.number_to_list(rand_num)
        if guess_list == rand_num_list:
            return True
        if guess_list != rand_num_list:
            # Compare guess to list 
