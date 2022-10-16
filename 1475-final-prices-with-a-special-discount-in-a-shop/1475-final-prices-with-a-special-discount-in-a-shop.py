class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack = []
        for idx, price in enumerate(prices):
            while stack and prices[stack[-1]] >= price:
                index_to_edit = stack.pop()
                prices[index_to_edit] -= price
            stack.append(idx)
            
        return prices
