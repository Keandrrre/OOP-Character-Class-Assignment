# Task 1
class char_class():
    # Define Constructor
    def __init__(self, name, phrase1, phrase2):
        self.name = name
        self.phrase1 = phrase1
        self.phrase2 = phrase2
        self.level = 0

    # Functions/Methods
    def speak(self, phraseNum):
        if phraseNum == 1:
            print(self.phrase1)
        elif phraseNum == 2:
            print(self.phrase2)

    def setLevel(self, newLevel):
        self.level = newLevel
        print('Level: ' + str(newLevel))


# Task 2
char1 = char_class('Kung Fu Panda', 'Skadoosh.',
                   'You have been blinded by pure awesomeness!')
char2 = char_class('Spiderman', 'My Spider-Sense is tingling.',
                   'Your friendly neighbourhood spiderman.')

# Task 3
char2.speak(1)
char2.setLevel(2)
char1.speak(2)
