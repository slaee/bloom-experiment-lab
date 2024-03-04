const express = require('express');
const app = express();

app.get('/vuln', (req, res) => {
  const errorMsg = req.query.error;
  res.send(`<div id="error-message">${errorMsg}</div>`);
});

app.listen(3000, () => console.log('Server listening on port 3000'));
