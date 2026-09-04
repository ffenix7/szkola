func szyfr(_ char : Character) -> String{
    if(char == " "){
        return String(0)
    }
    var val = Int(char.asciiValue!)
    val = val - 97
    var position_1 = val / 3
    position_1 += 2
    var postion_2 = val % 3 + 1
    
    if(position_1 >= 8){
        postion_2 -= 1
        if(postion_2 <= 0){
            position_1 -= 1
            if(position_1 == 7){
                postion_2 = 4
            }
            else{
                postion_2 = 3
            }
        }
    }
    if (position_1 == 10){
        position_1 = 9
        postion_2 = 4
    }

    var out = " "

    for _ in 0 ..< postion_2{
        out += String(position_1)
    }
    return out
}

if let input = readLine(){
    var out = ""
    for num in input{
        out += szyfr(num)
    }
    print(out)
}