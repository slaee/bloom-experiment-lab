const express = require('express');
const app = express();

app.get('/vuln', (req, res) => {
  const userLocation = req.query.location;
  res.send('<div>Location: ' + userLocation + '</div>');
});

app.listen(3000, () => console.log('Server listening on port 3000'));
