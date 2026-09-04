import UIKit

class ViewController: UIViewController, UIScrollViewDelegate {

    @IBOutlet weak var sv: UIScrollView!
    @IBOutlet weak var pc: UIPageControl!
    @IBOutlet weak var lapsButton: UIButton!
    @IBOutlet weak var tableView: UITableView!
    @IBOutlet weak var button: UIButton!
    @IBOutlet weak var time: UILabel!
    
    var timer: Timer?
    var isRunning = false
    
    var laps: [String] = []
    
    var startTime: TimeInterval = 0
    var totalTime: TimeInterval = 0
    var lastLapTime: TimeInterval = 0

    override func viewDidLoad() {
        super.viewDidLoad()
        
        tableView.dataSource = self
        tableView.delegate = self
        sv.delegate = self
        
        time.text = "0.00"
        button.backgroundColor = UIColor.green
        
        var slides = Array<Any>()
        sv.frame = CGRect(x: 0, y: 0, width: view.frame.width, height: view.frame.height)
        sv.isPagingEnabled = true    // w przypadku dwóch widoków - nadmiarowe

        // odpowiednie paski przewijania
        sv.showsVerticalScrollIndicator = false
        sv.showsHorizontalScrollIndicator = false

        let slideA : SlideA = Bundle.main.loadNibNamed("SlideA", owner: self, options: nil)?.first as! SlideA
        let slideB : SlideB = Bundle.main.loadNibNamed("SlideB", owner: self, options: nil)?.first as! SlideB

        slideA.frame = CGRect(x: 0, y: 0, width: view.frame.width, height: view.frame.height)
        slideB.frame = CGRect(x: view.frame.width, y: 0, width: view.frame.width, height: view.frame.height)
                
        slides = [slideA, slideB]
        
        sv.addSubview(slideA)
        sv.addSubview(slideB)
        sv.contentSize = CGSize(width: view.frame.width*2, height: view.frame.height-24)   // 24 - pobierz programowo wartość StatusBara'a
        pc.numberOfPages = slides.count

    }
    
    func scrollViewDidScroll(_ scrollView: UIScrollView) {
        let pageIndex = round(sv.contentOffset.x/view.frame.width)
        pc.currentPage = Int(pageIndex)
    }
    
    @IBAction func change(_ sender: UIPageControl) {
        let x = CGFloat(sender.currentPage) * view.frame.width
        sv.contentOffset = CGPoint(x: x, y: 0)
    }
    
    @IBAction func lapsButtonClicked(_ sender: Any) {
        if isRunning {
            // Obliczamy czas od ostatniego lapu
            let currentTime = Date().timeIntervalSinceReferenceDate
            let lapTime = (currentTime - startTime) - lastLapTime
            lastLapTime += lapTime
            
            laps.insert(String(format: "%.2f", lapTime), at: 0)
            tableView.reloadData()
        } else {
            // Reset całego stopera
            timer?.invalidate()
            time.text = "0.00"
            laps.removeAll()
            lastLapTime = 0
            totalTime = 0
            tableView.reloadData()
            button.setTitle("Start", for: .normal)
            button.backgroundColor = UIColor.green
            lapsButton.setTitle("Laps", for: .normal)
        }
    }
    
    @IBAction func buttonClicked(_ sender: Any) {
        if isRunning {
            // Stop
            timer?.invalidate()
            totalTime += Date().timeIntervalSinceReferenceDate - startTime
            
            button.setTitle("Start", for: .normal)
            button.backgroundColor = UIColor.green
            lapsButton.setTitle("Wyzeruj", for: .normal)
        } else {
            // Start
            startTime = Date().timeIntervalSinceReferenceDate
            lastLapTime = 0
            
            timer = Timer.scheduledTimer(timeInterval: 0.01,
                                         target: self,
                                         selector: #selector(update),
                                         userInfo: nil,
                                         repeats: true)
            
            button.setTitle("Stop", for: .normal)
            button.backgroundColor = UIColor.red
            lapsButton.setTitle("Laps", for: .normal)
        }
        
        isRunning.toggle()
    }

    @objc func update() {
        let currentTime = Date().timeIntervalSinceReferenceDate
        let elapsed = (currentTime - startTime) + totalTime
        time.text = String(format: "%.2f", elapsed)
    }
}

extension ViewController: UITableViewDataSource {

    func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
         return laps.count
    }
    
    func tableView(_ tableView: UITableView,
                   cellForRowAt indexPath: IndexPath) -> UITableViewCell {

        let cell = tableView.dequeueReusableCell(withIdentifier: "cell", for: indexPath) as! TableData
        
        cell.left.text = "#\(indexPath.row + 1)"
        cell.mid.text = "Lap"
        cell.right.text = laps[indexPath.row]

        return cell
    }
}

extension ViewController: UITableViewDelegate { }

class TableData: UITableViewCell {
    @IBOutlet weak var left: UILabel!
    @IBOutlet weak var mid: UILabel!
    @IBOutlet weak var right: UILabel!
}
