from time import sleep

import random

import raylibpy
from game import constants
from game.word import Word
from game.random_number import Random_Number
from game.update_services import Update
from game.point import Point
from game.score_board import ScoreBoard

# from game.food import Food
# from game.score_board import ScoreBoard
# from game.snake import Snake


class Director:
    """A code template for a person who directs the game. The responsibility of
    this class of objects is to control the sequence of play.

    Stereotype:
        Controller

    Attributes:
        food (Food): The snake's target.
        input_service (InputService): The input mechanism.
        keep_playing (boolean): Whether or not the game can continue.
        output_service (OutputService): The output mechanism.
        score (Score): The current score.
        snake (Snake): The player or snake.
    """

    def __init__(self, input_service, output_service):
        """The class constructor.

        Args:
            self (Director): an instance of Director.
        """
        self._input_service = input_service
        self._keep_playing = True
        self._output_service = output_service
        self._word = Word
        self._random_number = Random_Number
        self.position = 600
        self.rand_word = ''
        self.letter_input_list = []
        self.input_string = ''
        self._update_services = Update
        self.get_y = 0
        self.points = 0
        self.y = random.randint(10, 380)

    def start_game(self):
        """Starts the game loop to control the sequence of play.

        Args:
            self (Director): an instance of Director.
        """
        print("Starting game...")
        self.get_y = self._word.get_y(self)
        self.rand_word = self._word.get_random_word(self)
        self._output_service.open_window("Speed")

        while self._keep_playing:
            self._do_updates()
            self._do_outputs()

        if self._input_service.window_should_close():
            self._keep_playing = False

    def _get_inputs(self):
        """Gets the inputs at the beginning of each round of play. In this case,
        that means getting the desired direction and moving the snake.

        Args:
            self (Director): An instance of Director.
        """
        direction = self._input_service.get_direction()
        self._snake.turn_head(direction)

    def _do_updates(self):
        """Updates the important game information for each round of play. In
        this case, that means checking for a collision and updating the score.

        Args:
            self (Director): An instance of Director.
        """
        self.position -= 2

        self._print_rand_word(self.rand_word, self.position)

        self._input_service.get_letter_pressed(
            self.letter_input_list)

        self.input_string = ''.join(self.letter_input_list)
        if self.rand_word in self.input_string:
            self.points += len(self.rand_word)
            self.letter_input_list = []
            self.rand_word = ''

    def _do_outputs(self):
        """Outputs the important game information for each round of play. In
        this case, that means checking if there are stones left and declaring
        the winner.

        Args:
            self (Director): An instance of Director.
        """
        self._output_service.clear_screen()
        self._output_service.flush_buffer()

        is_off_screen = self._word.is_off_screen(
            self.rand_word, self.position)
        if is_off_screen:
            self.points -= len(self.rand_word)
            is_off_screen = False
            self.position = 600
            self.rand_word = self._word.get_random_word(self)
            self.get_y = self._word.get_y(self)

    def _print_rand_word(self, rand_word, position):

        raylibpy.draw_text(rand_word, position, self.y, 30, raylibpy.BLACK)
        raylibpy.draw_text(f'SCORE: {self.points}', 10, 10, 30, raylibpy.BLACK)

        raylibpy.draw_text(f'GUESS: {self.input_string}',
                           10, 370, 20, raylibpy.BLACK)
