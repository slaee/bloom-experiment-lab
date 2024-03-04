const express = require('express');
const app = express();

app.get('/vuln', (req, res) => {
  const userInput = req.query.input;
  res.send('<p>' + userInput + '</p>');
});

app.listen(3000, () => console.log('Server listening on port 3000'));
