class Solution {
    /**
     * @param {number[]} nums
     * @return {number[][]}
     */
    threeSum(nums) {
        const answers = [];
        const seenNums = new Set();
        for (let i = 0; i < nums.length; i++) {
            for (let j = i + 1; j < nums.length; j++) {
                for (let k = j + 1; k < nums.length; k++) {
                    let sum = nums[i] + nums[j] + nums[k];
                    if (sum === 0 && !seenNums.has([nums[i], nums[j], nums[k]].sort().join(""))) {
                        seenNums.add([nums[i], nums[j], nums[k]].sort().join(""));
                        answers.push([nums[i], nums[j], nums[k]].sort());
                    }
                }
            }
        }
        return answers;
    }
}
