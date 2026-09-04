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
    int num;

    while(true){
        std::cout <<"Insert a number to look for:";
        std::cin >> temp;

        if(temp == "exit"){
            stream.close();
            return 0;
        }
        
        try {
            num = std::stoi(temp);
        } catch (const std::invalid_argument&) {
            std::cout << "Invalid input! Please enter a number." << std::endl;
            stream.close();
            return -1;
        }
    
        auto it = std::find(vec.begin(), vec.end(), num);
    
        if(it != vec.end()){
            std::cout << "Found: " << num << " at index: " <<  it - vec.begin() << '\n';
        }
        else{
            std::cout << "Couldnt find: " << num << '\n';
        }
    }
}

int main(){
    std::ifstream file("text.txt");
    if (!file.is_open()) {
        std::cout << "Cannot open file!" << std::endl;
        return 1;
    }

    int index = findIndex(file);

    return 0;
}