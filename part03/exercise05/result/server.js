const express = require('express');
const { Pool } = require('pg');
const app = express();

const pool = new Pool({
  connectionString: process.env.DATABASE_URL
});

app.get('/results', async (req, res) => {
  const result = await pool.query('SELECT * FROM results');
  res.json(result.rows);
});

app.listen(5001, () => {
  console.log('Result app listening on port 5001');
});
