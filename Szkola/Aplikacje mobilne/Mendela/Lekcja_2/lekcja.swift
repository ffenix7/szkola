if let input = readLine(){
    let imie = String(input)
    if imie == "Kuba" || imie == "kuba" { print("M")}
    else if imie == "Barnaba" || imie == "barnaba" { print("M")}
    else if imie.last == "a"{ print("F")}
    else{ print("M")}
}
