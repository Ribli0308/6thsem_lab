#3. wap class to find the 3 elements that sum = 0from a set or array of n real numbers.
class Solution:
    def find3Elements(self, array):
        for i in range(len(array)):
            sum = array[i]
            for j in range(i + 1, len(array)):
                for k in range(j + 1, len(array)):
                    if sum + array[j] + array[k] == 0:
                        return array[i], array[j], array[k]
        return -1
    
sol = Solution()
print(sol.find3Elements([1,0,-3,8,0,-8]))