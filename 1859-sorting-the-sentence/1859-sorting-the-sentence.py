class Solution:
    def sortSentence(self, s: str) -> str:
        bucket = [""]*10

        s = s.split(" ")

        for wr in s:
            bucket[int(wr[-1])] += wr

        res = ""

        for wr in bucket:
            if wr != "":
                res += wr[:-1] + " "

        return res[:-1]
        
        