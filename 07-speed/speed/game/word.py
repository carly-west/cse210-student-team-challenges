'''
Generates random word and moves it across the screen
'''

import random


class Word:
    def __init__(self):
        self.rand_word = ""

    def get_random_word(self):
        words = ['amigo', 'sasquach', 'geronimo', 'butter']
        self.rand_word = words[random.randint(0, 3)]
        return self.rand_word

    def is_off_screen(self, position):
        if position >= 600:
            return True
