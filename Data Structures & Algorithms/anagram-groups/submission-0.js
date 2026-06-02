class Solution {
    /**
     * @param {string[]} strs
     * @return {string[][]}
     */
    groupAnagrams(strs) {
        const anagramMap = new Map();
        const sortedStrs = [];
        const answers = [];
        for (let i = 0; i < strs.length; i++) {
            let sortedStr = strs[i].split('').sort().join("");
            if (!anagramMap.has(sortedStr)) {
                anagramMap.set(sortedStr, []);
                sortedStrs.push(sortedStr);
            }
            anagramMap.get(sortedStr).push(strs[i]);
        }

        for (const str of sortedStrs) {
            answers.push(anagramMap.get(str));
        }
        return answers;
    }
}
