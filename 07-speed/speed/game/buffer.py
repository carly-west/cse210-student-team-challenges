from game.actor import Actor

from game import constants
from game.point import Point

class Buffer(Actor):

    def __init__(self):
        super().__init__
        position = Point(0, constants.MAX_Y)
        self.set_position(position)
        self._update_word("")

    def compares(self, word):        

        return self._user_word == word

    def get_word(self):
        
        return self._user_word

    def clear_buffer(self):
        
        self._user_word = ""

    def add_character(self, char):
        self._update_word(self._user_word + char)

    def remove_character(self):
        self._update_word(self._user_word[:-1])

    def _update_word(self, new_word):
        self._user_word = new_word
        self.set_text(f"Buffer: {self._user_word}")