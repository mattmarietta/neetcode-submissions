class Solution:
    def isPalindrome(self, s: str) -> bool:
        #Define 2 pointers for traversal
        pattern = r'[^a-zA-Z0-9]'
        s = s.replace(" ", "")
        s = s.lower()
        s = re.sub(pattern, '', s)
        print(s)
        left, right = 0, len(s) - 1
        is_pali = True
  
        while left < right:
            if s[left] != s[right]:
                is_pali = False
                break
            left += 1
            right -= 1

        return is_pali

