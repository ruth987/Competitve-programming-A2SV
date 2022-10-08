class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        text = text.split()
        count = len(text)
        
        for word in text:
            for letter in word:
                if letter in brokenLetters:
                    count-=1
                    break
                    
        return count