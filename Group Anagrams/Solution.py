class Solution(object):       
    def groupAnagrams(self, strs):
        anagram_groups = {}
        
        for word in strs:
            sorted_word = ''.join(sorted(word))
            if sorted_word in anagram_groups:
                anagram_groups[sorted_word].append(word)
                print(anagram_groups)
            else:
                anagram_groups[sorted_word] = [word]
                print(anagram_groups)
        print(anagram_groups)

        
        return list(anagram_groups.values())


                        
        
                
                    
            
            
            
            
            
            
strs = ["eat","tea","tan","ate","nat","bat"]
strs = ["","",""]

res = Solution().groupAnagrams(strs=strs)
# res = Solution().isAnagram(t="", s="")

print(res)
