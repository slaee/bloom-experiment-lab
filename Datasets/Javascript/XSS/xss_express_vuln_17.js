const express = require('express');
const app = express();

app.get('/vuln', (req, res) => {
  const userIP = req.query.ip;
  res.send('<div>Your IP: ' + userIP + '</div>');
});

app.listen(3000, () => console.log('Server listening on port 3000'));
