  #sliding window
  #O(n) + O(26)[for matches] = O(n) time and O(2*26) = O(1) space
  def checkInclusion(self, s1: str, s2: str) -> bool:
      #substring cannot be less than string
      s1_len,s2_len = len(s1),len(s2)
      if s1_len > s2_len:
          return False

      #insantiate array storage
      s1map=[0]*26
      s2map = [0]*26
      #How does s1map=s2map=[0]*26 causes both of them to be equal and cause true always??

      #prefill the arrays
      for i in range(s1_len):
          s1map[ord(s1[i])-ord('a')] += 1
          s2map[ord(s2[i])-ord('a')] += 1

      #variable to check for matches
      matches = left =  0

      #initial check for the arrays we just prefilled and this also 
      #prefills the matches variable
      #the check to see if matches equals 26 is done in the 
      #next loop to prevent redundancy
      for i in range(26):
          matches += 1 if s1map[i]==s2map[i] else 0
      #we can start from the char at the idx that corresponds to
      #the length of s1 since we already captured previous chars
      for right in range(s1_len,s2_len):
          #if the values of all indices in the array are equal
          #meaning we have a match return true
          if matches == 26:
              return True

          #add a char to the sliding window
          #if adding it causes a match at the idx in the array
          #add 1 but if it causes a mismatch, minus 1
          idx = ord(s2[right]) - ord('a')
          s2map[idx] += 1
          if s1map[idx] ==  s2map[idx]:
              matches += 1
          #check for mismatch by seeing if +1 to the value at
          #that idx is what now matches the incremented idx value
          elif s1map[idx]+1 ==  s2map[idx]:
              matches -= 1

          #this simulates removing a value from the left
          #reason the logic from above case
          idx = ord(s2[left]) - ord('a')
          s2map[idx] -= 1
          if s1map[idx] ==  s2map[idx]:
              matches += 1
          elif s1map[idx]-1 ==  s2map[idx]:
              matches -= 1
          left  += 1
          #the matches might be equal after last iteration 
          #so this is a check and return in one
      return matches==26


