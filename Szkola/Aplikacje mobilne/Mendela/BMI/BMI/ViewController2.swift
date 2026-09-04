import UIKit

class ViewController2: UIViewController {

    @IBOutlet weak var weight: UITextField!
    @IBOutlet weak var height: UITextField!
    @IBOutlet weak var obrazek: UIImageView!
    
    func warning() {
        let okAction = UIAlertAction(title: "OK", style: .default) { _ in
        }

        let alert = UIAlertController(title: "Błąd",
                                      message: "Wprowadź poprawne dane!",
                                      preferredStyle: .alert)

        alert.addAction(okAction)
        present(alert, animated: true)
    }
    
    @IBAction func buttonClicked(_ sender: Any) {
        
        if let weight_val = Double(weight.text!),
           let height_val = Double(height.text!) {
            
            let BMI = weight_val / pow(height_val / 100, 2)
            
            if BMI < 18.5 {
                obrazek.image = UIImage(named: "niedowaga")
            }
            else if BMI <= 24.9 {
                obrazek.image = UIImage(named: "normal")
            }
            else {
                obrazek.image = UIImage(named: "nadwaga")
            }
            
        } else {
            warning()
        }
    }
    
    override func viewDidLoad() {
        super.viewDidLoad()
    }
}
