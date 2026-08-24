#include <iostream>
#include <vector>
#include <string>
#include <queue>


int main() {
    int n, m;
    std::cin >> n >> m;

    std::vector<std::string> grid(n);
    for (int i = 0; i < n; ++i) std::cin >> grid[i];

    std::vector<char> visited(n * m, 0);
    auto id = [m](int row, int col) { return row * m + col; };

    int islands = 0;
    std::queue<std::pair<int, int>> queue;

    for (int row = 0; row < n; ++row) {
        for (int col = 0; col < m; ++col) {

            if (grid[row][col] != '1' || visited[id(row, col)]) continue;

            ++islands;
            visited[id(row, col)] = 1;
            queue.push({row, col});

            while (!queue.empty()) {
                auto [x, y] = queue.front();
                queue.pop();

                int up = (x - 1 + n) % n;
                int down = (x + 1) % n;
                int left = (y - 1 + m) % m;
                int right = (y + 1) % m;

                const int nr[4] = {up, down, x, x};
                const int nc[4] = {y, y, left, right};

                for (int k = 0; k < 4; ++k) {
                    int nx = nr[k], ny = nc[k];
                    int idx = id(nx, ny);
                    if (!visited[idx] && grid[nx][ny] == '1') {
                        visited[idx] = 1;
                        queue.push({nx, ny});
                    }
                }
            }
        }
    }

    std::cout << islands << '\n';
    return 0;
}