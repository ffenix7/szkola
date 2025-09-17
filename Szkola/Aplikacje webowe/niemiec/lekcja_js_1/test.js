const express = require('express')
const path = require('node:path')
const app = express()
const port = 3000

app.get('/', (req, res) => {
  res.send('Kocham kremówki!')
  res.sendFile('index.html', { root: path.join(__dirname, 'public') })
})

app.listen(port, () => {
  console.log(`Example app listening on port ${port}`)
})