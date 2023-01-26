class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:

        ptr1, ptr2 = 0, 0
        l_w1 = len(word1)
        l_w2 = len(word2)
        ans = []
        while ptr1<l_w1 and ptr2<l_w2:
            if word1[ptr1] < word2[ptr2]:
                ans.append(word2[ptr2])
                ptr2 += 1
            elif word1[ptr1] > word2[ptr2]:
                ans.append(word1[ptr1])
                ptr1+=1
            else: #word1[ptr1] == word2[ptr2]
                p1, p2 = ptr1, ptr2
                while p1<l_w1 and p2<l_w2 and word1[p1] == word2[p2]:
                    p1 += 1
                    p2 += 1
                if p1 == l_w1 :
                    ans.append(word2[ptr2])
                    ptr2 += 1
                elif p2 == l_w2:
                    ans.append(word1[ptr1])
                    ptr1+=1
                elif word1[p1] < word2[p2]:
                    ans.append(word2[ptr2])
                    ptr2 += 1
                elif word1[p1] > word2[p2]:
                    ans.append(word1[ptr1])
                    ptr1+=1
        while ptr1 < l_w1:
            ans.append(word1[ptr1])
            ptr1 += 1
        while ptr2 < l_w2:
            ans.append(word2[ptr2])
            ptr2 += 1
        return "".join(ans)
            
                    
                    