if let input = readLine(), let n = Int(input) {
    var result = 1
    if n < 0{
        print("Nie mozna liczyć silni dla liczb ujemnych")
    }
    else{
        for i in 1...n{
            result*=i
        }
        print("Silnia z \(n) wynosi \(result)")
    }
} else {
    print("Niepoprawne dane")
}