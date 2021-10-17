import random
# from urllib.request import urlretrieve

'''
Holds the list of words and picks one at random for the code
'''

class Word_Bank:
    def __init__(self):
        self.rand_word = ""

    def get_random_word(self):
        words = ['amigo', 'sasquach', 'geronimo', 'butter']
        self.rand_word = words[random.randint(0, 3)]
        return self.rand_word


'''This code is for the extra

def __init__(self):
    self.url = 'https://www.mit.edu/~ecprice/wordlist.10000'

def urlretrieve(url, words):
    words = '''
