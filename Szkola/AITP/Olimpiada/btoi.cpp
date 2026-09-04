#include <iostream>
#include <vector>

int main(){

    int n;
    std::cin >> n;
    std::vector<int> present(8,0);

    for (int i=0;i<n;++i){
        int s,i2,m;
        std::cin >> s >> i2 >> m;
        int mask = (s<<2) | (i2<<1) | m;
        present[mask]=1;
    }

    bool changed = true;
    
    while(changed){
        changed = false;
        for(int a=0;a<8;++a) 
            if(present[a]){
                for(int b=0;b<8;++b) if(present[b]){
                    int s1=(a>>2)&1, i1=(a>>1)&1, m1=a&1;
                    int s2=(b>>2)&1, i2=(b>>1)&1, m2=b&1;
                    int s = s1 ^ s2;
                    int i_ = i1 & i2;
                    int m_ = m1 | m2;
                    int mask = (s<<2) | (i_<<1) | m_;
                    if(!present[mask]){ present[mask]=1; changed=true; }
                }
        }
    }

    int ans=0;
    for(int x=0;x<8;++x) ans += present[x];
    std::cout << ans << '\n';

    return 0;
}