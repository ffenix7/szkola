#include <iostream>
#include <vector>
#include <exception>

template <typename T>
class Stack{
public:
    int size();
    bool isEmpty();
    void push(T elem);
    T pop();
    T peek();
private:
    std::vector<T> stos;
};