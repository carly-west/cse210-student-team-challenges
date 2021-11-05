from game.actor import Actor
from game.word import Word
from game.point import Point
import random


class Update():
    def __init__():

        pass

    def update_word_position(self):
        pass

    def remove_failed_words(self, word, list_words):
        failed_words = []
        for w in list_words:
            if w._position <= -1:
                failed_words.append(w)
        for words in failed_words:

            list_words.remove(words)

    def compare(self, rand_word, input_word):
        if rand_word in input_word:
            return []
