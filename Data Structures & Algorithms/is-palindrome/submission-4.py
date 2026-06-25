import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Palindrome has same count
        # Double for loop and remove all the punctuation
        new_word = re.sub(r"[^\w]|_", "", s)

        # If we reverse the word it should work
        print(new_word.lower())
        #
        return new_word.lower() == "".join(reversed(new_word.lower()))