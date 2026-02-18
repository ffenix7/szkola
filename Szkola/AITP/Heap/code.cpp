#include "heap.hpp"

int Heap::extract_min(){
    if(heap.empty()){
        throw std::runtime_error("Heap is empty");
    }
    
    int min = heap[0];
    heap[0] = heap.back();
    heap.pop_back();
    heapify_down(0);
    return min;
}

void Heap::insert(int val){
    heap.push_back(val);
    heapify_up(heap.size() - 1);
}

void Heap::heapify_up(int index){
    while(index > 0){
        int parent = (index - 1) / 2;

        if(heap[index] < heap[parent]){
            std::swap(heap[index], heap[parent]);
            index = parent;
        } 
        else {
            break;
        }
    }
}

void Heap::heapify_down(int index){
    int smallest = index;
    int left = 2 * index + 1;
    int right = 2 * index + 2;

    if(left < heap.size() && heap[left] < heap[smallest]){
        smallest = left;
    }
    if(right < heap.size() && heap[right] < heap[smallest]){
        smallest = right;
    }
    if(smallest != index){
        std::swap(heap[index], heap[smallest]);
        heapify_down(smallest);
    }
}

int main(){
    Heap heap;
    heap.insert(1);
    heap.insert(5);
    heap.insert(10);
    heap.insert(20);
    std::cout << heap.extract_min() << std::endl;
    std::cout << heap.extract_min() << std::endl;
    return 0;
}