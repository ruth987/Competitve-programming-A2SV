class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = [ None for _ in range(26) ] 

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root
        for ch in word:
            pos = ord(ch)-ord("a")
            if not cur.children[pos]:
                cur.children[pos] = TrieNode() 
            cur = cur.children[pos]

        cur.is_end = True
            
    def search(self, word: str) -> bool:
        cur = self.root
        for ch in word:
            pos = ord(ch)-ord("a")
        
            cur = cur.children[pos]
            if not cur.is_end:
                return False

        return cur.is_end

class Solution:
    def longestWord(self, words: List[str]) -> str:
        trie = Trie()

        for word in words:
            trie.insert(word)
        
        ans = []
        for word in words:
            if trie.search(word):
                ans.append(word)

        ans.sort(key = lambda x : (-len(x), x)) 

        return ans[0] if ans else ""