#include <iostream>

bool check(long long a){
    if (a<0) return 0;

    if((a%3==0) || (a%8==0)) return 1;

    return check(a-3) || check(a-8);
}

int main(){
    long long x;
    std::cin >> x;

    bool out = check(x);

    std::cout << (out ? "TAK" : "NIE");
}