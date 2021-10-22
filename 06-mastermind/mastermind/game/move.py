'''takes the guess and compares it to the generated number'''

class Move:
    def __init__(self):
        self.number_list = []

    def number_to_list(self, number1):
        number_to_string = str(number1)
        self.number_list = number_to_string.split()
        print(self.number_list)
        return self.number_list
    
    # def compare_guess(self, number, guess):
        # if guess == number:
