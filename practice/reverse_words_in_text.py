#How do I evaluate total complexity
def reverseWords(s: str) -> str:
    #O(n) time and space
    def join(iterable, seperator):
        mapped_iterable = map(str, iterable)
        seperator = str(seperator)
        string = next(mapped_iterable, '')
        for s in mapped_iterable:
            string += seperator + s
        return string
      
    #O(n) time and space
    def reverse(s):
        s = [i for i in s]
        left,right= 0,len(s)-1
        while left<=right:
            s[left],s[right] = s[right],s[left]
            left += 1
            right -= 1
        return join(s,"")
    
    #O(n) time and space
    def split(string,seperator):
        ret = ""
        words = []
        for i in range(len(string)):
            if s[i]!=seperator:
                ret += s[i]
            else:
                words.append(ret)
                ret = ""
        
        words.append(ret)
        return words
        
    words = split(s," ")
    words[:] = [reverse(i) for i in words]
        
    return join(words," ")
print(reverseWords("Ian is an eagle"))
    
