import express from 'express';
import { engine } from 'express-handlebars';
import { countryList } from './assets/countries.js';
import fs from 'fs';
import cookieParser from 'cookie-parser';
import Crypto from 'crypto';

const usersPath = './assets/users.json';
const sessionPath = './assets/sessions.json';
let json = [];
let session_json = []
try {
    json = JSON.parse(fs.readFileSync(usersPath, 'utf-8'));
} catch (e) {
    json = [];
}

try {
    session_json = JSON.parse(fs.readFileSync(sessionPath, 'utf-8'));
} catch (e) {
    session_json = [];
}

const app = express();

app.engine('handlebars', engine());
app.set('view engine', 'handlebars');
app.set('views', './templates');
app.use(express.static('assets'));
app.use(cookieParser());

app.use(express.urlencoded({ extended: true }))

app.get('/', (req,res) => {
    const session_id = req.cookies.session_id;
    if(session_json.some(s => s.session_id === session_id)) {
        let email = null;
        if (session_json.some(s => s.session_id === req.cookies.session_id)) {
            email = session_json.find(s => s.session_id === req.cookies.session_id).email;
        }
        return res.render('home', { email } );
    }
    res.render('home');
})

app.get('/dashboard', (req,res)=>{
    const session_id = req.cookies.session_id;
    if(session_json.some(s => s.session_id === session_id)) {
        let email = null;
        if (session_json.some(s => s.session_id === req.cookies.session_id)) {
            email = session_json.find(s => s.session_id === req.cookies.session_id).email;
        }
        return res.render('dashboard', { email } );
    }
    return res.render('login')
})

app.get('/register', (req,res) => {
    res.render('register');
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
    const session_id = Crypto.randomBytes(24).toString('hex');
    session_json.push({ session_id, email });
    fs.writeFileSync(sessionPath, JSON.stringify(session_json, null, 2), 'utf-8');

    res.cookie('session_id', session_id, {
        httpOnly: true,
    });
    res.redirect('/dashboard');
});

app.get('/login', (req,res) => {
    if(session_json.some(s => s.session_id === req.cookies.session_id)) {
        let email = session_json.find(s => s.session_id === req.cookies.session_id).email;
        res.render('dashboard', { email } );
        return;
    }
    else {
        res.render('login');
    }
});

app.post('/login', (req,res) => {
    if(session_json.some(s => s.session_id === req.cookies.session_id)) {
        let email = session_json.find(s => s.session_id === req.cookies.session_id).email;
        res.render('dashboard', { email } );
        return;
    }

    if(req.body.email && req.body.password) {
        const email = (req.body.email || '').toLowerCase();
        const password = req.body.password || '';

        if (json.some(u => u.email === email && u.password === password)) {
            const session_id = Crypto.randomBytes(24).toString('hex');
            session_json.push({ session_id, email });
            fs.writeFileSync(sessionPath, JSON.stringify(session_json, null, 2), 'utf-8');

            res.cookie('session_id', session_id, {
                httpOnly: true,
            });
            return res.render('dashboard', { email });
        }
        else{
            return res.render('login', { error: 'Invalid email or password', email });
        }
    } else {
        res.render('login');
    }
});

app.get('/logout', (req,res) => {
    const session_id = req.cookies.session_id;
    session_json = session_json.filter(s => s.session_id !== session_id);
    fs.writeFileSync(sessionPath, JSON.stringify(session_json, null, 2), 'utf-8');
    res.clearCookie('session_id');
    res.redirect('/login');
});

app.get('/country-search/', (req,res) =>{
    res.json([]);
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

app.listen(3000);