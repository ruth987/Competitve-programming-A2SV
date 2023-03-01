class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        adict = Counter(s)
        stack = []
        aset = set()
        for ch in s:
            while stack and ch < stack[-1] and adict[stack[-1]] > 0 and ch not in aset:
                aset.remove(stack[-1])
                stack.pop()
                
            if ch not in aset:
                stack.append(ch)
            aset.add(ch)
            adict[ch] -= 1
            
        return "".join(stack)