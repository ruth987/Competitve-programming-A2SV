class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        countTrue=0
        countFalse=0
        maxTF=0
        start=0
        n=len(answerKey)
        for i in range(n):
            if answerKey[i]=="T":
                countTrue+=1
            else:
                countFalse+=1
            while countTrue>k and countFalse>k:
                if answerKey[start]=="T":
                    countTrue-=1
                else:
                    countFalse-=1
                start+=1
            if (countTrue<=k or countFalse<=k) and maxTF<(countTrue+countFalse):
                maxTF=countFalse+countTrue
        return maxTF
        
        
            