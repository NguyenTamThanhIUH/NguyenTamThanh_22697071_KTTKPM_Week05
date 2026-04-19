const express = require('express');
const mongoose = require('mongoose');
const app = express();

app.use(express.json());

// MongoDB connection
mongoose.connect(process.env.MONGO_URI, {
  useNewUrlParser: true,
  useUnifiedTopology: true
}).then(() => {
  console.log('MongoDB connected');
}).catch(err => {
  console.log('MongoDB connection error:', err);
});

// Simple schema
const itemSchema = new mongoose.Schema({
  name: String,
  createdAt: { type: Date, default: Date.now }
});

const Item = mongoose.model('Item', itemSchema);

// Routes
app.get('/api/items', async (req, res) => {
  const items = await Item.find();
  res.json(items);
});

app.post('/api/items', async (req, res) => {
  const item = new Item(req.body);
  await item.save();
  res.json(item);
});

app.get('/health', (req, res) => {
  res.json({ status: 'OK' });
});

app.listen(3000, () => {
  console.log('Node.js app listening on port 3000');
});
