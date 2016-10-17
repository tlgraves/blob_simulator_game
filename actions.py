from string import ascii_lowercase
import json
from person import Player
from blob import Blob

def game_over():
    print('The game is over, Goodbye!')
    raise SystemExit

def save_file(player):
    filename = 'save.txt'
    f = open(filename, 'w')
    json.dump(player.name, f)
    f.write('\n')
    json.dump(player.inventory, f)
    f.write('\n')
    json.dump(len(player.blobs), f)
    f.write('\n')
    for blob in player.blobs:
        blob_data = (blob.name, blob.color, blob.egg_color, blob.num_eyes, blob.size,
                     blob.age, blob.happiness, blob.hunger, blob.health,
                     blob.traits, blob.inventory)
        json.dump(blob_data, f)
        f.write('\n')
    f.close()

def load_save():
    filename = 'save.txt'
    f = open(filename, 'r')
    name = json.loads(f.readline().strip())
    player = Player(name)
    player.inventory = json.loads(f.readline())
    for i in range(json.loads(f.readline())):
        blob = Blob()
        data = json.loads(f.readline())
        blob.name, blob.color, blob.egg_color, blob.num_eyes, blob.size, \
        blob.age, blob.happiness, blob.hunger, blob.health, blob.traits, \
        blob.inventory = data
        player.blobs.append(blob)
    return player
            
def get_action(num_choices):
    #keeps asking for input until valid chioce
    #num_choices must be <= 26
    action = input('Enter letter: ').strip().lower()
    if action in ascii_lowercase[0:num_choices]:
        return action
    else:
        get_action(num_choices)

def start():
    print('You can:')
    print('A. Start new game')
    print('B. Load saved game')         
    action = get_action(2)
    return action
            
def new_game():
    name = input('Enter name: ')
    player = Player(name)
    first_blob = Blob()
    player.blobs.append(first_blob)
    print('Hello, ' + player.name + ', you found an egg!')
    return player, first_blob

def egg_actions(player, blob):
    while blob.age < 0:
        print('You can:')
        print('A. Look at egg')
        print('B. Pick up egg')
        print('C. Make an omelet')
        action = get_action(3)
        if action == 'a':
            blob.examine_blob()
            egg_actions
            blob.age += 1
        elif action == 'b':
           held_egg_actions(player, blob)
        elif action == 'c':
            print('Before you can crack the egg a Judgmental Field Biologist appears.\n \
He glares at you and takes the egg away. You are alone.')
            game_over()
    print('Your egg is hatching!')
    blob.hatch()

def held_egg_actions(player, blob):
    while blob.age < 0:
        blob.age += 1
        print('You can:')
        print('A. Talk to the egg')
        print('B. Sing to the egg')
        print('C. Cuddle the egg')
        print('D. Put the egg down')
        action = get_action(4)
        if action == 'a':
            print('Is it your imagination or did the egg make a noise?')
            blob.traits['intelligence'] += 2
            blob.traits['friendliness'] += 1
            blob.happiness += 1
        elif action == 'b':
            print('Is it your imagination or did the egg wobble?')
            blob.traits['creativity'] += 1
            blob.traits['intelligence'] += 1
            blob.happiness += 2
        elif action == 'c':
            print('The egg is pleasantly warm.')
            blob.traits['friendliness'] += 1
            blob.happiness += 3
        elif action == 'd':
            return
    print('You put the egg down.')
         
def main_game(player):
    for blob in player.blobs:
        blob.examine_blob()
