'''sets up the board'''


class Board:

    def print_empty(self, name):
        print(f"Player {name}: ----, ****")

    def print_screen(self, name, guess, comparison):
        print(f'comparison {comparison}')

        strings = [str(integer) for integer in guess]
        guess_str = "". join(strings)

        comparison_str = "".join(comparison)
        print(f"Player {name}: {guess_str}, {comparison_str} ")

    def print_line(self):
        print('-----------------------')
