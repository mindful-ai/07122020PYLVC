import json
import random
import threading
import matplotlib.pyplot as plt

class jumblegame(object):

    nplayers = 0

    def __init__(self, name):
        self.name = name
        self.score = 0
        self.data = 0
        self.loadwords()
        jumblegame.nplayers += 1

    def __repr__(self):
        return "Jumble Game : {}".format(self.name)

    def loadwords(self):
        with open('words.json') as f:
            self.data = json.load(f)

    def jumble(self, word):
        L = list(word)
        random.shuffle(L)
        return ''.join(L)

    def run(self):
        
        for word in self.data:

            # Pick a word
            # Jumble the word
            self.jword = self.jumble(word)

            # Show the word
            print("The word is -------> ", self.jword)

            # Get the user input - attempt #1
            self.uword = input("[{}]? ".format(self.name))

            # if it failes - show clue 
            if(self.uword == word):
                self.score += 1
                continue
            else:
                print("Not correct")
                print("Clue -> ", self.data[word])
                # Get the user input - attempt #2
                self.uword = input("[{}]? ".format(self.name))
                # Compare
                if(self.uword == word):
                    # update score
                    self.score += 1
                else:
                    print("Not correct -> Moving on...")

    def results(self):
        print("-"*80)
        print(self.name, ' --> ', "SCORE :", self.score)

    def getscore(self):
        return self.score

# --------------------------------------------------------------------


if __name__ == "__main__":


    '''
    p1 = jumblegame("Purushotham")
    p2 = jumblegame("Raju")
    
    # https://realpython.com/intro-to-python-threading/
    px1 = threading.Thread(target=p1.run())
    px2 = threading.Thread(target=p2.run())


    px1.start()
    px1.join()

    px2.start()
    px2.join()

    p1.results()
    p2.results()
    '''

    names = ["Purushotham", "Rashmi", "Deepika", " Dilip", "Ramprasad"]

    players = []
    for name in names:
        players.append(jumblegame(name))

    print(players)

    threads = []
    for player in players:
        threads.append(threading.Thread(target=player.run()))

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    scores = []
    for player in players:
        scores.append(player.getscore())

    plt.bar(names, scores, color = 'r')
    plt.show()

