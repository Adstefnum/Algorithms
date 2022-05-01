#O(n) time and space
  #sliding window problem
  def lengthOfLongestSubstring(s: str) -> int:
      #keep track of characters
      chars = set()
      left = res = 0

      for right in range(len(s)):
          while s[right] in chars:
              #keep removing duplicate characters from the left until 
              #none is any longer in the set
              chars.remove(s[left])
              left += 1
          #add the new character
          chars.add(s[right])
          #right-left gives the length of the substring and 
          #he +1 is to cancel zero indexing
          #the max substring length throughout the whole run will be kept
          #if no other calculated length is greater than the previous ones
          #res has been set to then that one is returned, if we however reach
          #another one then that becomes res
          res = max(res,right-left+1)
      return res
