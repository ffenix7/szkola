#include "ll.hpp"

LinkedList::LinkedList(std::initializer_list<double> l){
    this->head = nullptr;
    for (auto element: l){
        this->insertBack(element);
    }
}

ListNode::ListNode(double value){
    this->next = nullptr;
    this->val = value;
}

int LinkedList::size(){
    int size = 0;
    ListNode* cur = this->head;
    while(cur->next != nullptr){
        cur = cur->next;
        size++;
    }
    return size;
}

void LinkedList::insertFront(double num){
    ListNode* node = new ListNode(num);
    ListNode* old_head = this->head;
    this->head = node;
    node->next = old_head;
}

void LinkedList::insertBack(double num){
    ListNode* node = new ListNode(num);
    if (this->head == nullptr) {
        this->head = node;
        return;
    }
    ListNode* cur = this->head;
    while(cur->next != nullptr){
        cur = cur->next; 
    }
    cur->next = node;
}

void LinkedList::insertAt(int index, double num){
    if(index > this->size()) throw std::runtime_error("Index out of bounds!");
    if(index == this->size()) this->insertFront(num);

    ListNode* cur = this->head;
    int iterator = 0;
    while((cur->next != nullptr) && iterator<index - 1 ){
        cur = cur->next;
        iterator++;
    }
    ListNode* node = new ListNode(num);
    ListNode* temp = cur->next;
    cur->next = node;
    node->next = temp;
}

double LinkedList::at(int index){
    if(index > this->size()) throw std::runtime_error("Index out of bounds!");
    
    ListNode* cur = this->head;
    int iterator = 0;
    while((cur->next != nullptr) && iterator< index - 1 ){
        cur = cur->next;
        iterator++;
    }
    return cur->val;
}

bool LinkedList::deleteAt(int index) {
    if (index < 0 || index >= this->size()) throw std::runtime_error("Index out of bounds!");

    if (index == 0) {
        ListNode* temp = this->head;
        this->head = this->head->next;
        delete temp;
        return true;
    }

    ListNode* cur = this->head;
    int iterator = 0;
    while (cur->next != nullptr && iterator < index - 1) {
        cur = cur->next;
        iterator++;
    }
    if (cur->next == nullptr) return false; 

    ListNode* temp = cur->next;
    cur->next = temp->next;
    delete temp;
    return true;
}

bool LinkedList::deleteByValue(double num){
    ListNode* cur = this->head;
    if(cur==nullptr) throw std::runtime_error("Can't delete from an empty list!");
    
    if(this->head->val == num){
        ListNode* temp = this->head;
        this->head = head->next;
        delete temp;
        return true;
    }

    while (cur->next != nullptr && cur->next->val != num) {
        cur = cur->next;
    }

    if (cur->next == nullptr) return false; 

    ListNode* temp = cur->next;
    cur->next = temp->next;
    delete temp;
    return true;
}

bool LinkedList::deleteAll(double num) {
    if (this->head == nullptr) throw std::runtime_error("Can't delete from an empty list!");

    bool deleted = false;
    
    while (this->head != nullptr && this->head->val == num) {
        ListNode* temp = this->head;
        this->head = this->head->next;
        delete temp;
        deleted = true;
    }

    ListNode* cur = this->head;
    while (cur != nullptr && cur->next != nullptr) {
        if (cur->next->val == num) {
            ListNode* temp = cur->next;
            cur->next = temp->next;
            delete temp;
            deleted = true;
        } 
        else {
            cur = cur->next;
        }
    }
    return deleted;
}

double LinkedList::popFront(){
    double val = this->head->val;
    this->deleteAt(0);
    return val;
}

double LinkedList::popBack(){
    if (this->head == nullptr) throw std::runtime_error("Can't pop from empty list!");
    if (this->head->next == nullptr) {
        double val = this->head->val;
        deleteAt(0);
        return val;
    }
    ListNode* cur = this->head;
    while (cur->next->next != nullptr ) {
        cur = cur->next;
    }
    double val = cur->next->val;
    deleteAt(this->size() - 1);
    return val;
}

void LinkedList::clear() {
    while (this->head != nullptr) {
        ListNode* temp = this->head;
        this->head = this->head->next;
        delete temp;
    }
}

void LinkedList::print(){
    if(this->head==nullptr) return;
    ListNode* cur = this->head;
    while(cur != nullptr){
        std::cout<<cur->val<<" ";
        cur = cur->next;
    }
}

int main(){
    LinkedList lista = {1.1, 2.2, 3.3, 4.4};
    std::cout << "Rozmiar: " << lista.size() << std::endl;
    lista.insertFront(0.0);
    lista.insertBack(5.5);
    std::cout << "Po dodaniu na poczatek i koniec: " << lista.size() << std::endl;
    std::cout << "Element na indeksie 2: " << lista.at(2) << std::endl;
    lista.deleteByValue(2.2);
    std::cout << "Po usunięciu 2.2: " << lista.size() << std::endl;
    lista.deleteAt(0);
    std::cout << "Po usunięciu pierwszego: " << lista.size() << std::endl;
    lista.insertAt(2, 9.9);
    std::cout << "Po wstawieniu 9.9 na indeks 2: " << lista.at(2) << std::endl;
    std::cout << "PopFront: " << lista.popFront() << std::endl;
    std::cout << "PopBack: " << lista.popBack() << std::endl;
    lista.clear();
    std::cout << "Po czyszczeniu: " << lista.size() << std::endl;
    return 0;
}