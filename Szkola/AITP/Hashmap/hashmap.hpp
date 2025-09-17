#include <iostream>
#include <vector>
#include "./Set/set.hpp"

class HashMap{
    public:
        bool insert(std::string, int);
        bool contains(std::string);
        bool erase(std::string);
        void clear();
        void print();
        int get_size();
        int get_value(std::string);
    
    private:
        size_t size = 10000;
        Set keys;
        std::vector<int> values;
};