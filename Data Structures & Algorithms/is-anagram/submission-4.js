class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {
        const sArray = s.split("");
        const tArray = t.split("");
        sArray.sort();
        tArray.sort();
        const sortedS = sArray.join("");
        const sortedT = tArray.join("");
        if (sortedS === sortedT) {
            return true;
        }
        return false;
    }
}
