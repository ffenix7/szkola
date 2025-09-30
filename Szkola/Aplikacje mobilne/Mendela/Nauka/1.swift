if let input: String = readLine(){
    let half: Int = input.count / 2
    var flag = false
    print(half)
    
    if((input.count % 2) != 0 ){
        for i in 0..<half{
            let left = input[input.index(input.startIndex, offsetBy: i)]
            let right = input[input.index(input.endIndex, offsetBy: -(i+1))]
            print("left: \(left), right: \(right)")
            if(input[input.index(input.startIndex, offsetBy: i)] == input[(input.index(input.endIndex,offsetBy:-(i+1)))]){
                continue
            }
            else{
                print("Nie palindrom!")
                flag = true
                break
            }
        }
        if (flag == false){
            print("Palindrom!")
        }
    }
    else{
        for i in 0...half{
            let left = input[input.index(input.startIndex, offsetBy: i)]
            let right = input[input.index(input.endIndex, offsetBy: -(i+1))]
            print("left: \(left), right: \(right)")
            if(input[input.index(input.startIndex, offsetBy: i)] == input[(input.index(input.endIndex,offsetBy:-(i+1)))]){
                continue
            }
            else{
                print("Nie palindrom!")
                flag = true
                break
            }
        }
        if (flag == false){
            print("Palindrom!")
        }
    }
}