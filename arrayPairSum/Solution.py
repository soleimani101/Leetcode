class Solution(object):
    def arrayPairSum(self, nums):
        nums.sort()  # Sort the array in ascending order
        total_sum = 0
        
        # Pair adjacent elements and sum the minimum of each pair
        for i in range(0, len(nums), 2):
            total_sum += nums[i]
        
        return total_sum
            