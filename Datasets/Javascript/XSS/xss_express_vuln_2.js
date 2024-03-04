const express = require('express');
const app = express();

app.get('/vuln', (req, res) => {
  const userName = req.query.username;
  res.send('<p>Hello, ' + userName + '!</p>');
});

app.listen(3000, () => console.log('Server listening on port 3000'));
