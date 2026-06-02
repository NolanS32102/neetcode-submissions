class Solution {
    public boolean isPalindrome(String s) {
        String newStr = s.replaceAll(" ", "").replaceAll("\\p{Punct}", "").toLowerCase();
        System.out.println(newStr);
        for (int i = 0; i < newStr.length() / 2; i++) {
            if (newStr.charAt(i) != newStr.charAt(newStr.length() - 1 - i)) {
                return false;
            }
        }
        return true;
    }
}
