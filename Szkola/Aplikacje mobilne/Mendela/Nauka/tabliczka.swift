if let input = readLine(), let num = Int(input){
    for i in 1...num{
        for j in 1...num{
            print("\(i*j)", terminator: " ")
        }
        print("\n")
    }
}