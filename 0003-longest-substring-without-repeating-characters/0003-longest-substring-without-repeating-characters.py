class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sub_str = set()
        max_len = 0

        left = 0

        for right in range(len(s)):
            if s[right] not in sub_str:
                sub_str.add(s[right])
                max_len = max(max_len, len(sub_str))
                
            else:
                while s[right] in sub_str:
                    sub_str.remove(s[left])
                    left += 1
                sub_str.add(s[right])
        
        return max_len
