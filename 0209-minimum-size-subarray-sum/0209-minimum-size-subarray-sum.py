class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        min_len = n + 5 # Arbitrary Number to indicate this is initialization value
        left, window_sum = 0, 0

        for right in range(n):
            window_sum += nums[right]
            while window_sum >= target:
                min_len = min(min_len, (right - left + 1))
                window_sum -= nums[left]
                left += 1
        return min_len if min_len != n+5 else 0

        """
        # Attempt 1 - Not Effecient Enough
        # Why? - Because computing sum(sub_arr) over and over adds quiet a bit of overhead
        left = 0
        right = 1
        len_nums = len(nums)
        min_len = 0

        while left <= right:
            sub_arr = nums[left:right]
            window_sum = sum(sub_arr)

            if window_sum >= target:
                min_len = min(min_len, len(sub_arr)) if min_len != 0 else len(sub_arr)
                left+=1
                continue
            
            if right < len_nums:
                right += 1
            elif left >= len_nums - 1:
                print("Breaking out")
                break
            else:
                left += 1
        
        return min_len
        """