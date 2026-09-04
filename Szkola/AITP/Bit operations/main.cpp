#include <iostream>
#include <string>

int fromBinaryString(std::string x) {
    int result = 0;
    for (int i = 0; i < x.length(); i++) {
        if (x[i] == '1') {
            result += 1 << (x.length() - 1 - i);
        }
    }
    return result;
}

std::string toBinaryString(int x){
    if (x == 0) return "0";
    
    std::string result = "";
    bool leadingZero = true;
    
    for(int i = 31; i >= 0; --i) { 
        bool bit = ((x & (1 << i)) != 0);
        if (bit) leadingZero = false;
        
        if (!leadingZero) {
            result += bit ? '1' : '0';
        }
    }
    return result;
}

int main(){

    std::cout<< toBinaryString(2147483647);
    //std::cout << fromBinaryString("1111");
}