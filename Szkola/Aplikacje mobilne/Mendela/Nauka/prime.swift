import Foundation

func divisors(_ n:Int) -> [Int]{
    var arr = [Int]()
    let limit = Int(sqrt(Double(n)))
    for i in 1...limit{
        if n % i == 0{
            arr.append(i)
            if (n/i) != i {
                arr.append(n/i)
            }
        }
    }
    return arr.sorted()
}

func isPrime(_ n: Int) -> Bool{
    if n < 2{
        return false
    }
    return divisors(n).count == 2
}



if let input = readLine(), let n = Int(input){
    print(isPrime(n))
}