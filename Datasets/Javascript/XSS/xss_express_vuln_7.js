const express = require('express');
const app = express();

app.get('/vuln', (req, res) => {
  const userId = req.query.id;
  res.send('<div>Your ID: ' + userId + '</div>');
});

app.listen(3000, () => console.log('Server listening on port 3000'));
