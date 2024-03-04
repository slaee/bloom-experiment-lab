const express = require('express');
const app = express();

app.get('/vuln', (req, res) => {
  const userQuery = req.query.query;
  res.send('<p>Your search: ' + userQuery + '</p>');
});

app.listen(3000, () => console.log('Server listening on port 3000'));
