func returnInt(arr: [Any]) -> [Int]{
    var temp: [Int] = []
    for ele in arr{
        if type(of: ele) == Int.self{
            temp.append(ele as! Int)
        }
    }
    return temp as [Int] 
}
var temp = returnInt(arr: [1,2,3,4,5, "obama", 6 , 7, 8, 9, 10])

print(temp)