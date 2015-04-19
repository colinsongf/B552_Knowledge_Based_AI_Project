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
        
        
 
# Abstract Acts:
# ----------------

# ATRANS - abstract transfer; transfer of possession

aTransRelevantFields = []
aTransRule = ParseRule('ATRANS', aTransRelevantFields)

# Physical Acts:
# ----------------

# PTRANS - physical transfer; change of location
pTransRelevantFields = ['from','to']        
pTransRule = ParseRule('PTRANS',pTransRelevantFields) 
     
# ROPEL - apply force to an object (but not necessarily set in motion)
propelRelevantFields = ['from','to']        
propelRule = ParseRule('PROPEL',propelRelevantFields) 
 
    
# INGEST - take an object inside the body
ingestRelevantFields = ['object']        
ingestRule = ParseRule('INGEST',ingestRelevantFields) 
 
# Mental Acts:
# ----------------

# MTRANS - mental transfer of information
mTransRelevantFields = ['mObject']        
mTransRule = ParseRule('MTRANS',mTransRelevantFields) 

# MBUILD - construction of new information from old information
mBuildRelevantFields = ['mObject']        
mBuildRule = ParseRule('MBUILD',mBuildRelevantFields) 

# Instrumental Acts:
# ----------------

# EXPEL - expulsion of object from the body
expelRelevantFields = ['object']        
expelRule = ParseRule('EXPEL',expelRelevantFields) 

# MOVEB - move body part
movebRelevantFields = ['object','from','to']        
movebRule = ParseRule('MOVEB',movebRelevantFields) 

# GRASP - grasp an object
graspRelevantFields = ['object','from']        
graspRule = ParseRule('GRASP',graspRelevantFields) 

# ATTEND - focus a sense organ
attendRelevantFields = ['object','to']        
attendRule = ParseRule('ATTEND',attendRelevantFields) 

# SPEAK - make noise
speakRelevantFields = ['object','to']        
speakRule = ParseRule('SPEAK',speakRelevantFields) 
