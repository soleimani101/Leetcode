class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        if (len(s) != len(t)):
            return False
        else:
            for i in s : 
                t = t.replace(i,"",1)
                
            if(len(t) != 0):
                return False
            else:
                return True        



s = "anagram"
t = "nagaram"
res = Solution().isAnagram(s = s,t=t)

print(res)