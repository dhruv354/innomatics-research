class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        
        temp = max(candies)
        # print(temp)
        output = []
        for i in candies:
            # print(i + extraCandies)
            if (i + extraCandies) >= temp:
                print(i+extraCandies, temp)
                output.append("true")
            else:
                output.append("false")
        return output
        