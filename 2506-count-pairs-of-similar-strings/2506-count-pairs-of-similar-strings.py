class Solution:
    def similarPairs(self, words: List[str]) -> int:
        """
        words = ["aba","aabb","abcd","bac","aabc"]
        
        similar words: words which have same characters
        we have to use hashtable to count all the possible pairs.
        
        1, changing each into a set then storing it in a dictionary if it doesnt already
        exist.
        2, if it is already there just increament the count in the dictionary
        
        3, when ever it is already there before increamenting increase the answer by the
        number of count of that word in the dictionary
        
        """
        count = 0
        for idx in range(len(words)):
            for i in range(idx+1, len(words)):
                if set(words[idx]) == set(words[i]):
                    count += 1
        
        return count