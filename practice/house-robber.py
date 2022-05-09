#O(n) time and space
  def rob(self, nums: List[int]) -> int:
      n = len(nums)
      res = [0]*n
      if n == 0:
          return 0
      if n == 1:
          return nums[0]
      res[0] = nums[0]
      res[1] = max(nums[0],nums[1])
      for i in range(2,n):
          res[i] = max(nums[i]+res[i-2],res[i-1])
      return res[-1]
