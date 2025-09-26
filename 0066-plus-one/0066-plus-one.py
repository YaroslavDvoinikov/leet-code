class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        string = "".join(str(d) for d in digits)
        string = int(string)
        string+=1
        string = str(string)
        digits = [0]*len(string)
        for i in range(len(string)):
            digits[i] = int(string[i])
        return digits
