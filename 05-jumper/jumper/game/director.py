from game.board import Board
from game.word_bank import Word_Bank
from game.welcome import Welcome


class Director:
    def __init__(self):
        self.welcome = Welcome()
        self.play_again = True
        self.board = Board()

    def start_game(self):
        isFirstGame = True
        if isFirstGame == False and self.play_again == True:
            self.get_inputs()
            self.board.put_user_guess()
        else:
            self.welcome.welcome_user()
            self.board.put_user_guess()

    def get_inputs(self):

        self.board.word_to_list()

        again = input("Do you want to play jumper? [y/n]: ")
        if again.lower() == 'y':
            self.play_again = True
        elif again.lower() == 'n':
            self.play_again = False
        else:
            again = (
                "That is not a valid input. Please enter 'y' for yes and 'n' for no")
