class Solution {
    public boolean isAnagram(String s, String t) {
        Map<Character, Integer> seenSChars = new HashMap<>();
        Map<Character, Integer> seenTChars = new HashMap<>();
        if (s.length() != t.length()) {
            return false;
        }
        for (int i = 0; i < s.length(); i++) {
            seenSChars.put(s.charAt(i), seenSChars.getOrDefault(s.charAt(i), 0) + 1);
            seenTChars.put(t.charAt(i), seenTChars.getOrDefault(t.charAt(i), 0) + 1);
        }
        return seenSChars.equals(seenTChars);

    }
}
