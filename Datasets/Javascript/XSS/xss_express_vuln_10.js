const express = require('express');
const app = express();

app.get('/vuln', (req, res) => {
  const userData = req.query.userdata;
  res.send('<div>User Data: ' + userData + '</div>');
});

app.listen(3000, () => console.log('Server listening on port 3000'));
