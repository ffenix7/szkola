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

std::vector<int> bfs(const std::vector<std::pair<int, std::vector<int>>>& graph, int start_node = 6){
    std::vector<int> visited;
    std::vector<int> queue;
    queue.push_back(start_node);

    while(!queue.empty()){
        int current_node = queue.front();
        queue.erase(queue.begin());

        if(std::find(visited.begin(), visited.end(), current_node) == visited.end()){
            visited.push_back(current_node);
            
            for(const auto& [node, edges] : graph){
                if(node == current_node){
                    for(const auto& edge : edges){
                        if(std::find(visited.begin(), visited.end(), edge) == visited.end()){
                            queue.push_back(edge);
                        }
                    }
                    break;
                }
            }
        }
    }
    return visited;
}

bool check_results(std::vector<std::pair<int, std::vector<int>>> gt, std::vector<int> visited){
    for(auto& [node,edges] : gt){
        if(std::find(visited.begin(), visited.end(), node) == visited.end()) return false;
    }
    return true;
}


int main(){
    std::fstream input("bfs.txt", std::ios::in);

    std::vector<std::pair<int, std::vector<int>>> graph = build_graph(input);

    std::vector<int> bfs_out = bfs(graph);

    for(int i=0;i<bfs_out.size(); i++){
        std::cout<<bfs_out[i]<<std::endl;
    }

    bool result = check_results(graph, bfs_out);
    std::cout << result <<std::endl;

    return 0;
}