class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        """
        how should i choose when to buy and when to sell a good
        there are two cases :
        - if i buy the first one
        - if i dont buy the first one

        """
        with_first = -prices[0]
        without_first = 0
        
        for p in range(1, len(prices)):
            with_first = max(with_first, without_first-prices[p])
            without_first = max(without_first, with_first+prices[p]-fee)
        
        return without_first