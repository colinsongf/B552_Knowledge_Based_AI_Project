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
        # will be a dict type with correct object referenced
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
            
'''
Unused Code        
def process (actionScriptParent, actionScriptChild):
    pass

def check_for_fields_key(CD, field):
    tempCD = CD
    while(True):
        for CDType,CDcontent in CD.iteritems():
            if CDType == field:
                pass
''' 
                       
def createActionScript(ruleDict, CD):
    ' Method to create an Action Script based on a set of rules and parsing a CD'
    #cdQueue is a Queue which has a state of the form [[1,2,3],[1,2,3]]
    #1 can be empty or correspond to CD attributes eg: mObject
    #2 has to be a CD's Action Type (Like MTRANS, PTRANS)
    #3 has to be the CD's  description / content 
    cdQueue = []
    
    cdQueue.append(['',CD.keys()[0], CD[CD.keys()[0]]])
    print "cdQueue : ",cdQueue
    actionScriptBook = []
    while (cdQueue != []):
       
        CDtoExpand = cdQueue[0]
        #print "g CDtoExpand: ",CDtoExpand
        del cdQueue[0]
        
        if CDtoExpand[0] != '':
                actionScriptBook.append([CDtoExpand[0]])
        
        if ruleDict.has_key(CDtoExpand[1]):
            if len(actionScriptBook) == 0:
                actionScriptBook.append(CDtoExpand[1])
                actionScriptBook.append('actor')
                actionScriptBook.append(not_known_formatter(CDtoExpand[2]['actor']))
                
            elif isinstance(actionScriptBook[len(actionScriptBook)-1], list):
                actionScriptBook[len(actionScriptBook)-1].append(CDtoExpand[1])
                actionScriptBook[len(actionScriptBook)-1].append('actor')
                actionScriptBook[len(actionScriptBook)-1].append(not_known_formatter(CDtoExpand[2]['actor']))
            else:
                actionScriptBook.append(CDtoExpand[1])
                actionScriptBook.append('actor')
                actionScriptBook.append(not_known_formatter(CDtoExpand[2]['actor']))
            
            #do something here
            #print "g relevant fields : ", ruleDict[CDtoExpand[1]].getRelevantFields()
            for field in ruleDict[CDtoExpand[1]].getRelevantFields():
                #print "\n"
                #print "g field: ", field
                #print "g CDtoExpand[2] :",CDtoExpand[2]
                #print "g cdQueue: ",cdQueue
                #print "g actionScriptBook: ",actionScriptBook
                if CDtoExpand[2].has_key(field):
                    if (isinstance(CDtoExpand[2][field], dict)):
                        
                        cdQueue.append([field,CDtoExpand[2][field].keys()[0], CDtoExpand[2][field][CDtoExpand[2][field].keys()[0]]])
                        #print "g new cdQueue: ",cdQueue 
                    else:
                        #print "what is here:", actionScriptBook[len(actionScriptBook)-1]
                        if isinstance(actionScriptBook[len(actionScriptBook)-1], list):
                            #print 'm hereeeee'
                            actionScriptBook[len(actionScriptBook)-1].append(field)
                            actionScriptBook[len(actionScriptBook)-1].append(not_known_formatter(CDtoExpand[2][field]))
                        else:
                            actionScriptBook.append(field)
                            actionScriptBook.append(not_known_formatter(CDtoExpand[2][field]))
    return actionScriptBook
    
    '''----------------------------------junk code after this i am not using it'''
'''
    
            #for CDType,CDcontent in CD.iteritems():
    
   
                        
    for CDType,CDcontent in CD.iteritems():
        #print CDType,CDcontent
        print "CD Type:" + str(CDType) + ":" + str(CDcontent)
        if ruleDict.has_key(CDType):
            
            actionScript = ActionScript();
            actionScript.setActionType(CDType)
            
            # Setting the actor 
           
            actionScript.setActionActor(not_known_formatter(CDcontent['actor']))
                                         
            
            actionScriptDict = {}
            print CDType + " rule is looking for fields : ",
            print ruleDict[CDType].getRelevantFields()
            
            #Forming the action sentence
            
            actionSentence += str(actionScript.getActionType()) + " by " + str(actionScript.getActionActor()) + " "
            allSubActionScripts.append(actionScript.getActionType())
            allSubActionScripts.append("actor")
            allSubActionScripts.append(actionScript.getActionActor())
            
            for field in ruleDict[CDType].getRelevantFields():
                print "Field: " + str(field) + " CDContent[Field] " +  str(CDcontent[field])
               
                if CDcontent.has_key(field):
                    actionScriptDict[field]=CDcontent[field]
                    
                    if (isinstance(CDcontent[field], dict)):
                        allSubActionScripts.append(field)
                        allSubActionScripts.append("###")
                        createActionScript(ruleDict, CDcontent[field], allSubActionScripts, actionSentence + get_type_of_field(field) + " ")
                        
                        
                        
                    else:
                        #setting the required Action Fields
                        allSubActionScripts.append(field)
                        allSubActionScripts.append(not_known_formatter(str(CDcontent[field])))                        
                        
                        actionSentence += str(field) + " " + not_known_formatter(str(CDcontent[field])) + " "
            
            
            #base case
                      
            if(not find_if_sub_cd_exists(ruleDict[CDType].getRelevantFields(), CDcontent, field)):
                    print "Final sentence before returning" 
                    print actionSentence
                    print "\nFinal all actionScipt before returning" 
                    print str(allSubActionScripts)
                    return allSubActionScripts
            
                              
            print "Actor: " + " ".join(actionScript.getActionActor())
            print "Task : " + actionScript.getActionType() +";\n",
            
            # forming a structure like ['MTRANS', []]
            allSubActionScripts.append(actionScript.getActionType())
            
            for k, v in actionScriptDict.iteritems():
                print k, value_list(v), ";",
                if (isinstance(v, dict)):
                    print '\n\n >>>'
                    print v
                    print 'in value dict'
                    createActionScript(ruleDict, v, allSubActionScripts)
                  #allSubActionScripts.append([k,value_list(v)])
                       
                     
          #print "Printing allSuvActionScripts"
          #print allSubActionScripts
     
     
     
def find_if_sub_cd_exists(fields, CDcontent, field):
    print "in sub cd loop"
    print "fields :", str(fields)
    print "CDcontent :", str(CDcontent)
    
    if (fields[len(fields)-1] != field ):
        return True
    for eachField in fields:
        if CDcontent.has_key(eachField):
            if (isinstance(CDcontent[eachField], dict)):
                
                return True
    return False                    
            
'''            
def not_known_formatter(value):
    if value == '?':
        return "Not Known"
    else:
        return value

# def value_list(x):
#     if isinstance(x, dict):
#         #return list(frozenset(x.values()))
#        
#         return x.values()
#     elif isinstance(x, basestring):
#         return [x]
#     else:
#         return None

def action_script_to_sentence(actionScriptBook, sentence=''):
    
    queue = []
    queue.append(actionScriptBook)
    #actionScriptSentence = '' 
    while (queue != []):
        toExpand = queue[0]
        del queue[0]
        for item in toExpand:
            if (not isinstance(item, list)):
                if (item == 'actor'):
                    sentence += ' by '
                elif (item == 'mObject'):
                    sentence += ' transferring mental information which is '
                elif (item == 'object'):
                    sentence += ' object is '
                elif (item == 'from'):
                    sentence += ' from '
                elif (item == 'to'):
                    sentence += ' to '
                elif (item == 'instr'):
                    sentence += ' using '
                elif (item == 'MTRANS'):
                    sentence += ' Mental Transfer of Information '
                else: 
                    sentence += item
            else:
                queue.append(item)
                
    return sentence

def is_mutual_exclusivity_top_activated(actionScripts):
    '''actionScript is a list of action scripts'''
    for eachActionScript in actionScripts:
        for eachSubItem in eachActionScript:
            if(isinstance(eachSubItem, list)):
                if ('mObject' in eachSubItem):
                    recommendScript = eachActionScript
                    actorInRecommendScript = eachActionScript[eachActionScript.index('actor')+1]
                    recommededObject = eachSubItem[eachSubItem.index('object')+1]
                    break
    
    
    #Finding objects over which recommendation happens
    objectList = []
    for eachActionScript in actionScripts:
        if ('actor' in eachActionScript):
            if(('mObject' in eachActionScript) or ('object' in eachActionScript)):
                print "in mObject or object"
                print actorInRecommendScript
                if (actorInRecommendScript == eachActionScript[eachActionScript.index('actor')+1]):
                    if ('mObject' in eachActionScript):
                        objectList.append(eachActionScript[eachActionScript.index('mObject')+1])
                    else:
                        objectList.append(eachActionScript[eachActionScript.index('object')+1])
    
    if recommendScript == None:
        return False
    else:
        return (recommededObject,objectList)
    #return actionScriptSentence
    



#CD_dict = pickle.load( open( "CDs.p", "rb" ) )
CD_dict = CDs.CD_dict
#ruleSet = ParseActionRules.ruleSet
ruleDict = ParseActionRules.ruleDict

#currentCD =  CD_dict[5]['CD4']
#currentCD =  CD_dict[1]['result'][0]['CD1']
currentCDLast =  CD_dict[4]['enable'][1]['CD7']
currentCDFirst =  CD_dict[2]['enable'][1]['CD3']


createACFirst = createActionScript(ruleDict, currentCDFirst)
createACLast = createActionScript(ruleDict, currentCDLast)



print "In Main"
print createACFirst
print createACLast


actionSentenceFirst = action_script_to_sentence(createACFirst)
actionSentenceLast = action_script_to_sentence(createACLast)
print 'Action sentence first: ', actionSentenceFirst
print 'Action sentence last: ', actionSentenceLast

'''Now we should look for specific rules to activate the top which are
        mObject in list inside list
        same actor for both sentences
        if needed find similarity or dis similarity by using concept net '''

print is_mutual_exclusivity_top_activated([createACFirst,createACLast])
#parseRules = pickle.load( open( "parseRules.p", "rb" ) )
 
#for k, v in CD_dict.iteritems():
#    print k, v
