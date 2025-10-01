#pragma once
#include <iostream>

class ListNode{
    private:
        double val;
        ListNode* next;

    public:
        ListNode(double);
        int size();
        bool insertFront(double);
        bool insertBack(double);
        bool insertAt(int,double);
        double at(int);
        bool deletaAt(int);
        bool deleteByValue(double); //delete first occurence of value
        bool deleteAll(double); //delete all ocurences of value
        double popFront();
        double popBack();
        void clear();
};