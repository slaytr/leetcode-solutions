#Problem 9
class Solution {
    public boolean isPalindrome(int x) {
        String str_x = Integer.toString(x);
        for (int i = 0; i < str_x.toCharArray().length; i++){ 
            if (str_x.toCharArray()[i] != str_x.toCharArray()[str_x.toCharArray().length-(i+1)]) return false;
        }
        return true;
    }
}