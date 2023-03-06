class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        q = []
        for que in queries:
            mydict = {}
            for letter in que:
                if letter in mydict:
                    mydict[letter] += 1
                else:
                    mydict[letter] = 1
            mydict = dict(sorted(mydict.items(), key= lambda item: item[0]))
            # print(mydict)
            for val in mydict.values():
                f_val = val
                break
            q.append(f_val)
        
        w = []
        for word in words:
            mydict = {}
            for letter in word:
                if letter in mydict:
                    mydict[letter] += 1
                else:
                    mydict[letter] = 1
            mydict = dict(sorted(mydict.items(), key =lambda item: item[0]))
            # print(mydict)
            for val in mydict.values():
                w_val = val
                break
            w.append(w_val)
        w.sort()
        # print(q, w)
        ans = []
        ln = len(words)
        for value in q:
            pos = bisect_right(w, value)
            ans.append(ln-pos)
        # print(ans) 
        return ans
            
            