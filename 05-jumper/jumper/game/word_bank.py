import random
# from urllib.request import urlretrieve

# to access this, just import and call Word_bank()


class Word_Bank:
    def __init__(self):
        self.rand_word = []


def word():
    Word_Bank.rand_words = ['amigo', 'sasquach', 'geronimo', 'butter']
    random_word = Word_Bank.rand_words[random.randint(0, 3)]
    return random_word


'''def __init__(self):
    self.url = 'https://www.mit.edu/~ecprice/wordlist.10000'

def urlretrieve(url, words):
    words = '''
