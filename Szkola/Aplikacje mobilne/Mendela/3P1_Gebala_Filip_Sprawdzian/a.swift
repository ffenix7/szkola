var tekst = ""

print("Podaj liczbe")
    if let input = readLine(){
        tekst = input
    }

var arr: [Int] = []
var flag = false
for i in tekst{
    if (i == "X"){
        flag = true
    }
    else{
        arr.append(Int(String(i))!)
    }
}


var sum = 0
let weights = [10,9,8,7,6,5,4,3,2]
for i in 0...8{
    let index_arr = arr.index(arr.startIndex, offsetBy: i)
    let index_weights = weights.index(weights.startIndex, offsetBy: i)
    sum += arr[index_arr] * weights[index_weights]
}

var modulo = sum % 11
var temp = 11 - modulo
var control = temp

if(temp == 11){
    control = 0
}
else if (temp == 10){
    control = -1
}
else{
    control = temp
}

let index = arr.index(before:arr.endIndex)

let control_first = arr[index]


if(Int(control_first) == control){
    print("Poprawny kod!")
} 
else if((control == -1) && flag == true){
    print("Poprawny kod!")
}
else{
    print("Niepoprawny kod!")
} 