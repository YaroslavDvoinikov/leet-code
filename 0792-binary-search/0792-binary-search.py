class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i = 0
        j = len(nums)-1
        pivot = (i+j)//2
        if i == j:
            if target == nums[i]:
                return i
            return -1
        while i<=j:
            if target == nums[pivot]: return pivot
            if target < nums[pivot]:
                j = pivot - 1
                pivot = (i+j)//2
            else:
                i = pivot + 1
                pivot = (i+j)//2
        return -1
            