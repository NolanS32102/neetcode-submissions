class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        high = len(numbers) - 1
        low = 0

        while high > low:
            sumOf = numbers[high] + numbers[low]
            if sumOf > target:
                high -= 1
            elif sumOf < target:
                low += 1
            else:
                return [low + 1, high + 1]

        return [low + 1, high + 1]
        




# Use a low pointer at start and high pointer at end
# if num[high] + num[low] > tar move high down
# if num[high] + num[low] < tar move low up
# if equal to tar then return index of high and low added by 1