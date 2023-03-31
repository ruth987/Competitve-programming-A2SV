class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        def check(adict):
            ans = True
            for val in adict.values():
                if val != 0:
                    ans = False
                    break
            return ans
        
        mydict = defaultdict(int)
        max_ans = 0
        n = len(requests)
        def backtrack(arr, idx):
            nonlocal max_ans
            if idx == n:
                res = check(mydict)
                # print(arr, res)
                if res:
                    max_ans = max(max_ans, len(arr))
                return
            # if we take the next request
            mydict[requests[idx][0]] -= 1
            mydict[requests[idx][1]] += 1
            backtrack(arr+[requests[idx]] , idx+1)
            # if we dont take the next request
            mydict[requests[idx][0]] += 1
            mydict[requests[idx][1]] -= 1
            backtrack(arr, idx+1)
        
        backtrack([], 0)
        return max_ans