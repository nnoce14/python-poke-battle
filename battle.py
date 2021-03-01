import random, time, csv, keyboard

pokemans = []
moves = []
streak = 0
wins = 0


def main():
    print('\n\n|----- Main Menu -----|\n')
    print('Useful Info [0]')
    print('Random Pokemon Battle [1]')
    print('User-Selected Pokemon Battle [2]')
    print('Quit [3]')
    print('Current Win Streak: {}'.format(streak))
    print('Total Session Wins: {}'.format(wins))
    print("\n|---------------------|\n")

    num = int(input('Enter the number next to the option you want to select:\n'))

    if num == 0:
        # open secondary menu
        print('\n|----- Info Menu -----|\n')
        print('Lookup a Pokemon [1]')
        print('See All Pokemon [2]')
        print('Game Rules [3]')
        print('Go Back [4]')
        print("\n|---------------------|\n")

        num = int(input('\nEnter your choice\'s number:\n'))

        if num == 1:
            print('\n\nYou selected \'Lookup a Pokemon\'\n')

            poke = input('Enter a Pokemon\'s name to search for it: ')

            print('\n')
            for p in pokemans:
                if p.getName() == poke:
                    p.toString()

            print()
            main(0)

        elif num == 2:
            # outputs name of every pokemon in game in order
            print('\nYou selected \'See All Pokemon\'\n')
            for i in range(len(pokemans)):
                print("{}. {}".format(i + 1, pokemans[i].getName()))

            print()
            # wait function, requires user to press spacebar to continue and reloads main()
            wait_for_user()

        elif num == 3:
            # outputs program and game rules
            print("Game/Program Rules:")
            print("""\nThis program was designed to simulate a very basic Pokemon battle based off the popular Pokemon game series.
    In this simulation, the highest level evolution of each Pokemon from Generation One were put into the game, and each
    Pokemon's stats is pulled as is from their base stats found online, excluding HP which was scaled up dramatically to
    ensure battles were able to be sustained for multiple turns at a minimum. Correct typing modifiers have been included to provide
    realism and emulate the battle tactics of a real Pokemon battle. Status conditions have not been added to the game, so all moves
    are either physical or special attack moves from Gen 1, which I slightly adjusted power and accurayc stats for balancing as I saw fit.
                    
    All the user is required to do is enter the corresponding number based on the Movelist provided at the start of each turn. On screen instructions
    will guide the user through the simple menu system, and the program will run forever unless the user enters a 4 on the Main Menu. Any feedback for
    the game would be greatly appreciated, I had a lot of fun designing this simulator and I'm always looking to improve it. Enjoy.\n""")

            wait_for_user()
        # if user selects go back
        elif num == 4:
            # returns to main menu
            time.sleep(0.5)
            main()

    elif num == 1:
        # random pokemon battle
        print('\n\nYou selected \'Random Pokemon Battle\'\n')
        # select random pokemon
        p1 = get_random_pokemon()
        p2 = get_random_pokemon()

        # checks to ensure not the same pokemon generated
        while p1.getName() == p2.getName():
            p2 = get_random_pokemon()

        time.sleep(0.5)

        print("Your pokemon is {}. You are battling {}\n".format(p1.getName(), p2.getName()))
        # initiates player battle with 2 random pokemon
        player_battle(p1, p2)

    elif num == 2:
        # select pokemon for battle
        print('\nYou selected \'Pick your Pokemon\'\n')
        # get input for player's pokemon
        name = input('Enter a pokemon\'s name:\n')
        p1 = get_pokemon(name)  # name-specific pokemon return function
        p2 = get_random_pokemon()  # random cpu pokemon

        # checks to ensure not the same pokemon generated
        while p1.getName() == p2.getName():
            p2 = get_random_pokemon()

        time.sleep(0.5)

        # initiates player battle with selected poke and random poke
        print("Your pokemon is {}. You are battling {}\n".format(p1.getName(), p2.getName()))
        player_battle(p1, p2)

    elif num == 3:
        time.sleep(0.5)
        print('Exiting program...\n')
        quit()

def info_menu():
    print('\n|----- Info Menu -----|\n')
    print('Lookup a Pokemon [1]')
    print('See All Pokemon [2]')
    print('Game Rules [3]')
    print('Go Back [4]')
    print("\n|---------------------|\n")

    num = int(input('\nEnter your choice\'s number:\n'))

    if num == 1:
        print('\n\nYou selected \'Lookup a Pokemon\'\n')

        poke = input('Enter a Pokemon\'s name to search for it: ')

        print('\n')
        for p in pokemans:
            if p.getName() == poke:
                p.toString()

        print()
        wait_for_user()

    elif num == 2:
        # outputs name of every pokemon in game in order
        print('\nYou selected \'See All Pokemon\'\n')
        for i in range(len(pokemans)):
            print("{}. {}".format(i + 1, pokemans[i].getName()))

        print()
        # wait function, requires user to press spacebar to continue and reloads main()
        wait_for_user()

    elif num == 3:
        # outputs program and game rules
        print("Game/Program Rules:")
        print("""\nThis program was designed to simulate a very basic Pokemon battle based off the popular Pokemon game series.
In this simulation, the highest level evolution of each Pokemon from Generation One were put into the game, and each
Pokemon's stats is pulled as is from their base stats found online, excluding HP which was scaled up dramatically to
ensure battles were able to be sustained for multiple turns at a minimum. Correct typing modifiers have been included to provide
realism and emulate the battle tactics of a real Pokemon battle. Status conditions have not been added to the game, so all moves
are either physical or special attack moves from Gen 1, which I slightly adjusted power and accurayc stats for balancing as I saw fit.
                
All the user is required to do is enter the corresponding number based on the Movelist provided at the start of each turn. On screen instructions
will guide the user through the simple menu system, and the program will run forever unless the user enters a 4 on the Main Menu. Any feedback for
the game would be greatly appreciated, I had a lot of fun designing this simulator and I'm always looking to improve it. Enjoy.\n""")

        wait_for_user()

    elif num == 4:
        # returns to main menu
        time.sleep(0.5)
        main()


# function that generates all pokemon from csv file
def pokemon_init():
    with open("poke.csv", newline='') as csvfile:
        hp_modifier = 2  # determines how much health is given to pokemon at init, increase for longer battles
        poke_reader = csv.reader(csvfile, delimiter=',')
        for row in poke_reader:
            if row[-1] != '':  # passes over row containing column headers
                # assign_moves() returns array with move objects with names that match the four input strings
                m = assign_moves(row[8], row[9], row[10],
                                 row[11])  # pulls the 4 move names from last 4 items in row list
                poke = Pokemon(row[0], row[1],
                               [int(row[2]) * hp_modifier, int(row[3]), int(row[4]), int(row[5]), int(row[6]),
                                int(row[7])], m)
                # passes in poke name, type, [hp, attack, defense, sp attack, sp defense, speed], moveList
                pokemans.append(poke)


# function that generates all pokemon moves from csv file        
def moves_init():
    with open("move.csv", newline='') as csvfile:
        move_reader = csv.reader(csvfile, delimiter=',')
        for row in move_reader:
            if row[-1] != "MoveType":
                m = Move(row[0], row[1], row[2], row[3], row[4])
                moves.append(m)

# helper function to assign proper moves to each pokemon based on csv file input
def assign_moves(m1, m2, m3, m4):
    moveList = []
    for move in moves:
        if (move.getName() == m1 or move.getName() == m2 or move.getName() == m3 or move.getName() == m4) and (
                move not in moveList):
            moveList.append(move)

    return moveList

# ----- Pokemon Class Constructor ----- #
class Pokemon:
    def __init__(self, n, t, s, m):
        self.name = n
        self.type = t
        self.stats = s  # contains list with 6 stats
        self.fainted = False
        self.moveset = m  # contains a list with 4 Move objects

    # ---- Setter/Getter methods ----#
    def getName(self):
        return self.name

    def getType(self):
        return self.type

    def getHP(self):
        return int(self.stats[0])

    def getAttack(self):
        return int(self.stats[1])

    def getDefense(self):
        return int(self.stats[2])

    def getSpecialAttack(self):
        return int(self.stats[3])

    def getSpecialDefense(self):
        return int(self.stats[4])

    def getSpeed(self):
        return int(self.stats[5])

    def getMoves(self):
        return self.moveset

    def isFainted(self):
        return self.fainted

    def hasFainted(self):
        self.fainted = True

    def setHP(self, h):
        self.stats[0] = h

    def toString(self):
        print("Name: {}, Type: {}, Stats: {}\n".format(self.getName(), self.getType(), self.stats))
        for m in self.getMoves():
            print(" - ", end='')
            m.toString()
        print("\n")

    # ---- Battle methods ----#
    def fight(self, opponent, m, typeModifier):
        rand = random.randint(55, 100)  # lowest accuracy move is 70, this generates num between 55 and 100
        if rand > m.getAccuracy():  # determines if the move misses or not, higher accuracy has greater chance of being greater than the random number
            m.misses = True
            return 0
        else:
            # determine damage dealt
            damage = int((m.getPower() / (((random.random() * 2) + 2) * typeModifier)))
            # STAB modifier
            if m.getType() == self.getType():
                damage *= 1.5
            # determines move type (physical or special) and damages accordingly
            if m.getMoveType() == 'physical':
                if self.getAttack() > self.getSpecialAttack():
                    damage += (self.getAttack() - self.getSpecialAttack())
                damage -= (opponent.getDefense() / 6)
            else:
                if self.getSpecialAttack() > self.getAttack():
                    damage += (self.getSpecialAttack() - self.getAttack())
                damage -= (opponent.getSpecialDefense() / 6)
        return damage

    # returns random move from moveset
    def pickRandomMove(self):
        rand = random.randint(0, 3)  # returns 0, 1, 2, or 3
        return self.moveset[rand]  # returns move from moveset at random index


class Move:
    # constructor function
    def __init__(self, n, t, p, a, mt):
        self.name = n
        self.type = t
        self.power = int(p)
        self.accuracy = int(a)
        self.moveType = mt
        self.misses = False

    # ---- Setter/Getter methods ----#
    def getName(self):
        return self.name

    def getType(self):
        return self.type

    def getMoveType(self):
        return self.moveType

    def getPower(self):
        return self.power

    def getAccuracy(self):
        return self.accuracy

    def getMisses(self):
        return self.misses

    def resetMisses(self):
        self.misses = False

    # debug function
    def toString(self):
        print('Name: {}  Type: {}  Power: {}  Accuracy: {}  Move Type: {}'.format(self.getName(), self.getType(),
                                                                                  self.getPower(), self.getAccuracy(),
                                                                                  self.getMoveType()))


# returns random pokemon from list
def get_random_pokemon():
    rand = random.randint(0, (len(pokemans) - 1))
    return pokemans[rand]


# returns pokeman from list based on name input
def get_pokemon(name):
    for p in pokemans:
        if p.getName() == name:
            return p


# checks if hp is 0, then updates fainted variable
def check_condition(pokemon):
    if pokemon.getHP() <= 0:
        pokemon.hasFainted()


# battle game loop, takes both pokemon as input
def player_battle(p1, p2):
    while (not p1.isFainted()) and (not p2.isFainted()):
        print('\n//----- {}\'s Movelist -----//\n'.format(p1.getName()))
        p1_moveset = p1.getMoves()
        for i in range(len(p1_moveset)):
            print('{} [{}]'.format(p1_moveset[i].getName(), i + 1))

        try:
            selection = int(input('\nPick a move...\n')) - 1
            if 0 <= selection <= 3:
                p1_move = p1_moveset[selection]  # retrieves user's move choice
            else:
                raise ValueError
        except ValueError:
            print("Error. Please input value between 1 - 4 to pick move\n")
            selection = int(input()) - 1
            p1_move = p1_moveset[selection]

        p1_damage = p1.fight(p2, p1_move, typing_modifier(p1_move.getType().lower(),
                                                          p2.getType().lower()))  # gets damage based on fight method in Pokemon class

        p2_move = p2.pickRandomMove()
        p2_damage = p2.fight(p1, p2_move, typing_modifier(p2_move.getType().lower(), p1.getType().lower()))

        if True:
            # Player's pokemon goes first
            if p1_move.getMisses():
                print('{} used {}! {} missed!\n'.format(p1.getName(), p1_move.getName(), p1.getName()))
                p1_move.resetMisses()  # resets misses to false for next turn
            else:
                if (typing_modifier(p1_move.getType().lower(), p2.getType().lower()) == 1):
                    # crit hit (1 in 6 chance)
                    roll = random.randint(0, 5)
                    if roll == 5:
                        p1_damage *= 1.5
                        print("{} used {}! A critical hit! {} does {} damage!\n".format(p1.getName(), p1_move.getName(),
                                                                                        p1.getName(), int(p1_damage)))
                    else:
                        print("{} used {}! {} does {} damage!\n".format(p1.getName(), p1_move.getName(), p1.getName(),
                                                                        int(p1_damage)))
                elif (typing_modifier(p1_move.getType().lower(), p2.getType().lower()) == 0.5):
                    p1_damage *= 0.5
                    print("{} used {}! A critical hit! {} does {} damage! It wasn't very effective...\n".format(
                        p1.getName(), p1_move.getName(), p1.getName(), int(p1_damage)))
                elif (typing_modifier(p1_move.getType().lower(), p2.getType().lower()) == 2):
                    roll = random.randint(0, 5)
                    if roll == 5:
                        p1_damage *= 3
                        print("{} used {}! A critical hit! {} does {} damage! It was super effective!\n".format(
                            p1.getName(), p1_move.getName(), p1.getName(), int(p1_damage)))
                    else:
                        p1_damage *= 2
                        print("{} used {}! {} does {} damage! It was super effective!\n".format(p1.getName(),
                                                                                                p1_move.getName(),
                                                                                                p1.getName(),
                                                                                                int(p1_damage)))
                elif (typing_modifier(p1_move.getType().lower(), p2.getType().lower()) == 0):
                    p1_damage = 0
                    print("{} used {}! It doesn't affect {}...\n".format(p1.getName(), p1_move.getName(), p2.getName()))

            time.sleep(2)

            p2.setHP(p2.getHP() - int(p1_damage))
            check_condition(p2)
            if p2.isFainted():
                game_over(p1, p2, True)
                break
            else:
                print("{} has {} HP remaining!\n".format(p2.getName(), p2.getHP()))

            time.sleep(1.5)

            # CPU pokemon goes after

            if p2_move.getMisses():
                print('{} used {}! {} missed!\n'.format(p2.getName(), p2_move.getName(), p2.getName()))
            else:
                if (typing_modifier(p2_move.getType().lower(), p1.getType().lower()) == 1):
                    # crit hit (1 in 6 chance)
                    roll = random.randint(0, 5)
                    if roll == 5:
                        p2_damage *= 1.5
                        print("{} used {}! A critical hit! {} does {} damage!\n".format(p2.getName(), p2_move.getName(),
                                                                                        p2.getName(), int(p2_damage)))
                    else:
                        print("{} used {}! {} does {} damage!\n".format(p2.getName(), p2_move.getName(), p2.getName(),
                                                                        int(p2_damage)))
                elif (typing_modifier(p2_move.getType().lower(), p1.getType().lower()) == 0.5):
                    p2_damage *= 0.5
                    print("{} used {}! A critical hit! {} does {} damage! It wasn't very effective...\n".format(
                        p2.getName(), p2_move.getName(), p2.getName(), int(p2_damage)))
                elif (typing_modifier(p2_move.getType().lower(), p1.getType().lower()) == 2):
                    roll = random.randint(0, 5)
                    if roll == 5:
                        p2_damage *= 3
                        print("{} used {}! A critical hit! {} does {} damage! It was super effective!\n".format(
                            p2.getName(), p2_move.getName(), p2.getName(), int(p2_damage)))
                    else:
                        p2_damage *= 2
                        print("{} used {}! {} does {} damage! It was super effective!\n".format(p2.getName(),
                                                                                                p2_move.getName(),
                                                                                                p2.getName(),
                                                                                                int(p2_damage)))
                elif typing_modifier(p1_move.getType().lower(), p2.getType().lower()) == 0:
                    p2_damage = 0
                    print("{} used {}! It doesn't affect {}...\n".format(p2.getName(), p2_move.getName(), p1.getName()))

                time.sleep(2)

                p1.setHP(p1.getHP() - int(p2_damage))
                check_condition(p1)
                if p1.isFainted():
                    game_over(p2, p1)
                    break
                else:
                    print("{} has {} HP remaining!\n".format(p1.getName(), p1.getHP()))

                time.sleep(1.5)


def wait_for_user():
    time.sleep(1)
    print('Press the spacebar to continue...')
    keyboard.wait('spacebar')
    print('\n')
    info_menu()

def restart_game():
    time.sleep(1)
    print('Press the \'r\' key to restart...')
    keyboard.wait('r')
    print('\n')
    main()


# winner function
def game_over(winner, loser, inc=False):
    global wins, streak
    if inc:
        streak += 1
        wins += 1
    else:
        streak = 0
    print('\nGame over! {} has fainted... {} wins!'.format(loser.getName(), winner.getName()))
    time.sleep(1.5)
    restart_game()


# type comparison function (everything except fairy bc no fairy pokemon in gen 1)
def typing_modifier(typeA, typeB):
    if typeA == 'fire':
        if typeB == 'water' or typeB == 'dragon' or typeB == 'rock' or typeB == 'fire':
            return 0.5
        elif typeB == 'grass' or typeB == 'bug' or typeB == 'ice' or typeB == 'steel':
            return 2
        else:
            return 1
    elif typeA == 'water':
        if typeB == 'water' or typeB == 'dragon' or typeB == 'grass':
            return 0.5
        elif typeB == 'fire' or typeB == 'ground' or typeB == 'rock':
            return 2
        else:
            return 1
    elif typeA == 'grass':
        if typeB == 'bug' or typeB == 'dragon' or typeB == 'fire' or typeB == 'flying' or typeB == 'grass' or typeB == 'poison':
            return 0.5
        elif typeB == 'ground' or typeB == 'water' or typeB == 'rock':
            return 2
        else:
            return 1
    elif typeA == 'electric':
        if typeB == 'electric' or typeB == 'dragon' or typeB == 'grass':
            return 0.5
        elif typeB == 'flying' or typeB == 'water':
            return 2
        elif typeB == 'ground':
            return 0
        else:
            return 1
    elif typeA == 'flying':
        if typeB == 'electric' or typeB == 'rock' or typeB == 'steel':
            return 0.5
        elif typeB == 'bug' or typeB == 'fighting' or typeB == 'grass':
            return 2
        else:
            return 1
    elif typeA == 'rock':
        if typeB == 'fighting' or typeB == 'ground' or typeB == 'steel':
            return 0.5
        elif typeB == 'fire' or typeB == 'flying' or typeB == 'bug' or typeB == 'ice':
            return 2
        else:
            return 1
    elif typeA == 'ground':
        if typeB == 'bug' or typeB == 'grass':
            return 0.5
        elif typeB == 'fire' or typeB == 'electric' or typeB == 'poison' or typeB == 'rock' or typeB == 'steel':
            return 2
        elif typeB == 'flying':
            return 0
        else:
            return 1
    elif typeA == 'fighting':
        if typeB == 'normal' or typeB == 'dark' or typeB == 'ice' or typeB == 'rock' or typeB == 'steel':
            return 2
        elif typeB == 'bug' or typeB == 'flying' or typeB == 'poison' or typeB == 'psychic':
            return 0.5
        elif typeB == 'ghost':
            return 0
        else:
            return 1
    elif typeA == 'psychic':
        if typeB == 'psychic' or typeB == 'steel':
            return 0.5
        elif typeB == 'fighting' or typeB == 'poison':
            return 2
        elif typeB == 'dark':
            return 0
        else:
            return 1
    elif typeA == 'dark':
        if typeB == 'fighting' or typeB == 'dark':
            return 0.5
        elif typeB == 'ghost' or typeB == 'psychic':
            return 2
        else:
            return 1
    elif typeA == 'normal':
        if typeB == 'rock' or typeB == 'steel':
            return 0.5
        elif typeB == 'dark':
            return 0
        else:
            return 1
    elif typeA == 'ghost':
        if typeB == 'ghost' or typeB == 'psychic':
            return 2
        elif typeB == 'dark':
            return 0.5
        elif typeB == 'normal':
            return 0
        else:
            return 1
    elif typeA == 'poison':
        if typeB == 'poison' or typeB == 'ground' or typeB == 'rock' or typeB == 'ghost':
            return 0.5
        elif typeB == 'grass':
            return 2
        elif typeB == 'steel':
            return 0
        else:
            return 1
    elif typeA == 'dragon':
        if typeB == 'steel':
            return 0.5
        elif typeB == 'dragon':
            return 2
        else:
            return 1
    elif typeA == 'steel':
        if typeB == 'electric' or typeB == 'fire' or typeB == 'steel' or typeB == 'water':
            return 0.5
        elif typeB == 'rock' or typeB == 'ice':
            return 2
        else:
            return 1
    elif typeA == 'bug':
        if typeB == 'fighting' or typeB == 'steel' or typeB == 'fire' or typeB == 'flying' or typeB == 'ghost' or typeB == 'poison':
            return 0.5
        elif typeB == 'dark' or typeB == 'grass' or typeB == 'bug' or typeB == 'psychic':
            return 2
        else:
            return 1
    else:
        return 1


moves_init()
pokemon_init()
main()
