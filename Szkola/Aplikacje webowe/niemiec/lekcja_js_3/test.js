const express = require('express')
const path = require('node:path')
const app = express()
const port = 44444

function loggerMiddleware(req, res, next) {
  console.log(`Adres żądania: ${req.path}, Data: ${new Date()}`);
  next();
}

function luckyMiddleware(req, res, next) {
  if(Math.random() < 0.5){
    res.status(403).send('Nie masz szczęścia!');
  } else {
    next();
  }
}

app.use(loggerMiddleware);
app.use('/static', express.static(__dirname + '/public'));

app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname, './public/index.html'));
});

app.get('/podstrona.html', (req, res) => {
  res.sendFile(path.join(__dirname, './public/podstrona.html'));
});

app.get('/podstrona2.html', (req, res) => {
  res.sendFile(path.join(__dirname, './public/podstrona2.html'));
});

app.get('/style.css', (req, res) => {
  res.sendFile(path.join(__dirname, './static/style.css'));
});


app.listen(port, () => {
  console.log(`Example app listening on port ${port}`)
})