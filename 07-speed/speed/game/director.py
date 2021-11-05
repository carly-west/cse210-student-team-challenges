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
        # self._food = Food()
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

        # self._score_board = ScoreBoard()
        # self._update = Update()
        # self._point = Point()
        self.points = 0
        self.y = random.randint(10, 380)

        # self._score_board = ScoreBoard()
        # self._snake = Snake()

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
            # self._get_inputs()
            self._do_updates()

            self._do_outputs()

        if self._input_service.window_should_close():
            self._keep_playing = False

        #     print("Game over!")

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
        # self._snake.move()
        # self._handle_body_collision()
        # self._handle_food_collision()
        self.position -= 2

        self._print_rand_word(self.rand_word, self.position)

        self._input_service.get_letter_pressed(
            self.letter_input_list)

        self.input_string = ''.join(self.letter_input_list)
        if self.rand_word in self.input_string:
            self.letter_input_list = []
         

    def _do_outputs(self):
        """Outputs the important game information for each round of play. In
        this case, that means checking if there are stones left and declaring
        the winner.

        Args:
            self (Director): An instance of Director.
        """
        self._output_service.clear_screen()
        # self._output_service.draw_actor(self._food)
        # self._output_service.draw_actors(self._snake.get_all())
        # self._output_service.draw_actor(self._score_board)
        self._output_service.flush_buffer()

        is_off_screen = self._word.is_off_screen(
            self.rand_word, self.position)
        if is_off_screen:
            self.points -= len(self.rand_word)
            is_off_screen = False
            self.position = 600
            self.rand_word = self._word.get_random_word(self)
            self.get_y = self._word.get_y(self)

        # HERE

    # def _handle_body_collision(self):
    #     """Handles collisions between the snake's head and body. Stops the game
    #     if there is one.

    #     Args:
    #         self (Director): An instance of Director.
    #     """
    #     head = self._snake.get_head()
    #     body = self._snake.get_collidable_segments()
    #     for segment in body:
    #         if head.get_position().equals(segment.get_position()):
    #             self._keep_playing = False
    #             break

    def _is_collision(self, first, second):
        x1 = first.get_position().get_x()
        y1 = first.get_position().get_y()
        width1 = first.get_width()
        height1 = first.get_height()

        rectangle1 = raylibpy.Rectangle(x1, y1, width1, height1)

        x2 = second.get_position().get_x()
        y2 = second.get_position().get_y()
        width2 = first.get_width()
        height2 = first.get_height()

        rectangle2 = raylibpy.Rectangle(x2, y2, width2, height2)

        return raylibpy.check_collision_recs(rectangle1, rectangle2)

    # def _handle_food_collision(self):
    #     """Handles collisions between the snake's head and the food. Grows the
    #     snake, updates the score and moves the food if there is one.

    #     Args:
    #         self (Director): An instance of Director.
    #     """
    #     head = self._snake.get_head()
    #     if self._is_collision(head, self._food):
    #         # get the amount the food is worth
    #         points = self._food.get_points()

    #         # grow the tail by that much
    #         self._snake.grow_tail(points)

    #         # add to the score
    #         self._score_board.add_points(points)

    #         # get a new food
    #         self._food.reset()

    def _print_rand_word(self, rand_word, position):

        # y_axis = self._random_number.random_number_yaxis()
        # font_size = self._random_number.random_number_size()

        # self._output_service.put_word(
        #     rand_word, random.randint(50, 350), random.randint(30, 100))

        # position = self._update.update_word_position(position)

        raylibpy.draw_text(rand_word, position, self.y, 30, raylibpy.BLACK)
        raylibpy.draw_text(f'SCORE: {self.points}', 10, 10, 30, raylibpy.BLACK)

        raylibpy.draw_text(f'GUESS: {self.input_string}',
                           10, 370, 20, raylibpy.BLACK)
