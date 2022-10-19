class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        mydict = collections.Counter(words)
        mydict = sorted(mydict.items(),key = lambda item: (-item[1], item[0]))
        answer = []
        
        for index in range(k):
            answer.append(mydict[index][0])
        return answer