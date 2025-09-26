class Solution:
    def arraySign(self, nums: List[int]) -> int:
        num = 1
        for i in range(len(nums)):
            num = num*nums[i]
        print(num)
        if num>0:
            return 1
        elif num<0:
            return -1
        return 0