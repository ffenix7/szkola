import express, { json } from 'express';
import {
  backupTasks,
  createTask,
  deleteTask,
  deleteTasks,
  getById,
  getTasks,
  updateTask,
} from './app/dbcontroller.js';

const app = express();
const PORT = 3000;

app.use(json());

app.get('/api/task', async (req, res) => {
  console.log('get');
  const tasks = await getTasks();
  res.status(200).json(tasks);
});

app.get('/api/task/:id', async (req, res) => {
  console.log('get by id');
  const task = await getById(req.params.id);
  res.status(200).json(task);
});

app.post('/api/task', async (req, res) => {
  console.log('post');
  const result = await createTask(req.body);
  res.status(201).json(result);
});

app.post('/api/task/backup', async (req, res) => {
  console.log('backup');
  const result = await backupTasks(req.body.notes);
  res.status(201).json({
    count: result.insertedCount,
  });
});

app.post('/api/task/update/:id', async (req, res) => {
  console.log('update');
  const result = await updateTask(req.params.id, req.body);
  res.status(200).json(result);
});

app.delete('/api/task', async (req, res) => {
  console.log('delete all');
  const result = await deleteTasks();
  res.status(200).json(result);
});

app.delete('/api/task/:id', async (req, res) => {
  console.log('delete');
  const result = await deleteTask(req.params.id);
  res.status(200).json(result);
});

app.listen(PORT, () => {
  console.log(`Server works on port ${PORT}`);
});
