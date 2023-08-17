class Solution(object):
    def productExceptSelf(self ,nums):
        n = len(nums)
        left_products = [1] * n
        right_products = [1] * n
        product = 1
        for i in range(n):
            left_products[i] = product
            product *= nums[i]
        product = 1
        for i in range(n - 1, -1, -1):
            right_products[i] = product
            product *= nums[i]

        
        answer = [left_products[i] * right_products[i] for i in range(n)]
        return answer
        
        
        
        
        
        
        
        
        
        
        
        
            
            
nums = [1,2,3,4]

res = Solution().productExceptSelf(nums=nums)
# res = Solution().isAnagram(t="", s="")

print(res)