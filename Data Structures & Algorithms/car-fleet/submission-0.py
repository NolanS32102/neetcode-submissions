class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        cars = sorted(list(zip(position, speed))) # cars: (pos, speed)
        stack = [cars[len(cars) - 1]]

        for i in range(len(cars) - 2, -1, -1):
            currTime = (target - cars[i][0]) / cars[i][1]
            topTime = (target - stack[-1][0]) / stack[-1][1]
            if currTime > topTime:
                stack.append(cars[i])
        
        return len(stack)
            


        