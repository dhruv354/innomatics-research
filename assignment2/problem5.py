class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        temp1 = 1
        temp2 = 0
        n = str(n)
        for i in range(len(n)):
            temp1 *= int(n[i])
            temp2 += int(n[i])
        return temp1 - temp2
        