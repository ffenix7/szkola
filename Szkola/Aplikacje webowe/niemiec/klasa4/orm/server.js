import express from 'express';
import {DataTypes, Sequelize} from 'sequelize'

const sequelize = new Sequelize({
    dialect: 'sqlite',
    storage: 'database.sqlite'
});

try {
    await sequelize.authenticate();
    console.log('Connection has been established successfully.');
} catch (error) {
    console.error('Unable to connect to the database:', error);
    process.exit()
}

//setup models
const Post = sequelize.define('Post', {
    content: {
        type: DataTypes.TEXT,
        allowNull: false
    },
    upvotes: {
        type: DataTypes.INTEGER,
        allowNull: false,
        defaultValue: 0
    }
})

await sequelize.sync({force: true});
console.log("All models were synchronized successfully!");


const app = express()
const port = 3000

app.use(express.json());

app.get('/', (req, res) => {
    res.send('Hello World!')
})

app.post('/create-post', async (req, res) => {
    console.log("Create post is hit", req.body);
    await Post.create({
        content: "test1",
    })

    return res.json({
        success: true
    });
})

app.get('/posts', async (req, res) =>{
    const posts = await Post.findAll();
    console.log("Posty załadowane");
    return res.json({
        posts: posts
    })
})

app.post('/upvote/:id', async (req, res)=>{
    if (!Number.isInteger(Number(req.params.id)) || req.params.id<0){
        throw new Error("W ID przekaż liczbę >= 0");
    }

    const post = await Post.findByPk(req.params.id);
    console.log(post);
    post.upvotes += 1;
    await post.save();
    return res.json({
        success: true
    })
})


app.listen(port, () => {
    console.log(`Example app listening on port ${port}`)
})