#include "pk.hpp"

void PrioQue::enqueue(int num){
    queue.push_back(0); 
    int j = queue.size()-2; 
    
    while(j >= 0 && queue[j] > num){
        queue[j+1] = queue[j];
        j--;
    }
    
    queue[j+1] = num;
}

int PrioQue::dequeue(){
    if(queue.size()){
        int temp =  queue[queue.size()-1];
        queue.pop_back();
        return temp;
    }
    throw std::runtime_error("Cannot dequeue from empty queue!");
}

bool PrioQue::isEmpty(){
    if(queue.size()) return false;
    return true;
}

int PrioQue::size(){
    return queue.size();
}

int main(){
    PrioQue que;

    que.enqueue(7);
    que.enqueue(5);
    que.enqueue(1);
    std::cout<<que.dequeue()<< " "<< que.size();
}