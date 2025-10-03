if let n = readLine(), let num = Int(n){
    var last = 1;
    var last_last = 0;
    var arr: [Int] = []
    arr.append(last_last)
    arr.append(last)
    for _ in 1..<num-1{
        var temp = last_last + last;
        arr.append(temp)
        last_last = last
        last = temp
    }
    arr.reverse()
    for i in arr{
        print(i)
    }
}