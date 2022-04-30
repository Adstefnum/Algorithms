#O(1) time and space
def rotate(self, nums: list[int], k: int) -> None:
        n = len(nums)
        in_key = (n-(k%n))
        nums[:] = nums[in_key:] + nums[:in_key]
print([0,1,2,3,4,5,6,7],3)
