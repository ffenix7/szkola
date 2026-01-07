#include <iostream>
#include <vector>
#include <string>

std::vector<std::pair<int, std::vector<int>>> build_graph(std::vector<std::string> input){
    //1: 2,3
    //2: 1,4
    std::vector<std::pair<int, std::vector<int>>> graph;
    for(const auto& line : input){
        size_t colon_pos = line.find(":");
        int node = std::stoi(line.substr(0, colon_pos));
        std::vector<int> edges;
        size_t start = colon_pos + 1;
        while (start < line.size()){
            size_t comma_pos = line.find(",", start);
            size_t edge_pos = (comma_pos > line.size()) ? line.size() : comma_pos;
            edges.push_back(std::stoi(line.substr(start, edge_pos - start)));
            start = edge_pos + 1;
        }
        graph.push_back({node, edges});
    }
    return graph;
}


int main(){
    std::vector<std::string> input = {
        "1:2,3",
        "2:1,4",
        "3:1",
        "4:2"
    };

    auto graph = build_graph(input);

    for(const auto& [node, edges] : graph){
        std::cout << "Node " << node << " has edges to: ";
        for(const auto& edge : edges){
            std::cout << edge << " ";
        }
        std::cout << std::endl;
    }

    return 0;
}