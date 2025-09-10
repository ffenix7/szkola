#include <iostream>
#include <vector>
#include <exception>

class Stack{
public:
    int size();
    bool isEmpty();
    void push(int elem);
    int pop();
    int peek();
private:
    std::vector<int> stos;
};


int Stack::size(){
    return stos.size();
}

bool Stack::isEmpty(){
    return stos.empty();
}

void Stack::push(int elem){
    stos.push_back(elem);
}

int Stack::pop(){
    if(isEmpty()){
        throw std::runtime_error("Stack is empty");
    }
    int val = stos.back();
    stos.pop_back();
    return val;
}

int Stack::peek(){
    if(isEmpty()){
       throw std::runtime_error("Stack is empty");
    }
    int size = stos.size();
    return stos[size-1];
}

int main(){
    Stack stos;
    stos.push(5);
    stos.push(7);
    std::cout<<stos.peek()<<'\n';   
    stos.pop();
    std::cout<<stos.peek();   
}