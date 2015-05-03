'''
CONCEPT LEVEL SENTIMENT ANALYZER

Created on 04/04/2015

@author: 
    Nihar Khetan <nkhetan@indiana.edu>, Ghanshyam Malu <gmalu@indiana.edu>, Varsha Suresh Kumar<vsureshk@indiana.edu>

Usage: 
    Execute the code using python 2.7

Description:   

    
Work Efforts          
-------------------------
Nihar Khetan: 

Ghanshyam Malu: 

Varsha Suresh Kumar:


Pre-requisite : 
----------------------

    Download and Install the NLKT tool for Python 
    Installation instructions can be found on : http://www.nltk.org/install.html

    Then, install the NLTK WordNet Corpora

    pythonShell>>> import 
    pythonShell>>> nltk.download()

    Download the WordNet Corpora from the NLTK Downloads Window

'''
# Load the CD dictionary back from the pickle file.
import cPickle as pickle
import CDs, ParseActionRules, SimilarityFinder
import operator
from string import lower
from nltk.corpus import wordnet as wn
from SimilarityFinder import SimilarityFinder

class ActionFrame:
    ActionFrameCounter = 0
    ' Class for an Action Frame'
    def __init__(self, actionType=None, actionActor=None, actionReqdField=None):
        ActionFrame.ActionFrameCounter += 1
        self.ActionFrameNum = ActionFrame.ActionFrameCounter
        self.actionType = actionType
        self.actionActor = actionActor
        # will be a dict type with correct object referenced
        self.actionReqdField = actionReqdField

    def getActionFrameNum(self):
        return self.ActionFrameNum
    
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
        ActionFrame.ActionFrameCounter -= 1
                                   
def createActionFrame(ruleDict, CD):
    ' Method to create an Action Frame based on a set of rules and parsing a CD'
    #cdQueue is a Queue which has a state of the form [[1,2,3],[1,2,3]]
    #1 can be empty or correspond to CD attributes eg: mObject
    #2 has to be a CD's Action Type (Like MTRANS, PTRANS)
    #3 has to be the CD's  description / content 
    cdQueue = []
    
    cdQueue.append(['',CD.keys()[0], CD[CD.keys()[0]]])
    ActionFrameBook = []
    while (cdQueue != []):
       
        CDtoExpand = cdQueue[0]
        del cdQueue[0]
        
        if CDtoExpand[0] != '':
                ActionFrameBook.append([CDtoExpand[0]])
        
        if ruleDict.has_key(CDtoExpand[1]):
            if len(ActionFrameBook) == 0:
                ActionFrameBook.append(CDtoExpand[1])
                ActionFrameBook.append('actor')
                ActionFrameBook.append(not_known_formatter(CDtoExpand[2]['actor']))
                
            elif isinstance(ActionFrameBook[len(ActionFrameBook)-1], list):
                ActionFrameBook[len(ActionFrameBook)-1].append(CDtoExpand[1])
                ActionFrameBook[len(ActionFrameBook)-1].append('actor')
                ActionFrameBook[len(ActionFrameBook)-1].append(not_known_formatter(CDtoExpand[2]['actor']))
            else:
                ActionFrameBook.append(CDtoExpand[1])
                ActionFrameBook.append('actor')
                ActionFrameBook.append(not_known_formatter(CDtoExpand[2]['actor']))

            for field in ruleDict[CDtoExpand[1]].getRelevantFields():
                if CDtoExpand[2].has_key(field):
                    if (isinstance(CDtoExpand[2][field], dict)):
                        cdQueue.append([field,CDtoExpand[2][field].keys()[0], CDtoExpand[2][field][CDtoExpand[2][field].keys()[0]]])
                    else:
                        if isinstance(ActionFrameBook[len(ActionFrameBook)-1], list):
                            ActionFrameBook[len(ActionFrameBook)-1].append(field)
                            ActionFrameBook[len(ActionFrameBook)-1].append(not_known_formatter(CDtoExpand[2][field]))
                        else:
                            ActionFrameBook.append(field)
                            ActionFrameBook.append(not_known_formatter(CDtoExpand[2][field]))
    
    return ActionFrameBook
    
def not_known_formatter(value):
    if value == '?':
        return "Not-Known"
    else:
        return value


def createSentenceForActionFrame(ActionFrameBook, sentence=''):
    ''' Creating a sentence for a given ActionFrame'''
    
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
    queue.append(ActionFrameBook)
    while (queue != []):
        toExpand = queue[0]
        toExpand = removeNotKnownElements(toExpand)
        del queue[0]
        for i in range(len(toExpand)):
            if (not isinstance(toExpand[i], list)):
                if (wordMap.has_key(toExpand[i])):
                    sentence += ' '+ wordMap[toExpand[i]]
                else:
                    sentence += ' '+ str(toExpand[i])
            else:
                queue.append(toExpand[i])

    return sentence           
  
  
def removeNotKnownElements(ActionFrame):
    ''' Remove the Not-Known elements to help creating a clear English sentence for a Action Frame
    Example :-
    Input  : ['MTRANS', 'actor', 'I', 'instr', 'Not-Known', ['mObject', 'ATTEND', 'actor', 'Not-Known', 'object', 'BOOK', 'to', 'Not-Known']]
    Output : ['MTRANS', 'actor', 'I', ['mObject', 'ATTEND', 'object', 'BOOK']] '''
    
    cleanActionFrame = []
    for item in ActionFrame:
        if (isinstance(item, list)):
            nestedScript = removeNotKnownElements(item)
            if nestedScript is not None:
                cleanActionFrame.append(nestedScript)       
        else:
            if (item == 'Not-Known'):
                cleanActionFrame.pop()
            else:
                cleanActionFrame.append(item)
            
    return cleanActionFrame


def is_mutual_exclusivity_top_activated(ActionFramesList):
    '''ActionFrame is a list of Action Frames'''
    flag = 1
    for eachActionFrame in ActionFramesList:
        for eachSubItem in eachActionFrame:
            if(isinstance(eachSubItem, list)):
                if ('mObject' in eachSubItem):
                    recommendScript = eachActionFrame
                    actorInRecommendScript = eachActionFrame[eachActionFrame.index('actor')+1]
                    recommededObject = eachSubItem[eachSubItem.index('object')+1]
                    flag = 0
                    break
                
    if flag == 1:
        return False
    
    #Finding objects over which recommendation happens
    objectList = []
    for eachActionFrame in ActionFramesList:
        if ('actor' in eachActionFrame):
            if(('mObject' in eachActionFrame) or ('object' in eachActionFrame)):
                if (actorInRecommendScript == eachActionFrame[eachActionFrame.index('actor')+1]):
                    if ('mObject' in eachActionFrame):
                        objectList.append(eachActionFrame[eachActionFrame.index('mObject')+1])
                    else:
                        objectList.append(eachActionFrame[eachActionFrame.index('object')+1])
    
    if recommendScript == None:
        return False
    else:
        return (recommededObject,objectList)
    

def processListAfterTopActivated(listToProcess):
    processedList = []
    descriptionDict = {}
    
    for eachItem in listToProcess:
        
        if isinstance(eachItem,list):
            newList = []
            
            for eachSubItem in eachItem:
                if '-' in eachSubItem:
                    newList.append(lower(eachSubItem.split('-')[0]))
                    descriptionDict[lower(eachSubItem.split('-')[0])] = eachSubItem.split('-')[1]
                
                #Now process it further to handle type two sentences where location of movie is mentioned
                #Additional check has to be done as key might already be preset in descriptionDict
                elif len(eachSubItem.split(" ")) > 1:
                    newList.append(lower(eachSubItem.split(" ")[0]))
                
                    if lower(eachSubItem.split(" ")[0]) in descriptionDict.keys():                        
                        descriptionDict[lower(eachSubItem.split(" ")[0])+'#'] = " ".join(eachSubItem.split(' ')[1:])
            
                else:
                    newList.append(lower(eachSubItem))
            processedList.append(newList)
        else:
            #print eachItem
            if '-' in eachItem:
                processedList.append(lower(eachItem.split('-')[0]))
                descriptionDict[lower(eachItem.split('-')[0])] = eachItem.split('-')[1]            
            
            #Now process it further to handle type two sentences where location of movie is mentioned
            elif len(eachItem.split(" ")) > 1:
                processedList.append(lower(eachItem.split(" ")[0]))
                descriptionDict[lower(eachItem.split(" ")[0])] = " ".join(eachItem.split(" ")[1:])

            else:
                processedList.append(lower(eachItem))   
    return (processedList,descriptionDict)  
    
                
def valueForKey(dict,key):
    try:
        value = dict[key]
        return value 
    except:
        return ""
   
def createActionFramesAndEnglishSentences(masterCD_List,ruleDict):
    ''' Create Action Frame and equivalent English Translation for each CD ''' 
    ActionFrameMasterList = [] 
    ActionFrameEnglishSentenceMasterList = []   

    ## Create Action Frame for each CD      
    for CD in masterCD_List:
        ActionFrame = createActionFrame(ruleDict, CD)
        ActionFrameMasterList.append(ActionFrame)    
        ActionFrame =  removeNotKnownElements(ActionFrame)
            
        ActionFrameSentence = createSentenceForActionFrame(ActionFrame)
        ActionFrameEnglishSentenceMasterList.append(ActionFrameSentence)


    return ActionFrameMasterList,ActionFrameEnglishSentenceMasterList

def printActionFramesAndEnglishTranslations(ActionFrameMasterList,ActionFrameEnglishSentenceMasterList):
    ''' Print Action Frames and Equivalent English Translation for each CD '''
    
    print
    print '-- +','-'*120, '+ --'
    print ' '*45, 'Action Frames and English Translations'
    print '-- +','-'*120, '+ --'
    print
    
    
    for i in range(len(ActionFrameMasterList)):  
        print
        print '\tAction Frame #        : ', i+1 
        print '\tAction Frame          : ', ActionFrameMasterList[i]                     
        print '\tAction Frame Sentence : ', ActionFrameEnglishSentenceMasterList[i] 
        print
        if (i != len(ActionFrameMasterList)-1):
            print '-'*130 
    print '-'*130
    print
    print


def printCDs(masterCD_List):
    '''Print CDs'''
    print
    print '-- +','-'*120, '+ --'
    print ' '*60, 'CDs'
    print '-- +','-'*120, '+ --'
    print
    i = 1 
    for CD in masterCD_List:
        print '     #',i, '\t', CD
        print
        i+=1
    print '-'*130
    print
    print

             
def findMutualExcluvityAndRecommendation(mutual_Exclusivity_TOP):
    ''' Find Mutual Exclusivity and Recommendation using the Python NLTK (Natural Language ToolKit) '''

    
    ActionFrameMasterList,ActionFrameEnglishSentenceMasterList  = createActionFramesAndEnglishSentences(masterCD_List,ruleDict)
    
    #print "Action Frame Master List"
    #print ActionFrameMasterList
    #print "Action Frame English Sentence Master list"
    #print ActionFrameEnglishSentenceMasterList
    #print "Mutual Exclusivity TOP"
    mutual_Exclusivity_TOP = is_mutual_exclusivity_top_activated(ActionFrameMasterList)
    #print mutual_Exclusivity_TOP
    
    if mutual_Exclusivity_TOP == False:
        print '-- +','-'*100, '+ --'            
        print ' '*20, 'NO RECOMMENDATION OF MUTUAL EXCLUSITY BETWEEN ITEMS FOUND IN SENTENCES'
        print '-- +','-'*100, '+ --'            
    else:
        ''' If this is a list that means the TOP got activated:
            The list can have two type of structures as per our CDS 
            1. ['item1',['item2-DESC']] DESC has to be a single word having delimiter other than '-'
            2. ['item1 at xyz1',['item1 at xyz2']] so in this case we are trying to find out the place xyz2 over xyz1'''
              
        #listToProcess= ['movie-SpiderMan',['book-Famous Five','popcorn']]
        #listToProcess1 = ['movie at amc',['movie at IMAX','popcorn']]
        processedList, descriptionDict = processListAfterTopActivated(mutual_Exclusivity_TOP)
        
        
        similarityFinder = SimilarityFinder(processedList)
        maxScoresDict = similarityFinder.findSimilarity()
        
        #print maxScoresDict

        print
        print '-- +','-'*120,'+ --'
        print ' '*40, 'Probable Recommendations Found' 
        print '-- +','-'*120, '+ --'
        print
        for key in maxScoresDict.keys():
            if str(maxScoresDict[key]) == '1.0':
                #That means that there are two items which are similar
                print ' '*25, "Preferred '" + key + " " + descriptionDict[key] + "' Over '" + key + " " + descriptionDict[key+'#'] +"'"            
               
            else:    
                print ' '*25,"'" + mutual_Exclusivity_TOP[0] + "' preferred over '" + key + (" " + valueForKey(descriptionDict, key)).rstrip() + "' with score %.2f" % maxScoresDict[key] + " out of 1.0"
            
        print
        print '-'*130 
        print 
        print
        print
        print '-- +','-'*120,'+ --'
        print ' '*40, 'Most Preferred' 
        print '-- +','-'*120, '+ --'
        print
    
    
        #some more explanations
        if len(maxScoresDict.keys()) > 1 and max(maxScoresDict.values()) != 1.0:
            print ' '*25, "'" +mutual_Exclusivity_TOP[0] + "' is being recommended as MOST LIKELIHOOD over '" + max(maxScoresDict.iteritems(), key=operator.itemgetter(1))[0] + \
            " " + valueForKey(descriptionDict, max(maxScoresDict.iteritems(), key=operator.itemgetter(1))[0]) +"'"
        elif max(maxScoresDict.values()) == 1.0:
            print ' '*25, "'" +mutual_Exclusivity_TOP[0] + "' is being recommended as MOST LIKELIHOOD over '" + \
            max(maxScoresDict.iteritems(), key=operator.itemgetter(1))[0] + \
            " " + descriptionDict[max(maxScoresDict.iteritems(), key=operator.itemgetter(1))[0]+'#'] + "'" 
        print
        print '-'*130
    
# Main()
if __name__ == "__main__":
    
    print
    print '-- +','-'*120,'+ --'
    print ' '*40, 'WELCOME TO CONCEPT LEVEL SENTIMENT ANALYZER' 
    print '-- +','-'*120, '+ --'
    print 
    print '-------------------------------------------'    
    print 'Choice 1 :: Sentence Set'
    print '-------------------------------------------'
    print '-I went to watch spider man at AMC.'
    print '-I loved the popcorn.'
    print '-I went with John and Mary.'
    print '-I will recommend to read the book'
    print ''
    print '-------------------------------------------'    
    print 'Choice 2 :: Sentence Set'
    print '-------------------------------------------'
    print '-I went to watch spider man at AMC.'
    print '-I loved the popcorn.'
    print '-I went with John and Mary.'
    print '-I will prefer to watch spider man at IMAX'
    print ''
    print '-------------------------------------------'    
    print 'Choice 3 :: Sentence Set'
    print '-------------------------------------------'
    print '-I went to watch spider man at AMC.'
    print '-I loved the popcorn.'
    print '-I went with John and Mary.'
    print '-I went to watch spider man at IMAX'
    print '-------------------------------------------'
    print ''
    
    # Accept the user's choice of Sentences Set
    option = input("Please enter the sentence you want to evaluate :: ")
    
    # Get the CD's for the Sentence Set selected from the CDs file
    masterCD_List = CDs.getMasterCDList(int(option))

    # Get the Rules Dictionary defined for each CD Action Type from the ParseActionRules file
    ruleDict = ParseActionRules.ruleDict
    
    # Print the list of all the CDs
    printCDs(masterCD_List)

    # Create Action Frame and English Translation for all the CDs    
    ActionFrameMasterList,ActionFrameEnglishSentenceMasterList  = createActionFramesAndEnglishSentences(masterCD_List,ruleDict)
    
    # Print Action Frame and English Translation for all the CDs    
    printActionFramesAndEnglishTranslations(ActionFrameMasterList,ActionFrameEnglishSentenceMasterList)
    
                       
    '''Now we should look for specific rules to activate the top which are
        mObject in list inside list
        same actor for both sentences
        if needed find similarity or dis similarity by using concept net '''
         
    # Find the Mutual Exclusivity TOP from the Action Frames
    mutual_Exclusivity_TOP = is_mutual_exclusivity_top_activated(ActionFrameMasterList)
    
    if (mutual_Exclusivity_TOP):
        print
        print '-- +','-'*120,'+ --'
        print ' '*40, 'Mutual Exclusivity TOP' 
        print '-- +','-'*120, '+ --'
        print
        print ' '*25, mutual_Exclusivity_TOP
        print
        print '-'*130
        print

    print

    # Find if any Recommendation has been done in the Sentence Set using the Natural Language ToolKit (NLTK) based on Python 
    findMutualExcluvityAndRecommendation(mutual_Exclusivity_TOP)
