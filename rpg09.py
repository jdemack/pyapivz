#!/usr/bin/python3


def showInstructions():
    print('''
        RPG Game
        ========
        Commands:
            go [direction]
            get [item]
    ''')


def showStatus():
    #print the player's current status
    print('---------------------------')
    print(f'You are in the {currentRoom}.')
    #print teh current inventory
    print('Inventory: ' + str(inventory))

    if 'item' in rooms[currentRoom]:
        print(f"You see a {rooms[currentRoom]['item']}")
    print('---------------------------')

inventory = []

rooms = {
            'Hall': {
            'south' : 'Kitchen',
            'east': 'Dining Room',
            'item': 'skeletonkey'
                },
            'Kitchen': {
                'north' : 'Hall',
                'item': 'monster'
                },
            'Dining Room': {
                'west' : 'Hall',
                'south': 'Garden',
                'item': 'cookies'
                },
            'Garden': {
                'north': 'Dining Room'
                }
        }

currentRoom = 'Hall'

showInstructions()

while True:
    showStatus()
    move = ''
    while move == '':
        move = input('> ')

    move = move.lower().split()

    if move[0] == 'go':
        if move[1] in rooms[currentRoom]:
            currentRoom = rooms[currentRoom][move[1]]
        else:
            print('You cannot go that way!')


    if move[0] == 'get':
        if 'item' in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
            inventory += [move[1]]
            print(f'You just picked up {move[1]}!')
            del rooms[currentRoom]['item']
        else:
            print('Cannnot get ' + move[1] + '!')

    if 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item']:
        if 'cookies' in inventory:
            inventory.remove('cookies')
            del rooms[currentRoom]['item']
            print('cookie monster time')
        else:
            print("A monster has you! Game Over")
            break

    if currentRoom == 'Garden' and 'skeletonkey' in inventory:
        print("You win the game")



