import express from 'express';
import { initDatabase } from './database.js';

const sequelize = await initDatabase();

const {Post, Comment} = sequelize.models;

const app = express()
const port = 3000

app.use(express.json());

app.get('/posts', async (req, res) =>{
    const posts = await Post.findAll();
    return res.json({
        posts: posts //wrzuć tu .map i wyciągnij to co potrzebujesz
    })
})

app.post('/post', async (req, res) => {
    if(req.body.title===undefined || req.body.title.length > 120){
        return res.status(400).json({
            success: false,
            message: "Musisz podać tytuł który ma max 10 znaków!"
        });
    }

    if(req.body.author===undefined || req.body.author.length > 10){
        return res.status(400).json({
            success: false,
            message: "Musisz podać autora który ma max 10 znaków!"
        });
    }

    if(req.body.content===undefined){
        return res.status(400).json({
            success: false,
            message: "Musisz podać content posta!"
        });
    }

    if(req.body.isPublished===undefined){
        return res.status(400).json({
            success: false,
            message: "Musisz podać flage isPublished!"
        });
    }

    const newPost = await Post.create({
        title: req.body.title,
        author: req.body.author,
        content: req.body.content,
        isPublished: req.body.isPublished
    })

    return res.json(newPost);
})

app.post('/comment', async (req,res)=>{
    if(req.body.author===undefined || req.body.author.length > 10){
        return res.status(400).json({
            success: false,
            message: "Musisz podać autora, którego długośc to max 10 znaków!"
        });
    }

    if(req.body.author===undefined || req.body.author.length > 255){
        return res.status(400).json({
            success: false,
            message: "Musisz podać content komentarza, którego długość to max 255 znaków!"
        });
    }

    if(req.body.postID===undefined){
        return res.status(400).json({
            success: false,
            message: "Musisz podać ID posta do którego chcesz dodać komentarz!"
        });
    }

    const post = Post.findByPk(req.body.postID)
    if(post === null){
        return res.status(400).json({
            success: false,
            message: "Musisz podać ID posta, który istnieje!"
        });
    }

    const newComment = await Comment.create({
        author: req.body.author,
        content: req.body.content,
        postID: req.body.postID
    })

    return res.status(201).json({
            success: true,
            message: "Utworzono komentarz!"
    });
})

app.post('/upvote/:id', async (req, res)=>{
    if (!Number.isInteger(Number(req.params.id)) || req.params.id<0){
        throw new Error("W ID przekaż liczbę >= 0");
    }

    const post = await Post.findByPk(req.params.id);
    post.upvotes += 1;

    await post.save();
    return res.json({
        success: true
    })
})

app.patch('/post/:id', (req,res)=>{
    return res.status(404);
})

app.listen(port, () => {
    console.log(`Example app listening on port ${port}`)
})