func silnia(_ n:Int) -> Int{
    if n == 0 || n == 1 {
        return 1
    }
    return silnia(n-1) * n
}

print(silnia(20))