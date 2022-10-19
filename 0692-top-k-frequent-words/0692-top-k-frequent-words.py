class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        mydict = {}
        for word in words:
            if word not in mydict:
                mydict[word] = 1
            else:
                mydict[word] += 1
        mydict = sorted(mydict.items(),key = lambda item: (-item[1], item[0]))
        answer = []
        for idx in range(k):
            answer.append(mydict[idx][0])
        return answer