class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> differences = new HashMap<>();
        Map<Integer, Integer> indexMap = new HashMap<>();
        int[] indicies = new int[2];
        for (int i = 0; i < nums.length; i++) {
            int complement = target - nums[i];
            if (indexMap.containsKey(complement)) {
                indicies[0] = indexMap.get(complement);
                indicies[1] = i;
                return indicies;
            }
            indexMap.put(nums[i], i);
            differences.put(nums[i], complement);
        }
        return indicies;
        
    }
}