if let input = readLine() {
    let slowo = input 
    var szyfr = ""

    for index in stride(from: 0, to: slowo.count, by: 2) {
        let stringIndex = slowo.index(slowo.startIndex, offsetBy: index)
        szyfr += String(slowo[stringIndex])
    }

    for index in stride(from: 1, to: slowo.count, by: 2) {
        let stringIndex = slowo.index(slowo.startIndex, offsetBy: index)
        szyfr += String(slowo[stringIndex])
    }

    print(szyfr)
}