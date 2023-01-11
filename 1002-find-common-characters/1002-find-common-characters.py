class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        answer = []
        
        for letter in words[0]:
            min_count = len(words[0])
            for idx in range(len(words)):
                min_count = min(min_count, words[idx].count(letter))

            if letter not in answer:
                for i in range(min_count) :
                        answer.append(letter)
        return answer