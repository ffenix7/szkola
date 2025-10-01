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
app.use('/static', express.static(__dirname + '/static'));
app.use('/public', express.static(__dirname + '/public'));

app.get('/style.css', (req, res) => {
  res.sendFile(path.join(__dirname, 'static', 'style.css'));
});

app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname, 'index.html'));
});

app.get('/podstrona.html', (req, res) => {
  res.sendFile(path.join(__dirname, 'podstrona.html'));
});

app.get('/podstrona2.html', (req, res) => {
  res.sendFile(path.join(__dirname, 'podstrona2.html'));
});

app.listen(port, () => {
  console.log(`Example app listening on port ${port}`)
})