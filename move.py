class Move:
    # constructor function
    def __init__(self, n, t, p, a, mt):
        self.name = n
        self.type = t
        self.power = p
        self.accuracy = a
        self.moveType = mt
        self.misses = False
        
    #---- Setter/Getter methods ----#
    def getName(self):
        return name
    
    def getType(self):
        return type
    
    def getMoveType(self):
        return moveType
    
    def getPower(self):
        return power
    
    def getAccuracy(self):
        return accuracy
    
    def getMisses(self):
        return misses
