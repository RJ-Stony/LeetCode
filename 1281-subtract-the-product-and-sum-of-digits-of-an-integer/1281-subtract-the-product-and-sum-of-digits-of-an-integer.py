class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        product_n = 1
        sum_n = 0
        
        num_list = list(str(n))
        for num in num_list:
            product_n *= int(num)
            sum_n += int(num)
            
        return product_n - sum_n