#O(n) time and O(1) space
#This doesn't solve the problem of wrong closing even if it is balanced numberwise
def is_valid(combination,char):
    diff = 0
    
    for comb in combination:
        if comb == char[0]:
            diff += 1
        
        else:
            #This can't work here because we might not have the char yet and 
            #so have zero but it might still be in the string
            if diff == 0:
                return False
                
            elif comb == char[1]:
                diff -= 1
    return diff == 0

def all_valid(combination):
    return is_valid(combination,"()") and is_valid(combination,"{}") and is_valid(combination,"[]")

#Time:O(n) for filling the stack. The checks occur in O(1)
#space: O(n) for stack
def all_valid_stack(combination):
    
    stack = []
    
    for char in combination:
        if char in ["[","{","("]:
            stack.append(char)
            
        else:   
            if not stack:
                return False
                
            current_char = stack.pop()
            if current_char == "(":
                if char != ")":
                    return False
                    
            if current_char == "[":
                if char != "]":
                    return False
                    
            if current_char == "{":
                if char != "}":
                    return False
        
    if stack:
        return False
        
    return True
    
    
print(is_valid("()[(){}()]","()"))
print(all_valid("()[(){}()]"))
print(all_valid("({[}])"))
print(all_valid_stack("()[(){}()]"))
print(all_valid_stack("({[}])"))


