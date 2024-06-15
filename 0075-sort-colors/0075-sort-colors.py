class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        """
        - Colors
            0 - red
            1 - white
            2 - blue
        - Order - red, white, and blue (0, 1, 2)
        - Sort in-place (can't save data elsewhere)
        """

        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if nums[i] > nums[j]:
                    nums[i], nums[j] = nums[j], nums[i] # swap
        