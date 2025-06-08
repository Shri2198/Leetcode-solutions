class Solution:
    def isPalindrome(self, s: str) -> bool:
        word = [char.lower() for char in s if char.isalnum()]
        left = 0
        right = len(word) - 1
        while left < right:
            if word[left] != word[right]:
                return False
            left += 1
            right -= 1
        return True