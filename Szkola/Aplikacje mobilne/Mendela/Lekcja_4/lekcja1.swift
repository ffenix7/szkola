var stack : Set<String> = []
var symbols = ["♠️", "♥️", "♦️", "♣️"]
var values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

print(stack)

func recreate_stacks(){
    stack.removeAll()
    for symbol in symbols{
        for value in values{
            let card = "\(value)\(symbol)"
            stack.insert(card)
        }
    }
    player_stack.removeAll()
    computer_stack.removeAll()
}

func calculatePoints(hand : Set<String>) ->Int {
    var points = 0
    var cards = 0
    var aces = 0
    for card in hand{
        let value = String(card.dropLast())
        if let intValue = Int(value){
            points += intValue
            cards += 1
        }
        else if value == "J" || value == "K" || value == "Q" {
            points += 10
            cards += 1
        }
        else if value == "A"{
            points += 11
            aces += 1
            cards += 1
        }
        else{
            print("Something went wrong")
        }
    }
    if(cards == 2 && points == 22){
        return 21
    }
    return points
}

var player_stack : Set<String> = []
var computer_stack : Set<String> = []

var flag = true
var mini_flag = false

recreate_stacks()
while flag {
    print("Fake blackjack - choose 1 to draw a card, 2 to stand, 3 to exit")
    if let input = readLine(), let choice = Int(input){
        if choice == 1{ 
            if let card = stack.randomElement(){
                stack.remove(card)
                player_stack.insert(card)
                print("Your cards: \(player_stack)")
                print("Your points: \(calculatePoints(hand: player_stack))")
                if calculatePoints(hand: player_stack) > 21 {
                    mini_flag = true
                }
            }
        }
        else if choice == 2 || mini_flag{
            while calculatePoints(hand: computer_stack) < 17{
                if let card = stack.randomElement(){
                    stack.remove(card)
                    computer_stack.insert(card)
                    print("Computer's cards: \(computer_stack)")
                    print("Computer's points: \(calculatePoints(hand: computer_stack))")
                }
            }
            mini_flag = true
        }
        else if choice == 3{
            flag = false
            print("Game exited.")
        }
        else{
            print("Invalid choice, please try again.")
        }
        if mini_flag {
            if (calculatePoints(hand: player_stack) > calculatePoints(hand: computer_stack) && calculatePoints(hand: player_stack) <= 21) || (calculatePoints(hand: player_stack) <= 21 && calculatePoints(hand: computer_stack) > 21){
                print("You won! You have more points than the computer.")
            }
            else if (calculatePoints(hand: player_stack) < calculatePoints(hand: computer_stack) && calculatePoints(hand: computer_stack) <= 21) || (calculatePoints(hand: player_stack) > 21 && calculatePoints(hand: computer_stack) <= 21){
                print("You lost! Computer has more points than you.")
            }
            else{
                print("It's a tie!")
            }
            mini_flag = false
            recreate_stacks()
        }
    }
}