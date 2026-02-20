#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

int findIndex(std::ifstream &stream){
    std::vector<int> vec;
    std::string line;

    while(getline(stream, line)){
        vec.push_back(std::stoi(line));
        // std::cout << std::stoi(line) << '\n';
    }

    std::string temp;
    std::cout <<"Insert a number to look for:";
    std::cin >> temp;

    int num;
    try {
        num = std::stoi(temp);
    } catch (const std::invalid_argument&) {
        std::cout << "Invalid input! Please enter a number." << std::endl;
        return -1;
    }

    auto it = std::find(vec.begin(), vec.end(), num);

    if(it != vec.end()){
        return it - vec.begin();
    }
    else{
        stream.close();
        return -1;
    }
}

int main(){
    std::ifstream file("text.txt");
    if (!file.is_open()) {
        std::cout << "Cannot open file!" << std::endl;
        return 1;
    }

    int index = findIndex(file);
    std::cout << "Index: " << index << std::endl;

    file.close();
    return 0;
}