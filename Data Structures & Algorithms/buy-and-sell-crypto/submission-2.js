class Solution {
    /**
     * @param {number[]} prices
     * @return {number}
     */
    maxProfit(prices) {
        //loop backwards and find smallest value

        let maxProfit = 0;
        for (let i = prices.length - 1; i >= 0; i--) {
            for (let j = 0; j < i; j++) {
                let currProfit = prices[i] - prices[j];
                if (currProfit > maxProfit) {
                    maxProfit = currProfit;
                }
            }
        }
        return maxProfit;
    }
}
