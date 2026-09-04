import express from 'express';
import { engine } from 'express-handlebars';
import fs from 'fs';
import cookieParser from 'cookie-parser';
import Crypto from 'crypto';

const app = express();

app.engine('handlebars', engine());
app.set('view engine', 'handlebars');
app.set('views', './templates');
app.use(express.static('assets'));
app.use(cookieParser());

app.use(express.urlencoded({ extended: true }))

app.listen(3000);