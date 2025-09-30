var arr: [Int] = [3,6,4,1,8,9,66,3,123,6,124,7,5]

for i in 0..<arr.count{
    for j in 0..<arr.count{
        let i_index = arr.index(arr.startIndex, offsetBy: i)
        let j_index = arr.index(arr.startIndex, offsetBy: j)
        if arr[i_index] < arr[j_index]{
            let temp = arr[j_index]
            arr[j_index] = arr[i_index]
            arr[i_index] = temp
        }
    }
}

for i in 0..<arr.count{
    let index = arr.index(arr.startIndex, offsetBy:i)
    print(arr[index])
}