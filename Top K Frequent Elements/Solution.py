class Solution(object):
    def topKFrequent(self, nums, k):
        dictnum = {}
        for i in nums: 
            if i in dictnum:
                dictnum[i] += 1
            else:
                dictnum[i] = 1
        
        sorted_items = sorted(dictnum.items(), key=lambda item: item[1], reverse=True)
        # Create a new dictionary from the sorted items
        sorted_dict = {key: value for key, value in sorted_items}

        lst = list({key: sorted_dict[key] for key in list(sorted_dict)[:k]})
        return lst
        
        
        
  
  
  
  
  
      
nums = [4,1,-1,2,-1,2,3]
k = 2
solution = Solution()
res = solution.topKFrequent(nums=nums,k=k)
print(res)