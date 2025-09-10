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
Stack<T> reverse(Stack<T> stos){
    Stack<T> new_stos;
    while(!stos.isEmpty()){
        T val = stos.pop();
        new_stos.push(val);
    }
    return new_stos;
}

int main(){
    Stack<char> stos;
    stos.push('a');
    stos.push('c');
    Stack<char> new_stack = reverse(stos);
    std::cout<<new_stack.peek();

}