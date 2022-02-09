import random
# I always suggest using the full module like "from random import random"
#  even though you don't use the randint part,I saw that you specify the module
class Word:
    # this shows a random word, and the length of the random word
    def __init__(self):
        #Constructor
        self._list = ["cereal", "love", "life", "music", "massage", "television", "man", "computer", "singer", "school",
        "house", "piano", "dance", "sushi", "woman", "english", "dog", "cat", "plum", "clock", "phone", "orange",
        "activity", "feeling", "calendar", "price", "playstation", "spoon", "card", "car", "rock", "bass", "pants", "father",
        "guitar", "work", "toys", "website", "word", "parachute", "game", "charge", "funny", "learn", "education", "color","mother",
        "coding", "hangman", "romance", "blue", "book", "grass", "yard", "friend", "street", "brazil", "scissor", "number",]
        self._initial_word = random.choice(self._list)

    def _length(self):
        #this treats the random word as a list
        blank = []
        for i in range(len(self._initial_word)):
            blank.append(" _")
        return blank

    def _printlist(self, list):
        #this prints the length of the random word using dashes across the parachute
        printblank=""
        for i in list:
            printblank += i
        print(printblank)
        return printblank