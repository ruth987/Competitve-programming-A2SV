class Solution:
    def repeatedCharacter(self, s: str) -> str:
        aset = set()
        
        for letter in s:
            if letter not in aset:
                aset.add(letter)
            else:
                return letter
    