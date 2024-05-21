class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # # Brute Force Approach - O(n^2)
        # numsSize = len(nums)
        # for i in range(numsSize):
        #     for j in range(numsSize):
        #         if nums[i] + nums[j] == target and i != j:
        #             return [i, j]
        # return []

        # Hashtable - O(n)
        seen = {}
        for ind, val in enumerate(nums):
            remainder = target - val

            if remainder in seen:
                return [ind, seen[remainder]]
            seen[val] = ind

