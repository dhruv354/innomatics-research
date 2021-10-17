class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hm = {}
        count = 0
        
        for i,n in enumerate(nums):
            if n not in hm:
                hm[n] = [i]
            else:
                for x in range(len(hm[n])):
                    count += 1
                hm[n].append(i)
        return count