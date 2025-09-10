#include "set.hpp"

bool Set::isEmpty(){
    return zbior.empty();
}

bool Set::insert(int liczba){
    for(int i=0;i<zbior.size();i++){
        if(zbior[i] == liczba) return false;
    }
    zbior.push_back(liczba);
    return true;
}

bool Set::contains(int liczba) const{
    for(int i=0;i<zbior.size();i++){
        if(zbior[i] == liczba) return true;
    }
    return false;
}

bool Set::remove(int liczba){
    for(int i = 0; i < zbior.size(); i++){
        if(zbior[i] == liczba){
            zbior.erase(zbior.begin() + i);
            return true;
        }
    }
    return false;
}

int Set::size(){
    return zbior.size();
}

bool Set::clear(){
    if (zbior.size() == 0) return false;
    zbior.erase(zbior.begin(), zbior.end());
    return true;
}

void Set::print(){
    for(int i=0;i<zbior.size();i++){
        std::cout<<zbior[i]<<" ";
    }
    std::cout<<"\n";
}

Set operator+(const Set& a, const Set& b) {
    Set result = a;
    for (const auto& elem : b.zbior) {
        result.insert(elem);
    }
    return result;
}

Set operator -(const Set& a, const Set& b){
    Set result = a;

    for(const auto& elem: b.zbior){
        result.remove(elem);
    }
    return result;
}

Set operator *(const Set& a, const Set& b){
    Set result;
        for(int i=0;i<a.zbior.size();i++){
            if(b.contains(a.zbior[i])){
                result.insert(a.zbior[i]);
            }
        }
    return result;
}

bool isSubsetOf(Set& a, Set& b){
    for(int i=0;i<a.size();i++){
        if(b.contains(a[i])) continue;
        else return false;
    }
    return true;
}

int main(){
    Set test;
    Set test2;

    test.insert(5);
    test.insert(7);
    test.insert(3);
    
    test2.insert(2);
    test2.insert(3);
    test2.insert(10);
    test2.insert(7);
    test2.remove(3);

    test = test * test2;
    test.print();
}