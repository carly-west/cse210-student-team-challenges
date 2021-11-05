from game.actor import Actor

from game import constants
from game.point import Point


class Buffer(Actor):

    def __init__(self):
        super().__init__
        position = Point(0, constants.MAX_Y)
        self.set_position(position)
        self._update_letter("")

    def compares(self, letter):

        return self._user_letter == letter

    def get_word(self):

        return self._user_letter

    def clear_buffer(self):

        self._user_letter = " "

    def _update_letter(self, new_letter):
        self._user_letter = new_letter
        self.set_text(f"Buffer: {self._user_letter}")
