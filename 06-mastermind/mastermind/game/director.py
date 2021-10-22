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
        

    def start_game(self):
        self._prepare_game()
        while self._keep_playing:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()
        
    def _prepare_game(self):
        for n in range(2):
            name = self._console.read(f"Enter a name for player {n + 1}: ")
            player = Player(name)
            self._roster.add_player(player)


    def _get_inputs(self):
        
        # display the game board
        board = self._board.to_string()
        self._console.write(board)
        # get next player's move
        player = self._roster.get_current()
        
        # self._console.write(f"{player.get_name()}'s turn:")
        # pile = self._console.read_number("What pile to remove from? ")
        # stones = self._console.read_number("How many stones to remove? ")
        # move = Move(stones, pile)
        player.set_move(move)

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
        if self._board.is_equal_to():
            winner = self._roster.get_current()
            name = winner.get_name()
            print(f"\n{name} won!")
            self._keep_playing = False
        self._roster.next_player()

        # rand_num = self._number.generate_random_number()
        # rand_string = self.move.number_to_list(self, rand_num)
        # print(rand_string)
