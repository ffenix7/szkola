#include <iostream>
#include <vector>
#include <string>
#include <fstream>
#include <algorithm>
#define INFINITY 1000000

std::vector<std::vector<std::pair<int, int>>> build_graph(std::fstream& input) {
    std::vector<std::vector<std::pair<int, int>>> graph;
    std::string line;

    while (std::getline(input, line)) {
        size_t colon_pos = line.find(':');
        int node = std::stoi(line.substr(0, colon_pos));
        std::vector<std::pair<int, int>> edges;
        size_t start = colon_pos + 1;
        while (start < line.size()) {
            size_t open = line.find('(', start);
            if (open == std::string::npos) break;

            size_t comma = line.find(',', open);
            size_t close = line.find(')', comma);
            
            if (comma == std::string::npos || close == std::string::npos) break;
            int neighbor = std::stoi(line.substr(open + 1, comma - open - 1));
            int weight = std::stoi(line.substr(comma + 1, close - comma - 1));
            edges.emplace_back(neighbor - 1, weight);
            start = close + 1;
        }
        graph.emplace_back(edges);
    }
    return graph;
}

std::vector<std::pair<int, int>> dijsktra(const std::vector<std::vector<std::pair<int, int>>>& graph) {
    if (graph.empty()) return {};
    std::vector<int> costs(graph.size(), INFINITY);
    std::vector<bool> visited(graph.size(), false);
    std::vector<int> prevs(graph.size(), -1);

    costs[0] = 0;

    for (auto _ : graph) {
        int min_cost = INFINITY;
        int min_index = -1;

        //find lowest cost unvisited node
        for (int i = 0; i < graph.size(); ++i) {
            if (!visited[i] && costs[i] < min_cost) {
                min_cost = costs[i];
                min_index = i;
            }
        }
        if (min_index == -1) break;
        visited[min_index] = true;

        //update costs for neighbors
        for (const auto& neighbor : graph[min_index]) {
            int neighbor_index = neighbor.first;
            int weight = neighbor.second;
            if (!visited[neighbor_index]) {
                int new_cost = costs[min_index] + weight;
                if (new_cost < costs[neighbor_index]) {
                    costs[neighbor_index] = new_cost;
                    prevs[neighbor_index] = min_index;
                }
            }
        }
    }
    
    std::vector<std::pair<int, int>> output;
    output.reserve(graph.size());
    for (int i = 0; i < graph.size(); ++i) {
        output.emplace_back(costs[i], prevs[i]);
    }
    return output;
}

int main(){
    std::fstream input("test_2.txt");
    if (!input.is_open()) {
        std::cerr << "Cannot open test_2.txt" << std::endl;
        return 1;
    }
    auto graph = build_graph(input);
    input.close();

    for(int i = 0; i < graph.size(); i++) {
        std::cout << "Node " << (i + 1) << ": ";
        for (const auto& edge : graph[i]) {
            std::cout << "(" << (edge.first + 1) << "," << edge.second << ") ";
        }
        std::cout << std::endl;
    }

    auto result = dijsktra(graph);

    for (int i= 0;i<result.size();i++) {
        std::cout <<"Node: "<< (i + 1) <<", Cost: " << result[i].first << ", Previous: " << (result[i].second == -1 ? -1 : result[i].second + 1) << std::endl;
    }

    return 0;
}