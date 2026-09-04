#pragma once
#include <iostream>
#include <vector>

class Heap{
    public:
        int extract_min();
        void insert(int val);
    private:
        std::vector<int> heap;
        void heapify_up(int index);
        void heapify_down(int index);
};