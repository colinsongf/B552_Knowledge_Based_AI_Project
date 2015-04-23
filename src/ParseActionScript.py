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
    actionScriptCounter = 0
    ' Class for an Action Script'
    def __init__(self, actionType=None, actionActor=None, actionReqdField=None):
        ActionScript.actionScriptCounter += 1
        self.actionScriptNum = ActionScript.actionScriptCounter
        self.actionType = actionType
        self.actionActor = actionActor
        self.actionReqdField = actionReqdField

    def getActionScriptNum(self):
        return self.actionScriptNum
    
    def getActionType(self):
        return self.actionType
    
    def getActionActor(self):
        return self.actionActor

    def getActionReqdField(self):
        return self.actionReqdField

    def setActionType(self,actionType):
        self.actionType = actionType
    
    def setActionActor(self, actionActor):
        self.actionActor = actionActor

    def setActionReqdField(self,actionReqdField):
        self.actionReqdField = actionReqdField
        
    def __del__(self):
        ActionScript.actionScriptCounter -= 1
            
        
def process (actionScriptParent, actionScriptChild):
    pass

def createActionScript(ruleDict, CD):
    ' Method to create an Action Script based on a set of rules and parsing a CD'
    
    for CDType,CDcontent in CD.iteritems():
        print CDType,CDcontent
        if ruleDict.has_key(CDType):
            
            actionScript = ActionScript();
            actionScript.setActionType(CDType)
            actionScript.setActionActor(CDcontent['actor'])
            actionScriptDict = {}
            #print CDType + " rule is looking for fields : ",
            #print ruleDict[CDType].getRelevantFields()
            for field in ruleDict[CDType].getRelevantFields():
                if CDcontent.has_key(field):
                    actionScriptDict[field]=CDcontent[field]
                              
            print "Actor: " + " ".join(actionScript.getActionActor())
            print "Task : " + actionScript.getActionType() +";",
            for k_actionScriptDict, v_actionScriptDict in actionScriptDict.iteritems():
                print k_actionScriptDict, 
                if isinstance(v_actionScriptDict, dict):
                    for k, v in v_actionScriptDict.iteritems():
                        if ruleDict.has_key(k):
                            #print "Found another CD"
                            print k, v 
                else:
                    print value_list(v_actionScriptDict), ";",
            print 


def value_list(x):
    if isinstance(x, dict):
        #return list(frozenset(x.values()))
        return x.keys(),x.values()
    elif isinstance(x, basestring):
        return x
    else:
        return None
    
# 5: {'CD4': {'MTRANS'    : {'actor' : 'I',
#                         'object' : 'popcorn',
#                         'love-state-before' : '?',
#                         'love-state-after' : '>8',
#                         }}}



#CD_dict = pickle.load( open( "CDs.p", "rb" ) )
CD_dict = CDs.CD_dict
ruleSet = ParseActionRules.ruleSet
ruleDict = ParseActionRules.ruleDict

#currentCD =  CD_dict[5]['CD4']
#currentCD =  CD_dict[1]['result'][0]['CD1']
#currentCD =  CD_dict[3]['result'][0]['CD5']
currentCD =  CD_dict[2]['enable'][1]['CD3']

createActionScript(ruleDict, currentCD)

#parseRules = pickle.load( open( "parseRules.p", "rb" ) )
 
#for k, v in CD_dict.iteritems():
#    print k, v

# for k, v in ruleDict.iteritems():
#     print k, v 