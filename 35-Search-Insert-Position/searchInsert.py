class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        res = 0
        idx = 0
        for i in nums:
            # print(i)
            if i >= target:
                res = idx
                break
            else:
                idx += 1
                res = idx
        return res
