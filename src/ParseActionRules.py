#import cPickle as pickle
# Saving the CD dictionary in a pickle file
#pickle.dump(parseRules, open('parseRules.p', 'wb'))

class ParseRule:
    'Class for the Parsing Rules'
    
    def  __init__ (self, ruleName = None, relevantFields = None):
        self.ruleName = ruleName;
        self.relevantFields = relevantFields

    def getRuleName(self):
        return self.ruleName;
    
    def setRuleName(self,ruleName):
        self.ruleName = ruleName;
    
    def getRelevantFields(self):
        return self.relevantFields;
    
    def setRelevantFields(self,relevantFields):
        self.relevantFields = relevantFields
        
        
# Set of rules
ruleSet = []
ruleDict = {}

# Abstract Acts:
# ----------------

# ATRANS - abstract transfer; transfer of possession

aTransRelevantFields = ['object','from','to']
aTransRule = ParseRule('ATRANS', aTransRelevantFields)
ruleSet.append(aTransRule)
ruleDict[aTransRule.getRuleName()] = aTransRule

# Physical Acts:
# ----------------

# PTRANS - physical transfer; change of location
pTransRelevantFields = ['from','to']        
pTransRule = ParseRule('PTRANS',pTransRelevantFields) 
ruleSet.append(pTransRule)
ruleDict[pTransRule.getRuleName()] = pTransRule
     
# PROPEL - apply force to an object (but not necessarily set in motion)
propelRelevantFields = ['from','to']        
propelRule = ParseRule('PROPEL',propelRelevantFields) 
ruleSet.append(propelRule)
ruleDict[propelRule.getRuleName()] = propelRule
    
# INGEST - take an object inside the body
ingestRelevantFields = ['object']        
ingestRule = ParseRule('INGEST',ingestRelevantFields) 
ruleSet.append(ingestRule)
ruleDict[ingestRule.getRuleName()] = ingestRule
 
# Mental Acts:
# ----------------

# MTRANS - mental transfer of information
mTransRelevantFields = ['mObject','instr']        
mTransRule = ParseRule('MTRANS',mTransRelevantFields) 
ruleSet.append(mTransRule)
ruleDict[mTransRule.getRuleName()] = mTransRule

# MBUILD - construction of new information from old information
mBuildRelevantFields = ['mObject','instr']        
mBuildRule = ParseRule('MBUILD',mBuildRelevantFields) 
ruleSet.append(mBuildRule)
ruleDict[mBuildRule.getRuleName()] = mBuildRule

# Instrumental Acts:
# ----------------

# EXPEL - expulsion of object from the body
expelRelevantFields = ['object']        
expelRule = ParseRule('EXPEL',expelRelevantFields) 
ruleSet.append(expelRule)
ruleDict[expelRule.getRuleName()] = expelRule

# MOVEB - move body part
movebRelevantFields = ['object','from','to']        
movebRule = ParseRule('MOVEB',movebRelevantFields) 
ruleSet.append(movebRule)
ruleDict[movebRule.getRuleName()] = movebRule

# GRASP - grasp an object
graspRelevantFields = ['object','from']        
graspRule = ParseRule('GRASP',graspRelevantFields) 
ruleSet.append(graspRule)
ruleDict[graspRule.getRuleName()] = graspRule

# ATTEND - focus a sense organ
attendRelevantFields = ['object','to']        
attendRule = ParseRule('ATTEND',attendRelevantFields) 
ruleSet.append(attendRule)
ruleDict[attendRule.getRuleName()] = attendRule

# SPEAK - make noise
speakRelevantFields = ['object','to']        
speakRule = ParseRule('SPEAK',speakRelevantFields) 
ruleSet.append(speakRule)
ruleDict[speakRule.getRuleName()] = speakRule

# for item in ruleSet:
#     print item.getRuleName(), item.getRelevantFields()