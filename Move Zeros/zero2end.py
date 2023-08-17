nums = [0,1,0,3,12]

def moveZeroes( nums):
    for i in range(len(nums)-1):
        if nums[i] == 0:
            nums[i+1], nums[i] = nums[i], nums[i +1]
    
        print(nums)
        
        
moveZeroes(nums)