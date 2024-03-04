const express = require('express');
const app = express();

app.get('/vuln', (req, res) => {
  const userAuthToken = req.query.authtoken;
  res.send('<div>Auth Token: ' + userAuthToken + '</div>');
});

app.listen(3000, () => console.log('Server listening on port 3000'));
