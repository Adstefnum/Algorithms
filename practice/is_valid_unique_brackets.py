#Time: O(n), Space: O(1)
def is_valid(combination):
    diff = 0
    for par in combination:
        #add 1 to diff if we have (
        if par == "(":
            diff += 1
            
        else:
            #There is no opening parentheses after runnig the above, so no +1 is added, so just forget it
            # This is because no matter the combination, we must have () open then close, ) cannot start
            if diff==0:
                return False
            #subtract -1 if we have )
            else:
                diff -= 1
    #diff must be zero at the end because +1-1 for each pair         
    return diff==0
        
print(is_valid("()()()"))
print(is_valid("((()()))"))
print(is_valid(")()()()("))

