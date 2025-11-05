import express from 'express';
import { engine } from 'express-handlebars';
import fs from 'node:fs';

const app = express();

app.engine('handlebars', engine());
app.set('view engine', 'handlebars');
app.set('views', './templates');


app.get('/form', (req, res) => {
    const content = fs.readFileSync('wpisy.txt', 'utf-8')
    console.log(content)
    res.render('form',
        {
            entries: content.split('\n')
        }
    );
});

app.use(express.urlencoded())

app.post('/form', async (req,res) => {
    const date = Date()
    console.log(res.nick)
    let content = await fs.readFileSync('wpisy.txt', 'utf-8')
    content += `\nNick:` + req.body.nick + ` Message:` + req.body.content + ` Date: ` + date.toLocaleString()
    console.log(content)
    fs.writeFileSync('wpisy.txt', content)
    res.redirect('/form')
})

app.get('/', (req,res) => {
    res.render('home');
})

app.listen(3000);