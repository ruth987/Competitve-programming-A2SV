class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:

        mydict = defaultdict(int)
        for word in words:
            mydict[word] += 1

        maxheap = []
        for key,val in mydict.items():
            heapq.heappush(maxheap, (-val, key))

        ans = []
        while k:
            ans.append(heapq.heappop(maxheap)[1])
            k-=1
        return ans