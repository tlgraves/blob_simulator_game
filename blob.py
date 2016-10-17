from random import randint, choice


egg_colors = ['light blue', 'speckled', 'pink polka-dotted', 'neon green']
blob_colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']

class Blob:
    def __init__(self):
        self.name = ''
        self.color = choice(blob_colors)
        self.egg_color = choice(egg_colors)
        self.num_eyes = randint(1, 3)
        self.size = 'small'
        self.age = -3
        self.happiness = 5
        self.hunger = 5
        self.health = 5
        self.traits = {'intelligence': randint(1,5),
                       'friendliness': randint(1,5),
                       'bravery': randint(1,5),
                       'perserverance': randint(1,5),
                       'creativity': randint(1,5)}
        self.inventory = {}

    def examine_blob(self):
        if self.age < 0:
           print('You are looking at a weird', self.egg_color, 'egg.')
           return
        else:
            print('This', self.color, 'blob is named', self.name + '.')
            if self.num_eyes == 1:
                eyes = 'eye.'
            else:
                eyes = 'eyes.'
            print('It is', self.size, 'and has', self.num_eyes, eyes)  

    def hatch(self):
        print('Your egg has hatched into an adorable...blob?')
        if self.num_eyes == 1:
            eyes = 'eye.'
        else:
            eyes = 'eyes.'
        print('It is', self.color, 'and has', self.num_eyes, eyes)
        print('It is gelatinous and slightly translucent. It jiggles.')
        self.name = input('Please enter a name for your blob: ').strip()
