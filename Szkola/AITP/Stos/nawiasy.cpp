#include "stack_szablon.hpp"
#include <iostream>
#include <string>

template <typename T>
int Stack<T>::size(){
    return stos.size();
}

template <typename T>
bool Stack<T>::isEmpty(){
    return stos.empty();
}

template <typename T>
void Stack<T>::push(T elem){
    stos.push_back(elem);
}

template <typename T>
T Stack<T>::pop(){
    if(isEmpty()){
        throw std::runtime_error("Stack is empty");
    }
    T val = stos.back();
    stos.pop_back();
    return val;
}

template <typename T>
T Stack<T>::peek(){
    if(isEmpty()){
       throw std::runtime_error("Stack is empty");
    }
    return stos.back();
}

template <typename T>
bool check(std::string text){
    Stack<T> stos;
    size_t pos;

    std::string temp = "()[]{}";

    for (int i=0;i<text.size();i++){
        char cur = text[i];
        pos = temp.find(cur);

        if(pos == std::string::npos) continue;

        if(pos%2){
            if(stos.isEmpty()) return false;
            if(stos.peek() == temp[pos-1]){
                stos.pop();
            }
            else return false;
        }

        else stos.push(cur);
    }
    return stos.isEmpty();
}

int main(){
    std::string test = ")";
    std::cout<< check<char>(test);
    return 0;
}