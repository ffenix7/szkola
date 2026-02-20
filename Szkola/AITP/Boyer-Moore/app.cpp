#include <fstream>
#include <iostream>
#include <string>
#include <ctime>
#include <cstdlib>
#include <chrono>

using namespace std;

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

int boore_moore(std::string needle, std::string haystack){
    int needle_len = needle.length();
    int haystack_len = haystack.length();
    
    if(needle_len > haystack_len) return -1;
    
    int shift_table[256];
    
    for(int i=0;i<256;i++){
        shift_table[i] = needle_len;
    }
    
    for(int i=0;i<needle.length();++i){
        shift_table[needle[i]] = needle_len - i - 1;
    }
    shift_table[needle[needle_len-1]] = 1;
    
    // for(int i=0;i<256;i++){
        //     cout<<shift_table[i];
    // }
        
    for(int i=0;i<=haystack_len - needle_len; ++i){
        bool found = false;
        for(int j=needle_len-1;j>=0;j--){
            if(needle[j] == haystack[i+j]){
                found = true;
            } 
            else{
                i+=shift_table[haystack[j+i]] - 1;
                found = false;
                break;
            }
        }
        if(found) return i;
    }

    return -1;
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

bool expect_result(std::string needle, std::string haystack, int expect){
        int result = boore_moore(needle, haystack);
        return expect == result;
    }
    
int main(){
    using std::chrono::high_resolution_clock;
    using std::chrono::duration_cast;
    using std::chrono::duration;
    using std::chrono::milliseconds;
    srand(static_cast<unsigned int>(time(0)));
    // cout<<expect_result("dupa", "asddupa", 3)<<'\n';
    // cout<<expect_result("", "asddupa", -1)<<'\n';
    // cout<<expect_result("dupa", "", -1)<<'\n';
    // cout<<expect_result("varius", "Lorem ipsum dolor varius", 18)<<'\n';
    
    std::string filename = "text.txt";
    generateFile(100000000, "varius", filename);
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
        
                auto t3 = high_resolution_clock::now();
                std::cout<<'\n' << findPattern("varius", file_content);
                auto t4 = high_resolution_clock::now();
        
        auto t1 = high_resolution_clock::now();
        std::cout<<'\n' << boore_moore("varius", file_content);
        auto t2 = high_resolution_clock::now();
        
        file.close();
        auto ms_int_1 = duration_cast<milliseconds>(t2 - t1);
        auto ms_int_2 = duration_cast<milliseconds>(t4 - t3);

        std::cout << "Boore-Moore:" <<ms_int_1.count() << "ms\n";
        std::cout << "Naive:" <<ms_int_2.count() << "ms\n";

    }
    catch (const std::exception& e) {
        std::cerr << e.what() << std::endl;
    }
    return 0;
}