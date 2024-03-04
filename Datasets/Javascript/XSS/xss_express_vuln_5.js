const express = require('express');
const app = express();

app.get('/vuln', (req, res) => {
  const pageTitle = req.query.title;
  res.send('<h1>' + pageTitle + '</h1>');
});

app.listen(3000, () => console.log('Server listening on port 3000'));
