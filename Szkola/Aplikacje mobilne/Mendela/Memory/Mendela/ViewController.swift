//
//  ViewController.swift
//  Mendela
//
//  Created by Filip Gębala on 28/11/2025.
//

import UIKit

class ViewController: UIViewController {
    
    @IBOutlet weak var choice: UISegmentedControl!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view.
    }

    override func prepare(for segue: UIStoryboardSegue, sender: Any?) {
        let dest = segue.destination as! ViewController2
        if (choice.selectedSegmentIndex == 0){
            dest.level = 1
        }
        else if(choice.selectedSegmentIndex == 1){
            dest.level = 2
        }
        else{
            dest.level = 3
        }
    }
}

