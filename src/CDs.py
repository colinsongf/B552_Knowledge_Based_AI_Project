'''
CONCEPT LEVEL SENTIMENT ANALYZER

Created on 04/29/2015

@author: 
    Nihar Khetan <nkhetan@indiana.edu>, Ghanshyam Malu <gmalu@indiana.edu>, Varsha Suresh Kumar<vsureshk@indiana.edu>

Usage: 
    Execute the code using python 2.7

'''
'''
 Conceptual Dependencies
 
 SENTENCE 1
 ----------
-I went to watch spider man at AMC        
-I loved the popcorn.         
-I went with John and Mary.         
-I will recommend to read the book

 SENTENCE 2
 ----------
-I went to watch spider man at AMC        
-I loved the popcorn.         
-I went with John and Mary.         
-I will prefer to watch spider man at IMAX

 SENTENCE 3
 ----------
-I went to watch spider man at AMC        
-I loved the popcorn.         
-I went with John and Mary.         
-I went to watch spider man at IMAX

--------------------------------------------

 {'CD1' : {'PTRANS' : {'actor' : 'I',
                        'object' : 'I',
                        'from' : '?',
                        'to' : 'AMC',
                        'instr' : '?'}}} 

{'CD2' : ['LOCATION', ['I'], AMC']}

{'result': ['CD1', 'CD2'] }    
                    
{'CD3' : {'MTRANS' : {'actor' : 'I',
                        'object' : 'Movie-SpiderMan',
                        'from' : 'Movie-SpiderMan',
                        'to' : 'I',
                        'instr' : { 'ATTEND' : { 
                                    'actor' : 'I',
                                    'object' : 'part-of-I',
                                    'from' : '?',
                                    'to' : 'Movie-Screen'
                                    }}}}} 
                        

{'enable': ['CD2', 'CD3']}
                        
{'CD4': {'MTRANS'    : {'actor' : 'I',
                        'object' : 'popcorn',
                        'love-state-before' : '?',
                        'love-state-after' : '>8',
                        }}}

                        
{'CD5' : {'PTRANS' : {'actor' : ['I','John','Mary'],
                        'object' : ['I','John','Mary'],
                        'from' : '?',
                        'to' : 'AMC',
                        'instr' : '?'}}} 

{'CD6' : ['LOCATION', ['I','John','Mary'], 'AMC']}

{'result' : ['CD5', 'CD6'] }            
            
{'CD7' : {'MTRANS' : {'actor' : 'I',
                        'object' : {'ATTEND' :   
                                    {'actor' : '?',
                                    'from' : '?',
                                    'to' : 'book',
                                    'instr' : '?'},
                        'from' : 'I',
                        'to' : 'AMC',
                        'instr' : '?'}}}} 
                        
                        
{'enable': ['CD3', 'CD7']}
'''

CD_dict1 = {
'1': {'result' : [{'CD1' : {'PTRANS' : {'actor' : 'I',
                        'object' : 'I',
                        'from' : '?',
                        'to' : 'AMC',
                        'instr' : '?'}}} ,             
                {'CD2' : {'LOCATION': {'actor' : ('I'), 
                                         'place' : 'AMC'}}}]},

'2': {'enable' : [{'CD2' : {'LOCATION': {'actor' : ('I'), 
                                         'place' : 'AMC'}}}, 
                {'CD3' : {'MTRANS' : {'actor' : 'I',
                                      'mObject' : 'Movie-SpiderMan',
                                      'from' : 'Movie-SpiderMan',
                                      'to' : 'I',
                                      'instr' : { 'ATTEND' : { 
                                                              'actor' : 'I',
                                                              'object' : 'part-of-I',
                                                              'from' : '?',
                                                              'to' : 'Movie-Screen'
                        }}}}} ]},
           
'3': { 'result' : [{'CD5' : {'PTRANS' : {'actor' : ('I','John','Mary'),
                                       'object' : ('I','John','Mary'),
                                       'from' : '?',
                                       'to' : 'AMC',
                                       'instr' : '?'}}} ,                   
                {'CD6' : {'LOCATION' : {'actor' : ('I','John','Mary'),
                                        'place' : 'AMC'}}} ]},
           
'4': { 'enable' : [{'CD3' : {'MTRANS' : {'actor' : 'I',
                                       'mObject' : 'Movie-SpiderMan',
                                       'from' : 'Movie-SpiderMan',
                                       'to' : 'I',
                                       'instr' : { 'ATTEND' : { 
                                                               'actor' : 'I',
                                                               'object' : 'part-of-I',
                                                               'from' : '?',
                                                               'to' : 'Movie-Screen'
                                                               }}}}} ,
                 {'CD7' : {'MTRANS' : {'actor' : 'I',
                         
                                        'mObject' : {'ATTEND' :   
                                                     {'actor' : '?',
                                                      'object' : 'Book',
                                                      'from' : '?',
                                                      'to' : '?',
                                                      'instr' : '?'}},
                                       'from' : 'I',
                                       'to' : '?',
                                       'instr' : '?'
                                       }}} ]},
           
'5': {'CD4': {'MTRANS'    : {'actor' : 'I',
                        'mObject' : 'popcorn',
                        'state-change-before' : '?',
                        'state-change-after' : 'love>8'                        
                        }}}
           
}

'''---------------------------------------------------------------------------------------------------------'''

CD_dict2 = {
'1': {'result' : [{'CD1' : {'PTRANS' : {'actor' : 'I',
                        'object' : 'I',
                        'from' : '?',
                        'to' : 'AMC',
                        'instr' : '?'}}} ,
                {'CD2' : {'LOCATION': {'actor' : ('I'), 
                                         'place' : 'AMC'}}}]},
            
'2': {'enable' : [{'CD2' : {'LOCATION': {'actor' : ('I'), 
                                         'place' : 'AMC'}}}, 
                {'CD3' : {'MTRANS' : {'actor' : 'I',
                                      'mObject' : 'Movie SpiderMan at AMC',
                                      'from' : 'Movie-SpiderMan',
                                      'to' : 'I',
                                      'instr' : { 'ATTEND' : { 
                                                              'actor' : 'I',
                                                              'object' : 'part-of-I',
                                                              'from' : '?',
                                                              'to' : 'Movie-Screen'
                        }}}}} ]},
           
'3': { 'result' : [{'CD5' : {'PTRANS' : {'actor' : ('I','John','Mary'),
                                       'object' : ('I','John','Mary'),
                                       'from' : '?',
                                       'to' : 'AMC',
                                       'instr' : '?'}}} ,
                {'CD6' : {'LOCATION' : {'actor' : ('I','John','Mary'),
                                        'place' : 'AMC'}}} ]},
           
'4': { 'enable' : [{'CD3' : {'MTRANS' : {'actor' : 'I',
                                       'mObject' : 'Movie SpiderMan at AMC',
                                       'from' : 'Movie-SpiderMan',
                                       'to' : 'I',
                                       'instr' : { 'ATTEND' : { 
                                                               'actor' : 'I',
                                                               'object' : 'part-of-I',
                                                               'from' : '?',
                                                               'to' : 'Movie-Screen'
                                                               }}}}} ,
                 {'CD7' : {'MTRANS' : {'actor' : 'I',
                         
                                        'mObject' : {'ATTEND' :   
                                                     {'actor' : '?',
                                                      'object' : 'Movie SpiderMan at IMAX',
                                                      'from' : '?',
                                                      'to' : '?',
                                                      'instr' : '?'}},
                                       'from' : 'I',
                                       'to' : '?',
                                       'instr' : '?'
                                       }}} ]},
           
'5': {'CD4': {'MTRANS'    : {'actor' : 'I',
                        'mObject' : 'popcorn',
                        'state-change-before' : '?',
                        'state-change-after' : 'love>8'                        
                        }}}
           
}

'''--------------------------------------------------------------------------------------------------------'''

CD_dict3 = {
'1': {'result' : [{'CD1' : {'PTRANS' : {'actor' : 'I',
                        'object' : 'I',
                        'from' : '?',
                        'to' : 'AMC',
                        'instr' : '?'}}} ,
                {'CD2' : {'LOCATION': {'actor' : ('I'), 
                                         'place' : 'AMC'}}}]},

'2': {'enable' : [{'CD2' : {'LOCATION': {'actor' : ('I'), 
                                         'place' : 'AMC'}}}, 
                {'CD3' : {'MTRANS' : {'actor' : 'I',
                                      'mObject' : 'Movie-SpiderMan',
                                      'from' : 'Movie-SpiderMan',
                                      'to' : 'I',
                                      'instr' : { 'ATTEND' : { 
                                                              'actor' : 'I',
                                                              'object' : 'part-of-I',
                                                              'from' : '?',
                                                              'to' : 'Movie-Screen'
                        }}}}} ]},
           
'3': { 'result' : [{'CD5' : {'PTRANS' : {'actor' : ('I','John','Mary'),
                                       'object' : ('I','John','Mary'),
                                       'from' : '?',
                                       'to' : 'AMC',
                                       'instr' : '?'}}} ,
                {'CD6' : {'LOCATION' : {'actor' : ('I','John','Mary'),
                                        'place' : 'AMC'}}} ]},
           
'4': {'result' : [{'CD7' : {'PTRANS' : {'actor' : 'I',
                        'object' : 'I',
                        'from' : '?',
                        'to' : 'IMAX',
                        'instr' : '?'}}} ,
                {'CD8' : {'LOCATION': {'actor' : ('I'), 
                                         'place' : 'IMAX'}}}]},

'5': {'enable' : [{'CD8' : {'LOCATION': {'actor' : ('I'), 
                                         'place' : 'IMAX'}}}, 
                {'CD9' : {'MTRANS' : {'actor' : 'I',
                                      'mObject' : 'Movie-SpiderMan',
                                      'from' : 'Movie-SpiderMan',
                                      'to' : 'I',
                                      'instr' : { 'ATTEND' : { 
                                                              'actor' : 'I',
                                                              'object' : 'part-of-I',
                                                              'from' : '?',
                                                              'to' : 'Movie-Screen'
                        }}}}} ]},
           
'6': {'CD4': {'MTRANS'    : {'actor' : 'I',
                        'mObject' : 'popcorn',
                        'state-change-before' : '?',
                        'state-change-after' : 'love>8'                        
                        }}}
           
}    

'''----------------------------------------------------------------------------------------------------------------'''
# Saving the CD dictionary in a pickle file
#pickle.dump(CD_dict, open('CDs.p', 'wb'))       

def makeCDMasterList(CD_dict):
    ''' Create a master list of all the CDs from the entire list of CD_dict '''
    masterCD_List = []
    tempList = []
    
    ##For every key value pair in the CD_dict, retrieve the list of CDs in the value
    for k,v in CD_dict.iteritems():
        res = getCDList(v) ## Retrieve the CDs from the v (value), if present
        if res is not None:
            tempList.extend(res)
    
    ##Create the master list of CDs from the tempList by elimating the duplicates
    for item in tempList:
        if item not in masterCD_List:
            masterCD_List.append(item)
    return masterCD_List

def getCDList(object):
    ''' Retrieve a list of CDs from the given object '''     
    CD_List = []
    queue=[]
    queue.append(object)
    while (queue != []):
        toExpand = queue[0]
        del queue[0]
        for k,v in toExpand.iteritems():
            if 'CD' in k[:2] :
                CD_List.append(v)  
            elif (isinstance(v, dict)):
                queue.append(v)
            elif (isinstance(v, list)):
                for item in v:
                    if (isinstance(item, dict)):
                        queue.append(item)
                
    return CD_List

def getMasterCDList(option):
    if option == 1:
        return makeCDMasterList(CD_dict1)
    elif option == 2:
        return makeCDMasterList(CD_dict2)
    else:
        return makeCDMasterList(CD_dict3) 
  