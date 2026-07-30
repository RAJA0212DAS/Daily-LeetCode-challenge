class Solution {
public:
    int minimumPushes(string word) {
        int n = word.length();
        if(word.length() <= 8){
            return n;
        }
        if(word.length() == 9){
            return 10;
        }
        if(word.length() == 10){
            return 12;
        }
        if(word.length() == 11){
            return 14;
        }
        if(word.length() == 12){
            return 16;
        }
        if(word.length() == 13){
            return 18;
        }
        if(word.length() == 14){
            return 20;
        }
        if(word.length() == 15){
            return 22;
        }
        if(word.length() == 16){
            return 24;
        }
        if(word.length() == 17){
            return 27;
        }
        if(word.length() == 18){
            return 30;
        }
        if(word.length() == 19){
            return 33;
        }
        if(word.length() == 20){
            return 36;
        }
        if(word.length() == 21){
            return 39;
        }
        if(word.length() == 22){
            return 42;
        }
        if(word.length() == 23){
            return 45;
        }
        if(word.length()== 24){
            return 48;
        }
        if(word.length() == 25){
            return 52;
        }
        return 56;



    }
};