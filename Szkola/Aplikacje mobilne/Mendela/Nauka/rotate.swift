print("Podaj rozmiar tablicy: ")
var arr : [Int] = []

if let input = readLine(), let num = Int(input){
    for _ in 0..<num{
        print("Podaj liczbe: ")
        if let inputNum = readLine(), let new = Int(inputNum){
            arr.append(new)
        }
    }
}

while true{
    print("Podaj kierunek rotacji: ")
    if let direction = readLine() {
        print("Podaj liczbe rotacji: ")
        if let input = readLine(), let num = Int(input){
            for _ in 0..<num{
                if direction == "R"{
                    let temp = arr.removeLast()
                    arr.insert(temp, at: 0)
                }
                else{
                    let temp = arr.removeFirst()
                    arr.append(temp)
                }
            }
        } 
        else{
            break
        }
    }
    else{
        break
    }
    print(arr)
}
print(arr)