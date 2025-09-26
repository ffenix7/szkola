import Darwin
if let input = readLine() {
    if input.count != 11 {
        print("Nieprawidlowa dlugosc")
    }
    
    var suma = 0
    
    for index in 0..<10 {
        let cyfra = input[input.index(input.startIndex, offsetBy: index)]
        let wagi: [Int] = [1,3,7,9,1,3,7,9,1,3,1]
        if cyfra.isNumber == true{
            if let cyfraInt = Int(String(cyfra)) {
                suma += cyfraInt * wagi[index]
            }
        }
        else{
            print("Niepoprawny pesel!")
            exit(2)
        }
    }

    let m = suma % 10
    if m==0 && Int(String(input.last!)) == 0{
        print("Pesel poprawny!")
    }
    else{
        let temp = 10 - m
        if temp == Int(String(input.last!)) {
            print("Pesel poprawny")
        } 
        else {
            print("Pesel niepoprawny")
        }
    }
    if Int(String(input[input.index(input.startIndex, offsetBy:9)]))! % 2 == 0{
    print("Kobieta")
    }

    else{
        print("Męzczyzna")
    }
}

