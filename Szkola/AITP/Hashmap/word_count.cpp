#include <iostream>
#include <string>
#include <unordered_map>
#include <sstream>

int count_words(std::unordered_map<std::string, int> map){
    long long sum = 0;
    for(const auto& num: map){
        sum+=num.second;
    }
    std::cout<<sum;
    return sum;
}

void word_count(std::string text) {
    std::unordered_map<std::string, int> map;
    std::stringstream ss(text);
    std::string temp;

    while(getline(ss, temp, ' ')){
        map[temp]++;
    }

    for (const auto& pair : map) {
        std::cout << pair.first << ": " << pair.second << std::endl;
    }

    count_words(map);
}


int main(){
    word_count("banan banan banan marchew");
}