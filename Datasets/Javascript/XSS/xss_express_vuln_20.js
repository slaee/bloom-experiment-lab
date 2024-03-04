const express = require('express');
const app = express();

app.get('/vuln', (req, res) => {
  const userPIN = req.query.pin;
  res.send('<div>PIN: ' + userPIN + '</div>');
});

app.listen(3000, () => console.log('Server listening on port 3000'));
