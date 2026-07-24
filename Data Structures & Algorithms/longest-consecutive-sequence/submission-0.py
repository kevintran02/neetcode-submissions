class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        store = set(nums)
        for i in nums:
            curr, count = i, 0
            while curr in store:
                count += 1
                curr += 1
            res = max(count, res)

        return res
            