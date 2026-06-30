class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right = 0, 0
        bestLength = 0
        charSet = set()

        for i in range(len(s)):
            if s[i] not in charSet:
                charSet.add(s[i])
                right += 1
            else:
                while s[i] in charSet:
                    charSet.discard(s[left])
                    left += 1
                    
                charSet.add(s[i])
                right += 1

            bestLength = max(bestLength, right - left)

        return bestLength

    
    