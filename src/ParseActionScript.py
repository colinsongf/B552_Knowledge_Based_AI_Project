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
#     print "cdQueue : ",cdQueue
    actionScriptBook = []
    while (cdQueue != []):
       
        CDtoExpand = cdQueue[0]
#         print "\nBeginning iteration in while loop"
#         print "g CDtoExpand: ",CDtoExpand
        del cdQueue[0]
        
        if CDtoExpand[0] != '':
#                 print "g CDtoExpand[0]: '",CDtoExpand[0],"' is not '', appending to actionScriptBook"
                actionScriptBook.append([CDtoExpand[0]])
#                 print "g actionScriptBook : ", actionScriptBook
        
        if ruleDict.has_key(CDtoExpand[1]):
#             print "g actionScriptBook: ",actionScriptBook
            if len(actionScriptBook) == 0:
#                 print "g len(actionScriptBook) = 0, appending to it"
                actionScriptBook.append(CDtoExpand[1])
                actionScriptBook.append('actor')
                actionScriptBook.append(not_known_formatter(CDtoExpand[2]['actor']))
#                 print "g actionScriptBook: ",actionScriptBook
                
            elif isinstance(actionScriptBook[len(actionScriptBook)-1], list):
#                 print "g actionScriptBook[len(actionScriptBook)-1] is a LIST, appending to it"
                actionScriptBook[len(actionScriptBook)-1].append(CDtoExpand[1])
                actionScriptBook[len(actionScriptBook)-1].append('actor')
                actionScriptBook[len(actionScriptBook)-1].append(not_known_formatter(CDtoExpand[2]['actor']))
#                 print "g actionScriptBook: ",actionScriptBook
            else:
#                 print "g appending to actionScriptBook"
                actionScriptBook.append(CDtoExpand[1])
                actionScriptBook.append('actor')
                actionScriptBook.append(not_known_formatter(CDtoExpand[2]['actor']))
#                 print "g actionScriptBook: ",actionScriptBook
            
            #do something here
#             print "\ng relevant fields for '",CDtoExpand[1],"' are : ", ruleDict[CDtoExpand[1]].getRelevantFields()
#             print "g entering For loop for relevant fields"
            for field in ruleDict[CDtoExpand[1]].getRelevantFields():
#                 print "\n"
#                 print "g field: ", field
#                 print "g CDtoExpand[2] :",CDtoExpand[2]
#                 print "g cdQueue: ",cdQueue
#                 print "g actionScriptBook: ",actionScriptBook
                if CDtoExpand[2].has_key(field):
                    if (isinstance(CDtoExpand[2][field], dict)):
#                         print "g CDtoExpand[2][field] is a DICT, appending to cdQueue"
                        cdQueue.append([field,CDtoExpand[2][field].keys()[0], CDtoExpand[2][field][CDtoExpand[2][field].keys()[0]]])
#                         print "g new cdQueue: ",cdQueue 
                    else:
                        #print "what is here:", actionScriptBook[len(actionScriptBook)-1]
                        if isinstance(actionScriptBook[len(actionScriptBook)-1], list):
                            #print 'm hereeeee'
#                             print "g actionScriptBook[len(actionScriptBook)-1] is a LIST, appending to actionScriptBook"
                            actionScriptBook[len(actionScriptBook)-1].append(field)
                            actionScriptBook[len(actionScriptBook)-1].append(not_known_formatter(CDtoExpand[2][field]))
#                             print "g actionScriptBook: ", actionScriptBook
                        else:
#                             print "g actionScriptBook[len(actionScriptBook)-1] is NOT A LIST, appending to actionScriptBook"
                            actionScriptBook.append(field)
                            actionScriptBook.append(not_known_formatter(CDtoExpand[2][field]))
#                             print "g actionScriptBook: ", actionScriptBook
    
#     print "g returning actionScriptBook :", actionScriptBook
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
        return "Not-Known"
    else:
        return value


def createSentenceForActionScript(actionScriptBook, sentence=''):
    ''' Creating a sentence for a given ActionScript'''
    
    '''
    Abstract Acts:
        ATRANS - abstract transfer; transfer of possession

    Physical Acts:
        PTRANS - physical transfer; change of location
        PROPEL - apply force to an object (but not necessarily set in motion)
        INGEST - take an object inside the body

    Mental Acts:
        MTRANS - mental transfer of information
        MBUILD - construction of new information from old information
    
    Instrumental Acts:    
        EXPEL - expulsion of object from the body
        MOVEB - move body part
        GRASP - grasp an object
        ATTEND - focus a sense organ
        SPEAK - make noise
    '''
    
    wordMap = {
                'ATRANS': 'Abstract-Transfer-of-Possession',
            
                'PTRANS' : 'Physical-Transfer-of-Location',
                'PROPEL' : 'Apply-Force',
                'INGEST' : 'Consume',

                'MTRANS' : 'Transfer-of-Information',
                'MBUILD' : 'Generate-New-Information',

                'EXPEL' : 'Expel',
                'MOVEB' : 'Move-Body-Part',
                'GRASP' : 'grasp',
                'ATTEND': 'focus',
                'SPEAK' : 'speak',                  
                
                'LOCATION'  : 'Current-location',
                'place'     : 'present-at',
                'actor'     : 'by',
                'object'    : 'of',
                'mObject'   : 'of',
                'instr'     : 'with-the-help-of',
                'I'         : 'I'                
              }
    
    queue = []
    queue.append(actionScriptBook)
#     print '-'*80
#     print "g Creating a sentence for ", actionScriptBook
    #actionScriptSentence = '' 
    while (queue != []):
        toExpand = queue[0]
        toExpand = removeNotKnownElements(toExpand)
        del queue[0]
        for i in range(len(toExpand)):
            if (not isinstance(toExpand[i], list)):
                #print toExpand[i], ":", 
                if (wordMap.has_key(toExpand[i])):
                 #   print wordMap[toExpand[i]]
                    sentence += ' '+ wordMap[toExpand[i]]
                else:
#                     print 
                    sentence += ' '+ str(toExpand[i])
            else:
                queue.append(toExpand[i])

    return sentence           
  
  
def removeNotKnownElements(actionScript):
    ''' Remove the Not-Known elements to help creating a clear English sentence for a action script
    Example :-
    Input  : ['MTRANS', 'actor', 'I', 'instr', 'Not-Known', ['mObject', 'ATTEND', 'actor', 'Not-Known', 'object', 'BOOK', 'to', 'Not-Known']]
    Output : ['MTRANS', 'actor', 'I', ['mObject', 'ATTEND', 'object', 'BOOK']] '''
    
    cleanActionScript = []
    for item in actionScript:
        if (isinstance(item, list)):
            nestedScript = removeNotKnownElements(item)
            if nestedScript is not None:
                cleanActionScript.append(nestedScript)       
        else:
            if (item == 'Not-Known'):
                cleanActionScript.pop()
            else:
                cleanActionScript.append(item)
            
    return cleanActionScript
    
      
def action_script_to_sentence(actionScriptBook, sentence=''):
    ''' Creating a sentence for a given ActionScript'''
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

def is_mutual_exclusivity_top_activated(actionScriptsList):
    '''actionScript is a list of action scripts'''
    for eachActionScript in actionScriptsList:
#        print 'g eachActionScript', eachActionScript
        for eachSubItem in eachActionScript:
#            print 'g eachSubItem', eachSubItem
            if(isinstance(eachSubItem, list)):
                if ('mObject' in eachSubItem):
#                    print 'g mObject found, finding recommendation stuff'
                    recommendScript = eachActionScript
                    actorInRecommendScript = eachActionScript[eachActionScript.index('actor')+1]
                    recommededObject = eachSubItem[eachSubItem.index('object')+1]
#                    print 'g recommendScript: ', recommendScript
#                    print 'g actorInRecommendScript', actorInRecommendScript
#                    print 'g recommededObject', recommededObject
                    break
    
    
    #Finding objects over which recommendation happens
#    print '\ng Finding objects over which recommendation happens'
    objectList = []
    for eachActionScript in actionScriptsList:
#        print 'g eachActionScript', eachActionScript
        if ('actor' in eachActionScript):
#            print 'g actor found'
            if(('mObject' in eachActionScript) or ('object' in eachActionScript)):
#                 print "g in mObject or object"
#                 print "g actorInRecommendScript", actorInRecommendScript
                if (actorInRecommendScript == eachActionScript[eachActionScript.index('actor')+1]):
#                     print 'g Actor in recommend script and eachActionScript are same'
                    if ('mObject' in eachActionScript):
                        objectList.append(eachActionScript[eachActionScript.index('mObject')+1])
                    else:
                        objectList.append(eachActionScript[eachActionScript.index('object')+1])
#                     print 'g updated objectList: ', objectList
    if recommendScript == None:
        return False
    else:
        return (recommededObject,objectList)
    #return actionScriptSentence
    

def old_main_function_only_for_testing_delete_it():
    #CD_dict = pickle.load( open( "CDs.p", "rb" ) )
    # CD_dict = CDs.CD_dict
    
    masterCD_List = CDs.masterCD_List
    ruleDict = ParseActionRules.ruleDict
    
    # currentCDFirst =  CD_dict['2']['enable'][1]['CD3']
    # currentCDLast =  CD_dict['4']['enable'][1]['CD7']
    
    currentCDFirst =  masterCD_List[4]
    currentCDLast =  masterCD_List[6]
    
    
    print "Creating action script for :", currentCDFirst
    createACFirst = createActionScript(ruleDict, currentCDFirst)
    print '-'*60
    print "g currentCDFirst : ", currentCDFirst
    print "g createACFirst : ", createACFirst
    print '-'*60
    print
    
    print "Creating action script for :", currentCDLast
    createACLast = createActionScript(ruleDict, currentCDLast)
    print '-'*60
    print "g currentCDLast : ", currentCDLast
    print "g createACLast : ", createACLast
    print '-'*60
    
    
    print "In Main"
    print createACFirst
    print createACLast
    
    
    cleanedActionScript_1 =  removeNotKnownElements(createACFirst)
    
    actionSentenceFirst = action_script_to_sentence(createACFirst)
    actionSentenceFirstNew = createSentenceForActionScript(cleanedActionScript_1)
    
    cleanedActionScript_2 =  removeNotKnownElements(createACLast)
    
    actionSentenceLast = action_script_to_sentence(createACLast)
    actionSentenceLastNew = createSentenceForActionScript(cleanedActionScript_2)
    
    print 'Action sentence first  : ', actionSentenceFirst
    #print 'actionSentenceFirstNew : ', actionSentenceFirstNew
    
    #print createACLast
    print 'Action sentence last      : ', actionSentenceLast
    # print 'Action sentence last New  : ', actionSentenceLastNew
    
    '''Now we should look for specific rules to activate the top which are
            mObject in list inside list
            same actor for both sentences
            if needed find similarity or dis similarity by using concept net '''
    
    #print is_mutual_exclusivity_top_activated([createACFirst,createACLast])
    #parseRules = pickle.load( open( "parseRules.p", "rb" ) )
     
    
def createActionScriptsAndEnglishSentences(masterCD_List,ruleDict):
    ''' Create Action Script and equivalent English Translation for each CD ''' 
    actionScriptMasterList = [] 
    actionScriptEnglishSentenceMasterList = []   

    ## Create Action Script for each CD      
    for CD in masterCD_List:
        actionScript = createActionScript(ruleDict, CD)
        actionScriptMasterList.append(actionScript)    
        actionScript =  removeNotKnownElements(actionScript)
            
        actionScriptSentence = createSentenceForActionScript(actionScript)
        actionScriptEnglishSentenceMasterList.append(actionScriptSentence)

    ## Create Equivalent English Translation for each CD '''
    for i in range(len(actionScriptMasterList)): 
        print '-'*60   
        print
        print 'Action Script #        : ', i+1 
        print 'Action Script          : ', actionScriptMasterList[i]                     
        print 'Action Script Sentence : ', actionScriptEnglishSentenceMasterList[i] 
        print

    return actionScriptMasterList,actionScriptEnglishSentenceMasterList


masterCD_List = CDs.masterCD_List
ruleDict = ParseActionRules.ruleDict

i = 0
for CD in masterCD_List:
    print i, CD
    i+=1

actionScriptMasterList,actionScriptEnglishSentenceMasterList  = createActionScriptsAndEnglishSentences(masterCD_List,ruleDict)

print is_mutual_exclusivity_top_activated(actionScriptMasterList)