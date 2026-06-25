class Solution:
    def search(self, nums: List[int], target: int) -> int:
        pivot = self.findMinIndex(nums)
        result = self.binary_search(nums, 0, pivot - 1, target)
        if result != -1:
            return result
        return self.binary_search(nums, pivot, len(nums) - 1, target)
            

    
    def findMinIndex(self, nums: List[int]) -> int:
        minIndex = 0
        left, right = 0, len(nums) - 1

        while left <= right:
            if nums[left] < nums[right]:
                if nums[left] < nums[minIndex]:
                    minIndex = left
                break

            mid = (left + right) // 2

            if nums[mid] < nums[minIndex]:
                minIndex = mid

            if nums[mid] >= nums[left]:
                left = mid + 1
            else:
                right = mid - 1

        return minIndex

    def binary_search(self, nums: List[int], left: int, right: int, target: int) -> int:
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                return mid
        
        return -1
        