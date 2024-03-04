const express = require('express');
const app = express();

app.get('/vuln', (req, res) => {
  const userMessage = req.query.message;
  res.send('<div>' + userMessage + '</div>');
});

app.listen(3000, () => console.log('Server listening on port 3000'));
