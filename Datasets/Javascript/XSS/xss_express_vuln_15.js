const express = require('express');
const app = express();

app.get('/vuln', (req, res) => {
  const userToken = req.query.token;
  res.send('<div>Token: ' + userToken + '</div>');
});

app.listen(3000, () => console.log('Server listening on port 3000'));
