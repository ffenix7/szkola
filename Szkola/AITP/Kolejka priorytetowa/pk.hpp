#pragma once
#include <iostream>
#include <vector>

class PrioQue{
    public:
        void enqueue(int num);
        int dequeue();
        bool isEmpty();
        int size();
    private:
        std::vector<int> queue;
};