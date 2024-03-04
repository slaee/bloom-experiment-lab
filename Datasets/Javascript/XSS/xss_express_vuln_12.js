const express = require('express');
const app = express();

app.get('/vuln', (req, res) => {
  const userEmail = req.query.email;
  res.send('<span>Email: ' + userEmail + '</span>');
});

app.listen(3000, () => console.log('Server listening on port 3000'));
