const express = require('express')
const path = require('node:path')
const app = express()
const port = 44444

app.listen(port, () => {
    console.log(`Serwer działa na http://localhost:${port}`);
});

const data = [
    {
        "id": "0001",
        "type": "donut",
        "name": "Cake",
        "ppu": 0.55,
        "batters": {
            "batter": [
                { "id": "1001", "type": "Regular" },
                { "id": "1002", "type": "Chocolate" },
                { "id": "1003", "type": "Blueberry" },
                { "id": "1004", "type": "Devil's Food" }
            ]
        },
        "topping": [
            { "id": "5001", "type": "None" },
            { "id": "5002", "type": "Glazed" },
            { "id": "5005", "type": "Sugar" },
            { "id": "5007", "type": "Powdered Sugar" },
            { "id": "5006", "type": "Chocolate with Sprinkles" },
            { "id": "5003", "type": "Chocolate" },
            { "id": "5004", "type": "Maple" }
        ]
    },
    {
        "id": "0002",
        "type": "donut",
        "name": "Raised",
        "ppu": 0.55,
        "batters": {
            "batter": [
                { "id": "1001", "type": "Regular" }
            ]
        },
        "topping": [
            { "id": "5001", "type": "None" },
            { "id": "5002", "type": "Glazed" },
            { "id": "5005", "type": "Sugar" },
            { "id": "5003", "type": "Chocolate" },
            { "id": "5004", "type": "Maple" }
        ]
    },
    {
        "id": "0003",
        "type": "donut",
        "name": "Old Fashioned",
        "ppu": 0.55,
        "batters": {
            "batter": [
                { "id": "1001", "type": "Regular" },
                { "id": "1002", "type": "Chocolate" }
            ]
        },
        "topping": [
            { "id": "5001", "type": "None" },
            { "id": "5002", "type": "Glazed" },
            { "id": "5003", "type": "Chocolate" },
            { "id": "5004", "type": "Maple" }
        ]
    }
]

app.get('/:ID/', (req,res) =>{
    console.log(req.params)
    const ID = req.params.ID

    let obj = data.find(item => item.id === ID)
    
    res.send("<h1>" + obj.type + "</h1>")
})

app.get('/:ID/:category/', (req,res) =>{
    console.log(req.params)
    const ID = req.params.ID
    const cat = req.params.category
    
    let obj = data.find(item => item.id === ID)
    
    if (cat == 'batters'){
        obj = obj["batter"]
    }
    
    const final = obj.map(item => item.type)
    res.send("<h1>" + final + "</h1>")
})

app.get('/:ID/:category/:ID2', (req,res) =>{
    console.log(req.params)
    const ID = req.params.ID
    const cat = req.params.category
    const ID2 = req.params.ID2
    
    let obj = data.find(item => item.id === ID)
    
    if (cat == 'batters'){
        obj = obj["batter"]
    }

    const final = data.find(item => item.id === ID2)
    
    res.send("<h1>" + final.type + "</h1>")
})

