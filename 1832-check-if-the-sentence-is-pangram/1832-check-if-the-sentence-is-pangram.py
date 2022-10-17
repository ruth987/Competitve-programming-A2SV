class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        sentence = collections.Counter(sentence)
        alphabet = ('q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m')
        count = 0
        
        for letter in alphabet:
            if letter in sentence:
                count+=1
                
        if count == 26:
            return True
        return False