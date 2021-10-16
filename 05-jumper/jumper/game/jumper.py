# from game.console import Console

"""
Display and update jumping mans parachute
"""


class Jumper:
    def __init__(self):
        self.row1 = ("  ___  ")
        self.row2 = (" /___\ ")
        # self.row2a = ("|     | ")
        self.row3 = (" \   / ")
        self.row4 = ("  \ /  ")
        self.person1 = ("   0   \n  /|\  \n  / \  \n^^^^^^^")
        self.person2 = ("   X   \n  /|\  \n  / \  \n^^^^^^^")

    def print_jumper(self, wrong_guesses):

        if wrong_guesses == 0:

            print(self.row1)
            print(self.row2)
            # print(row2a)
            print(self.row3)
            print(self.row4)
            print(self.person1)

        elif wrong_guesses == 1:

            print(self.row2)
            # print(row2a)
            print(self.row3)
            print(self.row4)
            print(self.person1)

        elif wrong_guesses == 2:

            # print(row2a)
            print(self.row3)
            print(self.row4)
            print(self.person1)

        elif wrong_guesses == 3:

            # print(row2a)
            print(self.row4)
            print(self.person1)

        elif wrong_guesses == 4:
            print()
            print(self.person2)
            print()


def main(self):

    # console = Console()
    wrong_guesses = self.console.get_bad_guess()

    jumper = Jumper()
    jumper.print_jumper(wrong_guesses)


# if __name__ == "__main__":
#     main()
