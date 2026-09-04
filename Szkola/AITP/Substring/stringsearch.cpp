#include <fstream>
#include <iostream>
#include <string>
#include <ctime>
#include <cstdlib>

char random(){
    return static_cast<char>(32 + rand() % (127 - 32));
}

void generateFile(long long len=100000, std::string key="", std::string filename="text.txt"){
    len -= key.length();
    if (len < 0) len = 0;

    long long key_idx = rand() % (len + 1);

    std::fstream file(filename, std::ios::out);
    for(long long i = 0; i < key_idx; i++) {
        file << random();
    }
    file << key;
    for(long long i = key_idx; i < len; i++) {
        file << random();
    }
    file.close();
}

int findPattern(const std::string& needle, const std::string& haystack) {
    if (needle.empty() || haystack.length() < needle.length()) return -1;

    for(int i=0; i<=haystack.length() - needle.length(); i++){
        bool match = true;
        for(int j=0;j<needle.length(); j++){
            if(haystack[i+j]!=needle[j]){
                match = false;
                break;
            }
        }
        if(match) return i;
    }
    return -1;
}

int main()
{
    srand(static_cast<unsigned int>(time(0)));
    std::string filename = "text.txt";
    generateFile(1024*1024*1024, "dupa", filename);
    try {
        std::fstream file(filename, std::ios::in);
        if (file.is_open()) {
            std::cout << "Success!\n";
        } else {
            throw std::runtime_error("File is not open! ");
        }

        std::string file_content;
        std::string temp;
        while(std::getline(file, temp)){
            file_content+=temp;
        }
        
        std::cout<<'\n' << findPattern("dupa", file_content);

        file.close();
    }
    catch (const std::exception& e) {
        std::cerr << e.what() << std::endl;
    }
}