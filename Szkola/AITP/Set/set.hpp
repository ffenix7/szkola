#pragma once 
#include <iostream>
#include <vector>

class Set{
    public:
        bool insert(int liczba);
        bool contains(int liczba) const;
        bool remove(int liczba);
        bool clear();
        int size();
        bool isEmpty();
        void print();
        friend Set operator+(const Set& a, const Set& b);
        friend Set operator-(const Set& a, const Set& b);
        friend Set operator*(const Set& a, const Set& b);
        int operator[](int idx) const { return zbior[idx]; }
    private:
        std::vector<int> zbior;
        size_t rozmiar;
};