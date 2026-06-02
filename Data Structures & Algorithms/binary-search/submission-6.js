class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number}
     */
    search(nums, target) {
        let upperIndex = nums.length - 1;
        let lowerIndex = 0;
        while(lowerIndex <= upperIndex) {
            let midIndex = Math.floor(lowerIndex + (upperIndex - lowerIndex) / 2)
            if (nums[midIndex] === target) {
                return midIndex;
            } else if (nums[midIndex] > target) {
                upperIndex = midIndex - 1;
            } else {
                lowerIndex = midIndex + 1;
            }
        }
        return -1;
    }
}
