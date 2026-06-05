class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        pref = 1
        res[0] = pref
        for i in range(1, len(nums)):
            pref *= nums[i - 1]
            res[i] *= pref
            

        suf = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= suf
            suf *= nums[i]

        return res