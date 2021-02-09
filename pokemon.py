import random

class Pokemon:
    #---- Pokemon ----#
    def __init__(self, n, t, s, m):
        self.name = n
        self.type = t
        self.stats = s
        self.fainted = False
        moveset = m
    
    #---- Setter/Getter methods ----#
    def getName(self):
        return self.name

    def getType(self):
        return self.type
    
    def getHP(self):
        return stats[0]

    def getAttack(self):
        return stats[1]

    def getDefense(self):
        return stats[2]
    
    def getSpecialAttack(self):
        return stats[3]
    
    def getSpecialDefense(self):
        return stats[4]
    
    def getSpeed(self):
        return stats[5]
    
    def isFainted(self):
        return fainted
    
    def hasFainted(self):
        fainted = True
        
    def setHP(self, h):
        stats[0] = h
        
    #---- Battle methods ----#
    def fight(self, opponent, move, typeModifier):
        random = random.randint(1, 100)
        if random > m.getAccuracy():
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
                    damage -= (opponent.getDefense() / 4)
            else:
                if self.getAttack() < self.getSpecialAttack():
                    damage += (self.getSpecialAttack() - self.getAttack())
                    damage -= (opponent.getSpecialDefense() / 4)
        return damage
    
    def pickRandomMove():
        moveNum = math.randint(3)
        return moveset[moveNum]
    
        
                    
                                           
                                           