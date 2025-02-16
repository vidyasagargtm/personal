

class Solution:
    
    def is_vowels(self, char):
        char = char.lower()
        return True if char == "a" or char == "e" or char == "i" or char == 'o' or char == "u" else False
            
    
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        left_index = 0
        right_index = len(s) - 1
        while left_index < right_index:
            
            while left_index < len(s):
                if self.is_vowels(s[left_index]):
                    break
                left_index += 1
                
            
            while right_index > -1:
                if self.is_vowels(s[right_index]):
                    break
                right_index -= 1
                
            if left_index < right_index:
                s[left_index], s[right_index] = s[right_index], s[left_index]
            left_index += 1
            right_index -= 1   
        return ''.join(s)
        




s = Solution()
# print("sagar")

print(s.reverseVowels("'.,"))