#pragma once
#include <iostream>

class ListNode {
    public:
        double val;
        ListNode* next;

    ListNode(double value);
};

class LinkedList {
private:
    ListNode* head;
public:
    LinkedList(std::initializer_list<double>);
    void insertFront(double);
    void insertBack(double);
    void insertAt(int, double);
    double at(int);
    bool deleteAt(int);
    bool deleteByValue(double); //delete first occurence of value
    bool deleteAll(double); //delete every occurence of value
    double popFront();
    double popBack();
    void clear();
    int size();
    void print();
};