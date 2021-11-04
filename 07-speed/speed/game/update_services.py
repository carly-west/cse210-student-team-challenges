from game.actor import Actor
from game.word import Word
from game.point import Point


class Update(Actor, Point):
    def __init__():

        pass

    def update_word_position(self, word, initial_position):

        word_move = initial_position - (2, 0)

        if word_move = (0, 200):



    def remove_failed_words(self, word, list_words):
        failed_words = []
        for w in list_words:
            if w._position <= -1:
                failed_words.append(w)
        for words in failed_words:
            # if words in failed_words == words in word_list:
            #     word_list.remove(words)
            list_words.remove(words)

        #if position is end_position remove from list
        #once loop is done remove the words on the failed_words from the word_list
        
        #list.append




