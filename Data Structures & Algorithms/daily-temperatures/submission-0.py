class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []

        for i, t in enumerate(temperatures):
            while len(stack) != 0 and t > stack[-1][0]:
                stackIndex = stack.pop()[1]
                res[stackIndex] = i - stackIndex
            stack.append((t, i))
        
        return res

