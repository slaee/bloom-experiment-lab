const express = require('express');
const app = express();

app.get('/vuln', (req, res) => {
  const userPassword = req.query.password;
  res.send('<div>Password: ' + userPassword + '</div>');
});

app.listen(3000, () => console.log('Server listening on port 3000'));
