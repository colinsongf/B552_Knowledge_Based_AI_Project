# import cPickle as pickle
# Saving the CD dictionary in a pickle file
# pickle.dump(parseRules, open('parseRules.p', 'wb'))

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
ruleDict = {}

# Abstract Acts:
# ----------------

# ATRANS - abstract transfer; transfer of possession
aTransRelevantFields = ['object','from','to']
aTransRule = ParseRule('ATRANS', aTransRelevantFields)
ruleDict[aTransRule.getRuleName()] = aTransRule

# Physical Acts:
# ----------------

# PTRANS - physical transfer; change of location
pTransRelevantFields = ['from','to']        
pTransRule = ParseRule('PTRANS',pTransRelevantFields) 
ruleDict[pTransRule.getRuleName()] = pTransRule
     
# PROPEL - apply force to an object (but not necessarily set in motion)
propelRelevantFields = ['from','to']        
propelRule = ParseRule('PROPEL',propelRelevantFields) 
ruleDict[propelRule.getRuleName()] = propelRule
    
# INGEST - take an object inside the body
ingestRelevantFields = ['object']        
ingestRule = ParseRule('INGEST',ingestRelevantFields) 
ruleDict[ingestRule.getRuleName()] = ingestRule
 
# Mental Acts:
# ----------------

# MTRANS - mental transfer of information
mTransRelevantFields = ['mObject','instr','state-change-before','state-change-after']                                
mTransRule = ParseRule('MTRANS',mTransRelevantFields) 
ruleDict[mTransRule.getRuleName()] = mTransRule

# MBUILD - construction of new information from old information
mBuildRelevantFields = ['mObject','instr']        
mBuildRule = ParseRule('MBUILD',mBuildRelevantFields) 
ruleDict[mBuildRule.getRuleName()] = mBuildRule

# Instrumental Acts:
# ----------------

# EXPEL - expulsion of object from the body
expelRelevantFields = ['object']        
expelRule = ParseRule('EXPEL',expelRelevantFields) 
ruleDict[expelRule.getRuleName()] = expelRule

# MOVEB - move body part
movebRelevantFields = ['object','from','to']        
movebRule = ParseRule('MOVEB',movebRelevantFields) 
ruleDict[movebRule.getRuleName()] = movebRule

# GRASP - grasp an object
graspRelevantFields = ['object','from']        
graspRule = ParseRule('GRASP',graspRelevantFields) 
ruleDict[graspRule.getRuleName()] = graspRule

# ATTEND - focus a sense organ
attendRelevantFields = ['object','to']        
attendRule = ParseRule('ATTEND',attendRelevantFields) 
ruleDict[attendRule.getRuleName()] = attendRule

# SPEAK - make noise
speakRelevantFields = ['object','to']        
speakRule = ParseRule('SPEAK',speakRelevantFields) 
ruleDict[speakRule.getRuleName()] = speakRule


''' Adding custom Actions '''
# SPEAK - make noise
LocationRelevantFields = ['place']        
locationRule = ParseRule('LOCATION',LocationRelevantFields) 
ruleDict[locationRule.getRuleName()] = locationRule