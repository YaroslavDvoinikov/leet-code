class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if len(nums)==0 or len(nums)==1:
            return
        zero_count=0
        for i in range(len(nums)):
            if nums[i]==0:
                zero_count+=1
                continue
            if zero_count!=0:
                nums[i-zero_count] = nums[i]
        for i in range(zero_count):
            nums[-(i+1)] = 0
