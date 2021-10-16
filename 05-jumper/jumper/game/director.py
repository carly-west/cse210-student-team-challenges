from game.board import Board
from game.word_bank import Word_Bank


class Director:
    def __init__(self):
        self.play_again = True
        self.board = Board()
        self.isFirstGame = True

    def start_game(self):
        isFirstGame = True
        while self.play_again:
            if isFirstGame == False and self.play_again:
                self.get_inputs()
                self.board.put_user_guess()
            elif isFirstGame == True:
                print()
                print("Welcome to Jumper!")
                self.board.put_user_guess()
                isFirstGame = False

    def get_inputs(self):

        self.board.word_to_list()

        again = input("Do you want to play jumper? [y/n]: ")
        if again.lower() == 'y':
            self.play_again = True
        elif again.lower() == 'n':
            self.play_again = False
            print()
            print("Thank you for playing jumper! Have a nice day.")
            print()
            exit()
        else:
            again = (
                "That is not a valid input. Please enter 'y' for yes and 'n' for no")
