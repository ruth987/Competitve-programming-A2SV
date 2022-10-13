class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = {'a','e','i','o','u','A','E','I','O','U'}
        n = int(len(s)/2)
        first, second = 0, 0

        for letter in s[:n]:
            if letter in vowels:
                first+=1
        for letter in s[n:]:
            if letter in vowels:
                second+=1
        if first == second:
            return True
        return False
            
            
        