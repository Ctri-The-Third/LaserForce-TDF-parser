

class teamEvent():
    """in a 2.003 TDF this is defined as a type ;2/team event"""
    def __init__(self,teamIndex,teamColourDesc):
        self.teamIndex = teamIndex
        self.teamColourDesc = teamColourDesc


class initialisationEvent():
    """in a 2.003 TDF, this is defined as a type ;3/entity-start event"""
    def __init__ (self,eventTimestamp,entityID,entityType,entitySoftName,entityTeam,entityHardName):
        self.timestamp = eventTimestamp
        self.entityID = entityID
        self.entityType = entityType #should be either "player" or "standard-target"
        self.entitySoftName = entitySoftName #player's gamertag or if null then hard-name
        self.entityHardName = entityHardName #player/base's battlesuit name, or base name 
    def getPlayerFromEvent():
        return #either None if not a player, or a player object

class gameEvent():
    """in a 2.003 TDF file this is defined as type ;4/event. It includes player tags, resupplies, achievements, and is of variable length"""
    def __init__(self, eventTimestamp, eventType, eventTypeText, subject=None,action=None,target=None):
        self.timestamp = eventTimestamp
        self.eventType = eventType
        self.eventTypeText = eventTypeText
        self.subject = subject #a player
        self.action = action #e.g. "earns an achievement" or "zaps" or "resupplies"

class scoreEvent():
    """in a 2.003 TDF, this is defined as a type ;5/entity-start event"""
    def __init__(self):

