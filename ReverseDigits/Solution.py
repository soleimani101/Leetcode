class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        res  = str(x)
        if "-" in res:
            res =res.replace("-","")
            if int(res[::-1]) *-1 <-2**31 or int(res[::-1]) *-1 > 2**31 - 1 :
                return 0 
            
            return int(res[::-1]) *-1
        else:
            if int(res[::-1]) *-1 <-2**31 or int(res[::-1]) *-1 > 2**31 - 1 :
                return 0 
            return int(res[::-1])

    
        

        
solution = Solution()
res =solution.reverse(1534236469)
        
print(res)
        
        
        
        
        
        
        
print()
