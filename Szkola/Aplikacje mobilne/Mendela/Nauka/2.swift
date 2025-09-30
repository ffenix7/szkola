let random = Int.random(in: 1...100)

print("Guess the number between 1 and 100. You have 5 attempts.")

for _ in 0..<5{
    if let input = readLine(), let num=Int(input){
        if num < random{
            print("Too low!")
        }
        else if num > random{
            print("Too high!")
        }
        else{
            print("Congratulations! You've guessed the number!")
            break
        }
    }
}