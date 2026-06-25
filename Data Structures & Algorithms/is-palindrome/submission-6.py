import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Palindrome has same count
        # Double for loop and remove all the punctuation
        new_word = re.sub(r"[^\w]|_", "", s)
        new_word = new_word.lower()
        # 2 pointer
        left, right = 0, len(new_word) - 1

        while left <= right:
            print(new_word[left])
            print(new_word[right])
            if new_word[left] != new_word[right]:
                return False
                break
            left += 1
            right -= 1
        return True