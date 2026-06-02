class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        if (digits.size() == 0) {
            return {1};
        }
        if(digits[digits.size() - 1] != 9) {
            digits[digits.size() - 1]++;
            return digits;
        } else {
            digits.pop_back();
            vector<int> results = plusOne(digits);
            results.push_back(0);
            return results;
        }
        
        
    }
};
