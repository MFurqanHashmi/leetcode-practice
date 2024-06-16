class Solution:
    # Optomized Solution
    def countSubstrings(self, s: str) -> int:
        num_of_palindromes = 0

        for i in range(len(s)):
            # For odd length palindromes
            l = r = i
            num_of_palindromes += self.countPalindromes(s, l, r)
            
            # For even length palindromes
            l = i
            r = i+1
            num_of_palindromes += self.countPalindromes(s, l, r)
        
        return num_of_palindromes

    def countPalindromes(self, s, l, r) -> int:
        num_of_palindromes = 0

        while l >= 0 and r < len(s) and s[l] == s[r]:
            num_of_palindromes += 1

            l -= 1
            r += 1
        
        return num_of_palindromes

    # # Brute Force Solution - O(n^3)
    # def countSubstrings(self, s: str) -> int:
    #     num_of_palindromes = 0
    #     left, right = 0, len(s) - 1

    #     # O(n^2)
    #     for i in range(len(s)):
    #         for j in range(i, len(s)):
    #             subStr = s[i:j+1]
    #             if self.isAPalindrome(subStr):
    #                 num_of_palindromes += 1
        
    #     return num_of_palindromes


    # # O(n)
    # def isAPalindrome(self, subString: str) -> bool:
    #     left, right = 0, max(0, len(subString) -1)
    #     while left <= right:
    #         if subString[left] != subString[right]:
    #             return False
            
    #         left += 1
    #         right -= 1
        
    #     return True