'''
RECOMMENDATION DETECTION SYSTEM

Created on 04/04/2015

@author: 
    Nihar Khetan <nkhetan@indiana.edu>, Ghanshyam Malu <gmalu@indiana.edu>, Varsha Suresh Kumar<vsureshk@indiana.edu>

Usage: 
    Execute the RecommendationDetectionSystem.py code using python 2.7

Description:   
    This module uses nltk toolkit to compute similarity between two synsets
    This file can be tested locally    

'''
from nltk.corpus import wordnet as wn

class SimilarityFinder:
    
    def __init__(self, recoItems):
        '''Sets the attributes for the recommeded items'''
        self.recoItems = recoItems
        
    def findSimilarity(self):
        #As we recommend only one item first item of this list will be recommended item
        #Second item can be list of items
        '''So what we try to do is get exact synset of first item and get 10 synsets (to reduce computation costs) of second list of items over 
        which the first item was preferred/recommended'''
        
        recommendation = wn.synsets(self.recoItems[0])  # @UndefinedVariable
        recommendationFiltered = []
        for eachSyn in recommendation:
            if self.recoItems[0] in str(eachSyn):
                recommendationFiltered.append(eachSyn)
                
        choices = {}
        for eachItem in self.recoItems[1]:
            choices[eachItem] = wn.synsets(eachItem)[:10]   # @UndefinedVariable getting only 10 items
        
        choiceScores = {}
        for key, value in choices.iteritems():
            choiceScores[key] = []
            for eachValue in choices[key]:            
                for eachRecoSyn in recommendationFiltered:                
                    choiceScores[key].append(eachRecoSyn.path_similarity(eachValue))
                            
        maxChoiceScores = {}
        
        for eachKey in choiceScores.keys():        
            maxChoiceScores[eachKey] = max(choiceScores[eachKey])
        
        return maxChoiceScores




# Main()
if __name__ == "__main__":
    
    prefModel1 = ['book',['movie','popcorn','comics']]
    prefModel = ['movie',['movie','food']]
    sim = SimilarityFinder(prefModel)
    sim.findSimilarity()