import express from 'express';
import cors from 'cors'
import fs from 'fs'

const app = express();
app.use(cors())
const users = fs.readFileSync('./users.json', 'utf-8')

app.get('/', (req, res) => {
    res.send('Hello world!');
});

app.get("/data", (req, res) =>{
    res.json(users)
})

app.listen(3000);