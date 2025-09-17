const express = require('express')
const path = require('node:path')
const app = express()
const port = 44444

app.get('/', (req, res) => {
  res.sendFile('index.html', { root: path.join(__dirname, 'public') })
  res.sendFile('style.css', { root: path.join(__dirname, 'public') })
})

app.get('/kremowki', (req,res) =>{
    res.sendFile('../public/kremowki.html', { root: path.join(__dirname, 'public') })
})

app.listen(port, () => {
  console.log(`Example app listening on port ${port}`)
})