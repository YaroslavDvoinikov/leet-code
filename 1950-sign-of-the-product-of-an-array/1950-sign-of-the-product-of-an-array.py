class Solution(object):
    def arraySign(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        neg_count = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                return 0
            if nums[i] < 0:
                neg_count += 1
        if neg_count%2 == 0:
            return 1
        return -1
