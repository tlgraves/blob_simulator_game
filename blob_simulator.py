from actions import start, new_game, save_file, load_save, egg_actions, \
     main_game
          

print('~ Welcome to Blob Simulator ~')
#load_save()
action = start()
if action == 'b':
    filename = 'save.txt'
    try:
        player = load_save()
    except FileNotFoundError:
        print('No saved game. Starting new game.')
        action = a       
elif action == 'a':
    player, blob = new_game()
    save_file(player)
    egg_actions(player, blob)
    save_file(player)
main_game(player)

