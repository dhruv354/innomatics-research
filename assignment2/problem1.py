class Solution(object):
    def defangIPaddr(self, address):
        output = ""
        i = 0
        while i < len(address):
            if address[i] == '.':
                output += '[.]'
            else:
                output += address[i]
            i += 1
        return output