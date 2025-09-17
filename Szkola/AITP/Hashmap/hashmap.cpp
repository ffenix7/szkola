#include "hashmap.hpp"
#include <cstdint>

uint32_t fnv1a_hash(const std::string& str) {
    const uint32_t FNV_prime = 16777619u;
    const uint32_t offset_basis = 2166136261u;

    uint32_t hash = offset_basis;
    for (char c : str) {
        hash ^= static_cast<uint8_t>(c);
        hash *= FNV_prime;
    }
    return hash;
}

bool HashMap::insert(std::string word, int num){
    uint32_t hash = fnv1a_hash(word);
    if(keys.insert(hash)%size){
        values[hash%size] = num;
        return true;
    }
    return false;
}

bool HashMap::contains(std::string word){
    uint32_t hash = fnv1a_hash(word);
    if(keys.contains(hash)%size) return true;
    return false;
}

bool HashMap::erase(std::string word){
    uint32_t hash = fnv1a_hash(word);

    if(keys.contains(hash%size)){
        keys.remove(hash%size);
        values.erase(values.begin() + hash%size);
        return true;
    }
    return false;
}

void HashMap::clear(){
    keys.clear();
    values.erase(values.begin(), values.end());
    return ;
}

void HashMap::print(){

}

int main(){
    
}