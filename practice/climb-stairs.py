#O(n) time and space
  def climbStairs(self, n: int) -> int:
      mem = {}
      def memoized_fib(n):
          if n <= 1:
              return 1
          if n in mem:
              return mem[n]
          mem[n] = memoized_fib(n-1) + memoized_fib(n-2)
          return mem[n]
      return memoized_fib(n)
