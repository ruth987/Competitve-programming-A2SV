class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        n_str = str(n)
        product, summation = 1, 0
        for digit in n_str:
            product *= int(digit)
            summation += int(digit)
        return product-summation
            