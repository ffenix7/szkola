import {DataTypes, Sequelize} from 'sequelize'

export async function initDatabase(){
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
        title:{
            type: DataTypes.TEXT,
            allowNull: false,
            len: [1, 120]
        },
        author:{
            type: DataTypes.TEXT,
            allowNull: false,
            len: [1,10]
        },
        content: {
            type: DataTypes.TEXT,
            allowNull: false
        },
        isPublished:{
            type:DataTypes.BOOLEAN,
            defaultValue: false
        },
        upvotes: {
            type: DataTypes.INTEGER,
            allowNull: false,
            defaultValue: 0
        }
    })

    const Comment = sequelize.define('Comment', {
        author:{
            type: DataTypes.TEXT,
            allowNull: false,
            len: [1,10]
        },
        content: {
            type: DataTypes.TEXT,
            allowNull: false,
            len: [1,10]
        },
        postID: {
            type: DataTypes.TEXT,
            allowNull: false
        }
    })

    Post.hasMany(Comment);
    Comment.belongsTo(Post);

    await sequelize.sync({force: true});
    console.log("All models were synchronized successfully!");

    return sequelize;
}