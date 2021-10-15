import random
# from urllib.request import urlretrieve

class Word_Bank:
    def __init__(self):
        self.rand_word = "this is not a word"

    def get_random_word(self):
        words = ['test', 'congeniality', 'computer', 'hippotamus', 'amigo']
        randint = random.randint(0,4)
        self.rand_word = words[randint]

def main():
    rando = Word_Bank()
    rando.get_random_word()

main()


'''def __init__(self):
    self.url = 'https://www.mit.edu/~ecprice/wordlist.10000'

def urlretrieve(url, words):
    words = '''