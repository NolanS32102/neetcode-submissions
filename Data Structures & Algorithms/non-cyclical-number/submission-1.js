class Solution {
    /**
     * @param {number} n
     * @return {boolean}
     */
    isHappy(n) {
        const seenNums = new Set();
        let sumOfDigits = 0;
        let num = n;
        while (sumOfDigits !== 1) {
            sumOfDigits = 0;
            while (num !== 0) {
                let digit = num % 10;
                sumOfDigits += Math.pow(digit, 2);
                num = Math.floor(num / 10);
            }
            if (seenNums.has(sumOfDigits)) {
                return false;
            }
            seenNums.add(sumOfDigits);
            num = sumOfDigits;
        }
        return true;
    }
}
