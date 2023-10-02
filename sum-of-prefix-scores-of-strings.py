class TrieNode:
    def __init__(self):
        self.children = [None for _ in range(26)]
        self.count = 0
        self.isEnd = False

class Solution:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        curr = self.root
        for ch in word:
            pos = ord(ch)-97
            if not curr.children[pos]:
                curr.children[pos] = TrieNode()
            
            curr = curr.children[pos]
            curr.count += 1 
        curr.isEnd = True

    def search(self, word):
        count = 0
        curr = self.root
        for ch in word:
            pos = ord(ch)-97
            # print(count)
            curr = curr.children[pos]
            count += curr.count 
        return count
            

    def sumPrefixScores(self, words: List[str]) -> List[int]:
        for word in words:
            self.insert(word)
        ans = []
        for word in words:
            # print(word)
            ans.append(self.search(word))
        
        return ans