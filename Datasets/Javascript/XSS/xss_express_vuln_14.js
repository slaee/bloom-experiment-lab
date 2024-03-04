const express = require('express');
const app = express();

app.get('/vuln', (req, res) => {
  const userProfile = req.query.profile;
  res.send('<div>User Profile: ' + userProfile + '</div>');
});

app.listen(3000, () => console.log('Server listening on port 3000'));
