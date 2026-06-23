class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxElement = -1
        for pile in piles:
            maxElement = max(maxElement, pile)
        
        high = maxElement
        low = 1
        minK = maxElement

        while low < high:
            k = low + (high - low) // 2
            totalHours = 0
            for i in range(len(piles)):
                totalHours += math.ceil(piles[i] / k)
            
            if totalHours > h:
                low = k + 1
            else:
                high = k
                minK = min(minK, k)

        return minK




    # Find largest element, m, in the array
    # Have high = m and low = 1 at the start
    # Find k by doing (high - low) / 2
    # Pass through the array and sum the times up
    #   by doing sum += ceil(piles[i] / k)
    # if sum > h make low = k and recalculate k
    # if sum <= h store that h in minK and make high = k and recalculate k
    # do until low >= high