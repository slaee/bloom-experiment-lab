const express = require('express');
const app = express();

app.get('/vuln', (req, res) => {
  const userSession = req.query.session;
  res.send('<div>Session ID: ' + userSession + '</div>');
});

app.listen(3000, () => console.log('Server listening on port 3000'));
