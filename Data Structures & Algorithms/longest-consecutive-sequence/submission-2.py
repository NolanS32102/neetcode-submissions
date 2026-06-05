class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longestStreak = 0

        for num in numSet:
            if (num - 1) not in numSet:
                currStreak = 1
                while (num + currStreak) in numSet:
                    currStreak += 1
                longestStreak = max(longestStreak, currStreak)

        return longestStreak 


        