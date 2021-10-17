class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        output = []
        for i in range(len(nums)):
            temp = 0
            for j in range(len(nums)): 
                if j != i and nums[j] < nums[i]:
                    temp += 1
            output.append(temp)
        return output
            
        