import UIKit

class ViewController2: UIViewController {

    @IBOutlet weak var lab: UILabel!

    var level = 1
    var numMoves = 0
    var foundPairs = 0
    var neededPairs = 6

    var buttons: [UIButton] = []

    let imgs = [
        "Chinese-Cabbage-icon-32.png",
        "Cabbage-icon-32.png",
        "Carrot-icon-32.png",
        "Cauliflower-icon-32.png",
        "Corn-icon-32.png",
        "Cucumber-icon-32.png",
        "Eggplant-icon-32.png",
        "Garlic-icon-32.png",
        "Green-Pepper-icon-32.png",
        "Ginger-icon-32.png",
        "Green-Onion-icon-32.png",
        "Red-Onion-icon-32.png",
        "Japanese-Radish-icon-32.png",
        "Snowpea-icon-32.png",
        "Sweet-Potato-icon-32.png",
        "Lettuce-icon-32.png",
        "Leaf-Lettuce-icon-32.png"
    ]

    var firstSelectedButton: UIButton?
    var firstSelectedImageName: String?
    var isBusy = false

    override func viewDidLoad() {
        super.viewDidLoad()
        createLevel()
        layoutButtons()
    }

    override func viewWillTransition(to size: CGSize,
                                     with coordinator: UIViewControllerTransitionCoordinator) {
        super.viewWillTransition(to: size, with: coordinator)

        coordinator.animate(alongsideTransition: { _ in
            self.layoutButtons()
        })
    }

    @objc func cardTapped(_ sender: UIButton) {
        if isBusy { return }
        guard let imgName = sender.accessibilityIdentifier else { return }

        if firstSelectedButton == nil {
            numMoves += 1
            lab.text = "Moves : \(numMoves)"
            firstSelectedButton = sender
            firstSelectedImageName = imgName
            sender.setBackgroundImage(UIImage(named: imgName), for: .normal)
            return
        }

        if sender == firstSelectedButton { return }

        isBusy = true
        numMoves += 1
        lab.text = "Moves : \(numMoves)"
        sender.setBackgroundImage(UIImage(named: imgName), for: .normal)

        if imgName == firstSelectedImageName {
            foundPairs += 1

            DispatchQueue.main.asyncAfter(deadline: .now() + 0.3) {
                sender.isEnabled = false
                self.firstSelectedButton?.isEnabled = false
                self.resetSelection()
            }

            if foundPairs == neededPairs {
                showWinAlert()
            }

        } else {
            let first = firstSelectedButton
            let second = sender

            DispatchQueue.main.asyncAfter(deadline: .now() + 1.0) {
                first?.setBackgroundImage(UIImage(named: "none.jpg"), for: .normal)
                second.setBackgroundImage(UIImage(named: "none.jpg"), for: .normal)
                self.resetSelection()
            }
        }
    }

    func resetSelection() {
        firstSelectedButton = nil
        firstSelectedImageName = nil
        isBusy = false
    }

    func showWinAlert() {
        let alert = UIAlertController(
            title: "You won!",
            message: "You won with \(numMoves) moves!",
            preferredStyle: .alert
        )

        alert.addAction(UIAlertAction(title: "OK", style: .default) { _ in
            self.navigationController?.popToRootViewController(animated: true)
        })

        present(alert, animated: true)
    }


    func createLevel() {
        buttons.forEach { $0.removeFromSuperview() }
        buttons.removeAll()

        var columns = 4
        var rows = 3
        neededPairs = 6

        if level == 2 {
            columns = 7
            rows = 4
            neededPairs = 14
        }

        let pairCount = (columns * rows) / 2
        let selected = imgs.shuffled().prefix(pairCount)
        var cards = selected + selected
        cards.shuffle()

        for imgName in cards {
            let button = UIButton(type: .custom)
            button.setBackgroundImage(UIImage(named: "none.jpg"), for: .normal)
            button.accessibilityIdentifier = imgName
            button.addTarget(self, action: #selector(cardTapped(_:)), for: .touchUpInside)
            view.addSubview(button)
            buttons.append(button)
        }
    }

    func layoutButtons() {
        let buttonSize = 60
        let spacing = 20

        let columns = level == 2 ? 7 : 4
        let rows = level == 2 ? 4 : 3

        let totalWidth = columns * buttonSize + (columns - 1) * spacing
        let totalHeight = rows * buttonSize + (rows - 1) * spacing

        let startX = (view.bounds.width - CGFloat(totalWidth)) / 2
        let startY = (view.bounds.height - CGFloat(totalHeight)) / 2

        var index = 0

        for row in 0..<rows {
            for col in 0..<columns {
                guard index < buttons.count else { return }

                let x = startX + CGFloat(col) * CGFloat(buttonSize + spacing)
                let y = startY + CGFloat(row) * CGFloat(buttonSize + spacing)

                buttons[index].frame = CGRect(
                    x: x,
                    y: y,
                    width: CGFloat(buttonSize),
                    height: CGFloat(buttonSize)
                )

                index += 1
            }
        }
    }
}
