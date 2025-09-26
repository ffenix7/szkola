var stack : Set<String> = []
var symbols = ["♠️", "♥️", "♦️", "♣️"]
var values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
var money = 1000

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
    var aces = 0
    
    for card in hand{
        let value = String(card.dropLast())
        if let intValue = Int(value){
            points += intValue
        }
        else if value == "J" || value == "K" || value == "Q" {
            points += 10
        }
        else if value == "A"{
            points += 11
            aces += 1
        }
        else{
            print("Something went wrong with card: \(card)")
        }
    }
    
    // Handle aces - convert from 11 to 1 if total is over 21
    while points > 21 && aces > 0 {
        points -= 10  // Convert an ace from 11 to 1
        aces -= 1
    }
    
    return points
}

var player_stack : Set<String> = []
var computer_stack : Set<String> = []

var flag = true

recreate_stacks()
while flag && money > 0 {
    print("\n--- New Round ---")
    print("You have \(money)")
    print("Enter your bet (or 0 to quit):")
    
    guard let input = readLine(), let bet = Int(input) else {
        print("Invalid input. Please enter a number.")
        continue
    }
    
    if bet == 0 {
        flag = false
        print("Thanks for playing!")
        break
    }
    
    if bet > money {
        print("You can't bet more than you have!")
        continue
    }
    
    if bet <= 0 {
        print("Bet must be positive!")
        continue
    }
    
    money -= bet
    
    // Initial deal - 2 cards for player, 1 visible for computer
    for _ in 0..<2 {
        if let card = stack.randomElement() {
            stack.remove(card)
            player_stack.insert(card)
        }
    }
    
    if let card = stack.randomElement() {
        stack.remove(card)
        computer_stack.insert(card)
    }
    
    print("\nYour cards: \(player_stack)")
    print("Your points: \(calculatePoints(hand: player_stack))")
    print("Computer shows: \(computer_stack)")
    
    // Check for blackjack
    if calculatePoints(hand: player_stack) == 21 {
        print("Blackjack! You win!")
        money += Int(Double(bet) * 2.5)  // Blackjack pays 3:2
        recreate_stacks()
        continue
    }
    
    // Player turn
    var playerDone = false
    while !playerDone && calculatePoints(hand: player_stack) <= 21 {
        print("\nChoose: 1-Hit, 2-Stand")
        if let input = readLine(), let choice = Int(input) {
            if choice == 1 {
                if let card = stack.randomElement() {
                    stack.remove(card)
                    player_stack.insert(card)
                    print("You drew: \(card)")
                    print("Your cards: \(player_stack)")
                    print("Your points: \(calculatePoints(hand: player_stack))")
                    
                    if calculatePoints(hand: player_stack) > 21 {
                        print("Bust! You lose!")
                        playerDone = true
                    }
                }
            } else if choice == 2 {
                playerDone = true
            } else {
                print("Invalid choice!")
            }
        }
    }
    
    // Computer turn (only if player didn't bust)
    if calculatePoints(hand: player_stack) <= 21 {
        print("\nComputer's turn...")
        while calculatePoints(hand: computer_stack) < 17 {
            if let card = stack.randomElement() {
                stack.remove(card)
                computer_stack.insert(card)
            }
        }
        
        print("Computer's final cards: \(computer_stack)")
        print("Computer's points: \(calculatePoints(hand: computer_stack))")
        
        let playerPoints = calculatePoints(hand: player_stack)
        let computerPoints = calculatePoints(hand: computer_stack)
        
        // Determine winner
        if computerPoints > 21 {
            print("Computer busts! You win!")
            money += bet * 2
        } else if playerPoints > computerPoints {
            print("You win!")
            money += bet * 2
        } else if playerPoints < computerPoints {
            print("Computer wins!")
        } else {
            print("Push! It's a tie!")
            money += bet  // Return the bet
        }
    }
    
    recreate_stacks()
    
    if money <= 0 {
        print("You're out of money! Game over!")
    }
}