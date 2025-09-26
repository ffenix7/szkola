var arr: [Int] = []

print("Podaj dlugosc tablicy")
if let input = readLine(), let len = Int(input) {
    for _ in 0..<len {
        print("Podaj element tablicy")
        if let input = readLine(), let ele = Int(input) {
            arr.append(ele)
        }
    }
    print(arr)

    print("Podaj kierunek rotacji (L/P):")
    if let direction = readLine() {
        if direction == "L" || direction == "P"{
            print("Podaj liczbe rotacji:")
            if let input = readLine(), let num = Int(input){
                print(arr)
                for _ in 0..<num{
                    if direction == "L"{
                        let first = arr.removeFirst()
                        arr.append(first)
                    }
                    else if direction == "P"{
                        let last = arr.removeLast()
                        arr.insert(last, at:0)
                    }
                    print(arr)
                }
            }
        }
        else {
            print("Nieprawidłowy kierunek rotacji. Użyj 'L' lub 'P'.")
        }
        print("Zrotowana tablica: \(arr)")
}}
else {
    print("Nieprawidłowa długość tablicy.")
}