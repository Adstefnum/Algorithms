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
    
    #list of pre_tokens
    pre_tokens = [] 
    ret = ""
   
    for key,value in tokens_lookup.items():
        res = re.search(value,op)
        #try using eval statement to calculate the answer in a += manner
        if res:
            pre_tokens.append([str(key),res.start()])
    #O(len(op)log(len(op) if we traverse over each letter?
    pre_tokens.sort(key=lambda x: x[1])
    tokens = [i[0] for i in pre_tokens]
    ret = int(eval("".join(tokens)))
    
    if ret >0:
        rex = "negative"+tokens_lookup[ret]
    else:
        rex = tokens_lookup[ret]
    
    return rex

#need to handle taking in duplicate values e.g two ones in onepluseightminusonezero
#need to break back up into tokens to return right answer e.g -11= negative one one
print(word_arithmetic("onepluseightminustwozero"))
    
