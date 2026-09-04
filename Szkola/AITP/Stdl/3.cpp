#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <algorithm>

enum Modes {
    mode_find,
    mode_less,
    mode_greater,
    mode_positions,
    mode_exit
};

std::vector<int> vec_reload(std::vector<int> &vec, std::ifstream &stream){
    std::string line;
    while(std::getline(stream, line)) {
        vec.push_back(std::stoi(line));
    }
    return vec;
}

void print_vec(std::vector<int> &vec){
    if(vec.size() == 0) std::cout << "[]";
    else std::cout << "[";
    for(int i = 0; i< vec.size(); i++){
        if(i != (vec.size() - 1)){
            std::cout << vec[i] << ", "; 
        }
        else{
            std::cout << vec[i]; 
        }
    }
    std::cout<< "]" << "\n";
}

std::string modeName(Modes mode){
    switch(mode) {
        case mode_find: return (std::string)"find";
        case mode_less: return (std::string)"less";
        case mode_greater: return (std::string)"greater";
        case mode_positions: return (std::string)"positions";
        case mode_exit: return (std::string)"exit";
        default: return (std::string)"unknown";
    }
}

int findIndex(std::ifstream &stream){
    std::vector<int> vec;
    std::string line;

    while(getline(stream, line)) {
        vec.push_back(std::stoi(line));
    }

    std::string temp;
    Modes currentMode = mode_find;

    while(true) {
        std::cout << "===== MENU =====" << std::endl;
        std::cout << "1. change command" << std::endl;
        std::cout << "2. number - find a number using current mode" << std::endl;
        std::cout << "current mode: " << modeName(currentMode) << std::endl;
        std::cout << "insert action: ";
        std::cin >> temp;

        if(temp == "1"){
            std::cout <<"Insert a command: ";
            std::cin >> temp;

            if(temp == "exit") {
                stream.close();
                return 0;
            } else if(temp == "find") {
                currentMode = mode_find;
            } else if(temp == "less") {
                currentMode = mode_less;
            } else if(temp == "greater") {
                currentMode = mode_greater;
            } else if(temp == "positions") {
                currentMode = mode_positions;
            } else if(temp == "reload") {
                stream.clear();
                stream.seekg(0);
                vec.clear();
                vec = vec_reload(vec, stream);
            } else if(temp == "print") {
                print_vec(vec);
            } else {
                std::cout << "Unknown command!" << std::endl;
                continue;
            }
            continue;
        }
        else if(temp=="2"){
            int num;
            std::cout << "Number: ";
            std::cin >> temp;

            try {
                num = std::stoi(temp);
            } catch (const std::invalid_argument&) {
                std::cout << "Invalid input!" << std::endl;
                continue;
            }

            switch(currentMode) {
                case mode_find: {
                    auto it = std::find(vec.begin(), vec.end(), num);
                    if(it != vec.end()) {
                        std::cout << "Found: " << num << " at index: " << it - vec.begin() << '\n';
                    } else {
                        std::cout << "Couldnt find: " << num << '\n';
                    }
                    break;
                }

                case mode_less: {
                    bool found = false;
                    auto it = vec.begin();
                    while ((it = std::find_if(it, vec.end(), [num](int x){ return x < num; })) != vec.end()) {
                        std::cout << *it << " at index: " << it - vec.begin() << '\n';
                        found = true;
                        ++it;
                    }
                    if(!found) std::cout << "No numbers less than " << num << '\n';
                    break;
                }

                case mode_greater: {
                    bool found = false;
                    auto it = vec.begin();
                    while ((it = std::find_if(it, vec.end(), [num](int x){ return x > num; })) != vec.end()) {
                        std::cout << *it << " at index: " << it - vec.begin() << '\n';
                        found = true;
                        ++it;
                    }
                    if(!found) std::cout << "No numbers greater than " << num << '\n';
                    break;
                }

                case mode_positions: {
                    bool found = false;
                    auto it = vec.begin();
                    while ((it = std::find_if(it, vec.end(), [num](int x){ return x == num; })) != vec.end()) {
                        std::cout << *it << " at index: " << it - vec.begin() << '\n';
                        found = true;
                        ++it;
                    }
                    if(!found) std::cout << "No numbers equal " << num << '\n';
                    break;
                }

                case mode_exit:
                    stream.close();
                    return 0;
            }
        }
        else{
            std::cout <<"Unkown command!" << std::endl;
            continue;
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