class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        cur = self.root
        for ch in word:
            cur = cur.children.setdefault(ch, TrieNode())

        cur.is_end = True
        

    def search(self, word):
        def dfs(node, index):
            if index == len(word):
                return node.is_end
               
            if word[index] == ".":
                for chi in node.children.values():
                    if dfs(chi, index+1): 
                        return True

            if word[index] in node.children:
                return dfs(node.children[word[index]], index+1)
            
            return False
    
        return dfs(self.root, 0)



# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)