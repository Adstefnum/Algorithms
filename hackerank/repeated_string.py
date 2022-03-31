#!/usr/bin/python3

def repeatedString(s,n):
    s = s*((n//len(s))+1)
    count = 0
    for i in s[0,n-1]:
        if i =='a':
            count += 1
    return count

print(repeatedString('kmretasscityylpdhuwjirnqimlkcgxubxmsxpypgzxtenweirknjtasxtvxemtwxuarabssvqdnktqadhyktagjxoanknhgiln',736778906400))
