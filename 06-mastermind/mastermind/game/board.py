'''sets up the board'''


class Board:

    def print_empty(self, name):
        print(f"Player {name}: ----, ****")

    def print_screen(self, name, guess, comparison):
        guess_str = "".join(guess)
        comparison_str = "".join(comparison)
        print(f"Player {name}: {guess_str}, {comparison_str} ")

    def print_line(self):
        print('\n-----------------------\n')
