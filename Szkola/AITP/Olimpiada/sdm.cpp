#include <iostream>

bool check(long long x, int a, int b){
    int smaller = std::min(a,b);
    int bigger = std::max(a,b);

    while(x>0){
        x -= smaller;
        if (x%bigger==0) return 1;
    }
    if (x==0) return 1;
    return 0;
}

int main(){
    long long t;
    std::cin >> t;

    for (int i=0;i<t;++i){
        int a,b,x;
        std:: cin >> a >> b >> x;
        if((x%a==0) || (x%b==0)){
            std::cout << "TAK" << '\n';
            continue;
        }
        bool out = check(x, a, b);
        std::cout << (out ? "TAK" : "NIE") << '\n';
    }

}