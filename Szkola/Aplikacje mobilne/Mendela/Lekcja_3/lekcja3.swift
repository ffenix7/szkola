import Darwin
var matrix: [[Int]] = []
var matrix2: [[Int]] = []

print("Podaj liczbę wierszy:")
if let input = readLine(), let rows = Int(input) {
    print("Podaj liczbę kolumn:")
    if let input = readLine(), let cols = Int(input) {
        for i in 0..<rows {
            var row: [Int] = []
            for j in 0..<cols {
                print("Podaj element [\(i)][\(j)]:")
                if let input = readLine(), let ele = Int(input) {
                    row.append(ele)
                } else {
                    print("Błąd: podaj liczbę całkowitą.")
                    exit(2)
                }
            }
            matrix.append(row)
        }
        print("Wprowadzona macierz:")
        print(matrix)
    }
}

print("Podaj liczbę wierszy macierzy 2:")
if let input = readLine(), let rows = Int(input) {
    print("Podaj liczbę kolumn macierzy 2:")
    if let input = readLine(), let cols = Int(input) {
        for i in 0..<rows {
            var row: [Int] = []
            for j in 0..<cols {
                print("Podaj element [\(i)][\(j)]:")
                if let input = readLine(), let ele = Int(input) {
                    row.append(ele)
                } else {
                    print("Błąd: podaj liczbę całkowitą.")
                    exit(2)
                }
            }
            matrix2.append(row)
        }
        print("Wprowadzona macierz:")
        print(matrix2)
    }
}

if matrix[0].count == matrix2.count{
    var result: [[Int]] = Array(repeating: Array(repeating: 0, count: matrix2[0].count), count: matrix.count)
    for i in 0..<matrix.count{
        for j in 0..<matrix2[0].count{
            for k in 0..<matrix[0].count{
                result[i][j] += matrix[i][k] * matrix2[k][j]
            }
        } 
    }
    print(result)
}
else{
    print("Nieprawidłowe rozmiary!")
    print("Macierz 1: \(matrix.count) na \(matrix[0].count)")
    print("Macierz 2: \(matrix2.count) na \(matrix2[0].count)")
}