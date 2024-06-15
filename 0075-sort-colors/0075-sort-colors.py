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

        # # Brute Force solution - Selection Sort [O(n^2)]
        # for i in range(len(nums)):
        #     for j in range(i, len(nums)):
        #         if nums[i] > nums[j]:
        #             nums[i], nums[j] = nums[j], nums[i] # swap

        # Optimized solution - Pointers [O(n)]
        """
        This strategy works by using three pointers to partition the array into 
        sections of 0s, 1s, and 2s in a single pass, swapping elements to place 
        0s at the beginning and 2s at the end, achieving sorting in constant space 
        and linear time.
        """
        red, white, blue = 0, 0, len(nums) - 1

        while white <= blue:
            if nums[white] == 0:
                nums[red], nums[white] = nums[white], nums[red]
                white += 1
                red += 1
            elif nums[white] == 1:
                white += 1
            else:
                nums[white], nums[blue] = nums[blue], nums[white]
                blue -= 1
