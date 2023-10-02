class TrieNode:
    def __init__(self):
        self.children = {}
        self.prefixCount = 0
        
        
class MapSum:  
    def __init__(self):
        self.root = TrieNode()
        self.map = {}

    def insert(self, key: str, val: int) -> None: 
        valval = val
        if key in self.map:     
            valval = val - self.map[key]

        self.map[key] = val
        
        cur = self.root
        for c in key:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
            cur.prefixCount += valval

    def sum(self, prefix: str) -> int:
        cur = self.root
        for c in prefix:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        return cur.prefixCount




'''
Time complexity: O(m) to insert key of length m as well it is O(m) to evaluate sum for prefix of length m. 
Space complexity: O(T) where T it total length of all words.
'''