import express from 'express';
import cors from 'cors';
import fs from 'fs';

const app = express();
app.use(cors());
app.use(express.json());

const USERS_PATH = './users.json';

const readUsers = () => {
    const raw = fs.readFileSync(USERS_PATH, 'utf-8');
    try {
        return JSON.parse(raw);
    } catch (error) {
        return [];
    }
};

const writeUsers = (users) => {
    fs.writeFileSync(USERS_PATH, JSON.stringify(users, null, 4));
};

app.get('/', (req, res) => {
    res.send('Hello world!');
});

app.get('/users', (req, res) => {
    res.json(readUsers());
});

app.get('/users/:index', (req, res) => {
    const index = Number(req.params.index);
    const users = readUsers();
    if (!Number.isInteger(index) || index < 0 || index >= users.length) {
        return res.status(404).json({ status: 'NOTFOUND' });
    }

    return res.json(users[index]);
});

app.post('/register', (req, res) => {
    const { username, password } = req.body || {};
    if (!username || !password) {
        return res.status(400).json({ status: 'INVALID' });
    }

    const users = readUsers();
    const exists = users.some((user) => user.username === username);
    if (exists) {
        return res.status(409).json({ status: 'USEREXISTS' });
    }

    users.push({
        username,
        password,
        createdAt: new Date().toISOString(),
    });
    writeUsers(users);
    return res.json({ status: 'OK' });
});

app.delete('/users/:index', (req, res) => {
    const index = Number(req.params.index);
    const users = readUsers();
    if (!Number.isInteger(index) || index < 0 || index >= users.length) {
        return res.status(404).json({ status: 'NOTFOUND' });
    }

    users.splice(index, 1);
    writeUsers(users);
    return res.json({ status: 'OK' });
});

app.get('/data', (req, res) => {
    res.json(readUsers());
});

app.listen(3000);