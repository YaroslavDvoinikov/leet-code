class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i = 0
        j = len(nums)-1
        while i<=j:
            pivot = (i + j) // 2
            if target == nums[pivot]: return pivot
            if target < nums[pivot]:
                j = pivot - 1
            else:
                i = pivot + 1
        return -1
            