import re

def word_arithmetic(op:str)->str:
    #make all string lower case to be fully
    #compatitble with the algorithm
    op = op.lower()
    
    #lookup table for expected list of tokens
    tokens_lookup = {
        1:"one",
        2:"two",
        3:"three",
        4:"four",
        5:"five",
        6:"six",
        7:"seven",
        8:"eight",
        9:"nine",
        0:"zero",
        "+":"plus",
        "-":"minus"
    }
    
    #list of tokens
    tokens = [] 
    ret = 0
   
    for key,value in tokens_lookup.items():
        res = re.search(value,op)
        #try using eval statement to calculate the answer in a += manner
        if res:
            tokens.append([key,res.start()])
            
    
    if ret >0:
        rex = "negative"+tokens_lookup[ret]
    else:
        rex = tokens_lookup[ret]
    
    return tokens

print(word_arithmetic("onepluseight"))
    
