#6. wap class to print all possible unique subsets from a set of integers.
class Solution:  
    def subsets(self, s1):  
        return self.uniqueSubsets([], (s1))  
 
    def uniqueSubsets(self, curr, s1):  
        if s1:  
            return self.uniqueSubsets(curr, s1[1:]) + self.uniqueSubsets(curr + [s1[0]], s1[1:])  
        return [curr]  
    
nums = Solution()
print(nums.subsets([4,3,2,1]))