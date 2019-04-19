#Problem 7
class Solution {
    public int reverse(int x) {
        boolean isNegtive = false;
        if (x < 0) {
            isNegtive = true;
            x = -x;
        }
        long y = 0;
        while (x > 0) {
            y *= 10;
            y += x % 10;
            x /= 10;
        }
        
        if (isNegtive) y = -y;
        if (y < Integer.MIN_VALUE || y > Integer.MAX_VALUE) return 0;

        return (int) y;
    }
}