#O(n) time and O(1) space
def singleNumber(self, nums: List[int]) -> int:
        xor  = 0
        for n in nums:
            xor ^= n
        return xor
