#include <iostream>
#include <vector>
#include <string>
#include <fstream>
#include <algorithm>

std::vector<std::pair<int, std::vector<int>>> build_graph(std::fstream& input){
    std::vector<std::pair<int, std::vector<int>>> graph;
    std::string line;
    
    while(std::getline(input, line)){
        std::cout<<line<<std::endl;
        size_t colon_pos = line.find(':');
        int node = std::stoi(line.substr(0, colon_pos));
        std::vector<int> edges;
        size_t start = colon_pos + 1;
        size_t comma_pos = line.find(',', start);
        while(comma_pos != std::string::npos){
            edges.push_back(std::stoi(line.substr(start, comma_pos - start)));
            start = comma_pos + 1;
            comma_pos = line.find(',', start);
        }
        if(start < line.size()){
            edges.push_back(std::stoi(line.substr(start)));
        }
        graph.emplace_back(node, edges);
    }
    return graph;
}

void dfs_recursive(const std::vector<std::pair<int, std::vector<int>>>& graph, int current_node, std::vector<int>& visited) {
    if (std::find(visited.begin(), visited.end(), current_node) != visited.end()) {
        return;
    }

    visited.push_back(current_node);

    for (const auto& [node, edges] : graph) {
        if (node == current_node) {
            for (const auto& edge : edges) {
                dfs_recursive(graph, edge, visited);
            }
            break;
        }
    }
}

std::vector<int> dfs(const std::vector<std::pair<int, std::vector<int>>>& graph, int start_node = 1) {
    std::vector<int> visited;
    dfs_recursive(graph, start_node, visited);
    return visited;
}

bool check_results(std::vector<std::pair<int, std::vector<int>>> gt, std::vector<int> visited){
    for(auto& [node,edges] : gt){
        if(std::find(visited.begin(), visited.end(), node) == visited.end()) return false;
    }
    return true;
}


int main(){
    std::fstream input("dfs_1.txt", std::ios::in);

    std::vector<std::pair<int, std::vector<int>>> graph = build_graph(input);

    std::vector<int> dfs_out = dfs(graph);

    bool result = check_results(graph, dfs_out);
    std::cout << result <<std::endl;

    return 0;
}