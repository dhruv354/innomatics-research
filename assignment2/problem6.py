class Solution(object):
    def xorOperation(self, n, start):
        """
        :type n: int
        :type start: int
        :rtype: int
        """
        nums = [2*i + start for i in range(n)]
        output = 0
        for i in nums:
            output ^= i
        return output