from game.board import Board
from game.console import Console
from game.move import Move
from game.player import Player
from game.random_num import Random_Num
from game.roster import Roster


class Director:
    def __init__(self):
        self._board = Board()
        self._number = Random_Num()
        self._console = Console()
        self._keep_playing = True
        self._move = Move()
        self._roster = Roster()
        self.name_list = []
        self.is_winner = False

        

    def start_game(self):
        self._prepare_game()
        while self._keep_playing:
            self._get_inputs()
            # self._do_updates()
            self._do_outputs()

    def _prepare_game(self):
        self.rand_num = self._number.generate_random_number()
        # self.rand_num_list = [int(x) for x in str(self.rand_num)]

        for n in range(2):
            name = self._console.read(f"Enter a name for player {n + 1}: ")
            self.name_list.append(name)
            player = Player(name)
            self._roster.add_player(player)

        self._board.print_line()
        for name in self.name_list:
            self._board.print_empty(name)
        self._board.print_line()

    def _get_inputs(self):

        player = self._roster.get_current()

        self._console.write(f"\n{player.get_name()}'s turn:")
        guess = self._console.read_number("What is your guess? ")
        
        guess = self._move.number_to_list(guess)
        
        if not isinstance(self.rand_num, list):
            self.rand_num = [int(x) for x in str(self.rand_num)]

        comparison = self._move.compare_guess(guess, self.rand_num)

        self._board.print_line()
        
        for name in self.name_list:
            self._board.print_screen(name, guess, comparison)
        self._board.print_line()

        if comparison == True:
            self.is_winner = True

    def _do_updates(self):
        """Updates the important game information for each round of play. In
        this case, that means updating the board with the current move.
        Args:
            self (Director): An instance of Director.
        """
        player = self._roster.get_current()
        move = player.get_move()
        self._board.apply(move)

    def _do_outputs(self):
        if self.is_winner:
            winner = self._roster.get_current()
            name = winner.get_name()
            print(f"\n{name} won!")
            self._keep_playing = False
        self._roster.next_player()
