class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word1_ptr, word2_ptr = 0, 0
        answer = ""
        
        while word1_ptr < len(word1) and word2_ptr < len(word2):
            answer += word1[word1_ptr]
            answer += word2[word2_ptr]
            word1_ptr += 1
            word2_ptr += 1
        
        while word1_ptr < len(word1):
            answer += word1[word1_ptr]
            word1_ptr += 1
            
        while word2_ptr < len(word2):
            answer += word2[word2_ptr]
            word2_ptr += 1
        
        return answer