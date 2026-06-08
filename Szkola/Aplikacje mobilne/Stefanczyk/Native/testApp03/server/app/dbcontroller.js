import { connectToMongoDB, ObjectId } from './dbconnect.js';

let db;
let collection;

const createCollection = async () => {
  let collection = await db.collection('task_collection');
  console.log('+---------------- collection works!');
  return collection;
};

const connect = async () => {
  db = await connectToMongoDB();
  console.log('+---------------- db works!');
  collection = await createCollection();
};

connect();

const getTasks = async () => {
  const items = await collection.find({}).toArray();
  console.log(items);
  return items;
};

const getById = async (id) => {
  const item = await collection.findOne({
    _id: new ObjectId(id),
  });
  return item;
};

const createTask = async (task) => {
  const result = await collection.insertOne(task);
  return result;
};

const backupTasks = async (tasks) => {
  await collection.deleteMany({});

  if (!tasks || tasks.length === 0) {
    return { insertedCount: 0 };
  }

  const result = await collection.insertMany(tasks);
  return result;
};

const updateTask = async (id, task) => {
  const result = await collection.updateOne(
    { _id: new ObjectId(id) },
    { $set: task }
  );
  return result;
};

const deleteTask = async (id) => {
  const result = await collection.deleteMany({
    _id: new ObjectId(id),
  });
  return result;
};

const deleteTasks = async () => {
  const result = await collection.deleteMany({});
  return result;
};

export {
  backupTasks,
  createTask,
  deleteTask,
  deleteTasks,
  getById,
  getTasks,
  updateTask,
};
