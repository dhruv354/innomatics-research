class Solution(object):
    def runningSum(self, nums):
        output = []
        for i in range(len(nums)):
            if i == 0:
                output.append(nums[i])
                continue
            output.append(output[i-1] + nums[i])
        return output