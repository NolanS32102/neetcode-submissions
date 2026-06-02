class Solution {
    /**
     * @param {number[][]} matrix
     * @param {number} target
     * @return {boolean}
     */
    searchMatrix(matrix, target) {
        const array = matrix.join(",").split(",");
        let lower = 0;
        let upper = array.length - 1;
        while (lower <= upper) {
            let mid = Math.floor(upper - lower);
            if (parseInt(array[mid]) === target) {
                return true;
            } else if (parseInt(array[mid]) > target) {
                upper = mid - 1;
            } else {
                lower = mid + 1;
            }
        }
        return false;
    }
}
