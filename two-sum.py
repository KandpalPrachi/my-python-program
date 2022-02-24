class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        arraysum = {}
        
        for index, n in enumerate(nums):
            diff = target - n
            if diff in arraysum:
                return [arraysum[diff], index]
            arraysum[n] = index