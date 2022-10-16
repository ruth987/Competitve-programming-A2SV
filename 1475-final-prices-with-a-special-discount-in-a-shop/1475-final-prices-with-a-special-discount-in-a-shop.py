class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        answer = []
        for idx in range(len(prices)):
            x = 0
            for index in range(idx+1, len(prices)):
                if prices[index] <= prices[idx]:
                    x = 1
                    answer.append(prices[idx]-prices[index])
                    break
            if x == 0:
                answer.append(prices[idx])
                    
        return answer