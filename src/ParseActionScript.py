# Load the CD dictionary back from the pickle file.
import cPickle as pickle
import CDs, ParseActionRules

'''
class Action Script:
    ActionScriptNum (integer)
    Action (String)
    ActionActor (String)

def process(Ac1,Ac2):
    on set of rules
    Ac1.setAction( Ac1.getAction() + Ac2.getAction()  [Merge meaningfully])
    return Ac1
    // Example Ac1.setAction ( MOBJ is ) + Ac2.getAction() (Attend to book)

def parseAscript(set of rules, firstCDInstance):
    //normal parsing
    if while parsing you incur another action script
        instantiate new ActionScript object say Ac2 (for seto of rules, fsecond CDInstance[like attend])
        Ac2 <-- parseAscript(set of rules, cd2)

        now we know that ac1 had a script ac2 embedded
        process(Ac1,Ac2)
return ActionScript object Ac1    
//writ
action.getActionScriptNumber() = 7
action.getAction() = MObject is Attend to Book
action.getActionActor() = i

'''

class ActionScript:
    
    def __init__(self, actionScriptNum, actionType, actionActor):
        self.actionScriptNum = actionScriptNum
        self.actionType = actionType
        self.actionActor = actionActor

    def getActionScriptNum(self):
        return self.actionScriptNum
    
    def getActionType(self):
        return self.actionType
    
    def getActionActor(self):
        return self.action


def process (actionScriptParent, actionScriptChild):
    pass

def parseScript(ruleSet, CD):
    pass

#CD_dict = pickle.load( open( "CDs.p", "rb" ) )
CD_dict = CDs.CD_dict

#parseRules = pickle.load( open( "parseRules.p", "rb" ) )

 
for k, v in CD_dict.iteritems():
    print k, v
    