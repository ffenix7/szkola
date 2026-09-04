const express = require('express')
const cors = require("cors")
const app = express()
app.use(cors())
app.use(express.json())
const port = 3000

let  data =  [
    { id: 'v1', location: 'Magazyn Główny', code: '1234', securityLevel: 'High' },
    { id: 'v2', location: 'Biuro Zarządu', code: '9988', securityLevel: 'Critical' },
    { id: 'v3', location: 'Magazyn Główny 2', code: '1234', securityLevel: 'High' },
];

app.get('/', (req, res) => {
  res.send('Hello World!')
})

app.get('/data', (req, res) => {
  res.json(data)
})

app.post('/data', (req, res) => {
  const newVault = {
    id: "v" + (data.length + 1),
    location: req.body.location,
    code: "0000",
    securityLevel: "Low"
  }

  data.push(newVault)

  res.json(newVault)
})

app.listen(port, () => {
  console.log(`Example app listening on port ${port}`)
})