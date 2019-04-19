class Solution {
    public int romanToInt(String s) {
        //conditions
        int value = 0;
        String last_char = "";
        
        for (char c : s.toCharArray()) {
            if (c == 'I' )
            {
                last_char = "I";
                value++;
            }
            else if (c == 'V')
            {
                if (last_char == "I"){
                    value += 3;
                }
                else{
                    value += 5;
                }
                last_char = "V";
            }
            else if (c == 'X')
            {
                if (last_char == "I"){
                    value += 8;
                }
                else{
                    value += 10;
                }
                last_char = "X";
            }
            else if (c == 'L')
            {
                if (last_char == "X"){
                    value += 30;
                }
                else{
                    value += 50;
                }
                last_char = "L";
            }
            else if (c == 'C')
            {
                if (last_char == "X"){
                    value += 80;
                }
                else{
                    value += 100;
                }
                last_char = "C";
            }
            else if (c == 'D')
            {
                if (last_char == "C"){
                    value += 300;
                }
                else{
                    value += 500;
                }
                last_char = "D";
            }
            else if (c == 'M')
            {
                if (last_char == "C"){
                    value += 800;
                }
                else{
                    value += 1000;
                }
                last_char = "M";
            }
        }
        return value;
    }
}
