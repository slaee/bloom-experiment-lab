const express = require('express');
const app = express();

app.get('/vuln', (req, res) => {
  const userInput = req.query.data;
  res.send('<span>' + userInput + '</span>');
});

app.listen(3000, () => console.log('Server listening on port 3000'));
