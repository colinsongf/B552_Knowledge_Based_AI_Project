import cPickle as pickle

'''
 Conceptual Dependencies
 
 {'CD1' : {'PTRANS' : {'actor' : 'I',
                        'object' : 'I',
                        'from' : '?',
                        'to' : 'AMC',
                        'instr' : '?'}}} 

{'CD2' : ['Location', ['I'], AMC']}

{'result': ['CD1', 'CD2'] }    
                    
{'CD3' : {'MTRANS' : {'actor' : 'I',
                        'object' : 'SpiderMan',
                        'from' : 'SpiderMan',
                        'to' : 'I',
                        'instr' : { 'ATTEND' : { 
                        'actor' : 'I',
                        'object' : '?',
                        'from' : '?',
                        'to' : 'Movie Screen'
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

{'CD6' : ['Location', ['I','John','Mary'], 'AMC']}

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

CD_dict = {
1: {'result' : [{'CD1' : {'PTRANS' : {'actor' : 'I',
                        'object' : 'I',
                        'from' : '?',
                        'to' : 'AMC',
                        'instr' : '?'}}} ,
                {'CD2' : ['Location', ['I'], 'AMC']}]},
           
2: {'enable' : [{'CD2' : 'Location I AMC'}, 
                {'CD3' : {'MTRANS' : {'actor' : 'I',
                        'object' : 'SpiderMan',
                        'from' : 'SpiderMan',
                        'to' : 'I',
                        'instr' : { 'ATTEND' : { 
                        'actor' : 'I',
                        'object' : '?',
                        'from' : '?',
                        'to' : 'Movie Screen'
                        }}}}} ]},
           
3: { 'result' : [{'CD5' : {'PTRANS' : {'actor' : ['I','John','Mary'],
                        'object' : ['I','John','Mary'],
                        'from' : '?',
                        'to' : 'AMC',
                        'instr' : '?'}}} ,
                 {'CD6' : ['Location', ['I','John','Mary'], 'AMC']} ]},
           
4: { 'enable' : [{'CD3' : {'MTRANS' : {'actor' : 'I',
                        'object' : 'SpiderMan',
                        'from' : 'SpiderMan',
                        'to' : 'I',
                        'instr' : { 'ATTEND' : { 
                        'actor' : 'I',
                        'object' : '?',
                        'from' : '?',
                        'to' : 'Movie Screen'
                        }}}}} ,
                 {'CD7' : {'MTRANS' : {'actor' : 'I',
                        'object' : {'ATTEND' :   
                                    {'actor' : '?',
                                    'from' : '?',
                                    'to' : 'book',
                                    'instr' : '?'},
                        'from' : 'I',
                        'to' : 'AMC',
                        'instr' : '?'}}}} ]},
           
5: {'CD4': {'MTRANS'    : {'actor' : 'I',
                        'object' : 'popcorn',
                        'love-state-before' : '?',
                        'love-state-after' : '>8',
                        }}}
           
}

# Saving the CD dictionary in a pickle file
pickle.dump(CD_dict, open('CDs.p', 'wb'))       
