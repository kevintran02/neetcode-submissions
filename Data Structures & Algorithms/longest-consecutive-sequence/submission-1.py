class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        store = set(nums)
        for n in nums: 
            if (n-1) not in store:
                length = 0
                while (n+length) in store:
                    length +=1
                res = max(length, res)
        return res