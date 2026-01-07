import express from 'express';
import { engine } from 'express-handlebars';
import { countryList } from './assets/countries.js';
import fs from 'fs';
import cookieParser from 'cookie-parser';

const usersPath = './assets/users.json';
let json = [];
try {
    json = JSON.parse(fs.readFileSync(usersPath, 'utf-8'));
} catch (e) {
    json = [];
}

const app = express();

app.engine('handlebars', engine());
app.set('view engine', 'handlebars');
app.set('views', './templates');
app.use(express.static('assets'));
app.use(cookieParser());

app.use(express.urlencoded({ extended: true }))

app.get('/', (req,res) => {
    console.log('Cookies: ', req.cookies);
    res.render('home');
})

app.get('/register', (req,res) => {
    res.render('register');
});

app.get('/country-search/', (req,res) =>{
    res.json([]);
});

app.get('/login', (req,res) => {
    if(req.body.email && req.body.password) {
        const email = (req.body.email || '').toLowerCase();
        const password = req.body.password || '';
        if (email == "test@gmail.com" && password == "zaq123") {
            res.cookie('session_id', 'random_session_value', {
                httpOnly: true,
            });
            return res.render('login-success', { email });
        }
        else{
            return res.render('login', { error: 'Invalid email or password', email });
        }
});

app.get('/test-cookies', (req,res) => {
    res.cookie('test_cookie', 'test_value', {
        httpOnly: true,
    });
    res.render('test');
});


app.get('/country-search/:term', (req,res) =>{
    const term = (req.params.term || '').toLowerCase();

    const results = countryList.filter(c =>
        c.toLowerCase().includes(term)
    );

    res.json(results);
});

app.get('/check-user/:email', (req,res) => {
    const email = req.params.email || '';
    const exists = json.some(u => u.email.toLowerCase() === email.toLowerCase());
    res.json({ exists });
});

app.post('/register', (req,res) => {
    const email = (req.body.email || '').toLowerCase();
    const password = req.body.password1 || req.body.password || '';
    const country = req.body.country || '';

    if (json.some(u => u.email === email)) {
        return res.render('register', { error: 'Email is already registered', email, country });
    }

    json.push({ "email": email, "password": password, "country": country });
    fs.writeFileSync(usersPath, JSON.stringify(json, null, 2), 'utf-8');
    console.log(json);
    res.redirect(`/register-success?email=${encodeURIComponent(email)}`);
});

app.get('/register-success', (req, res) => {
    const email = (req.query.email || '').toLowerCase();
    res.render('register-success', { email });
});
app.listen(3000);