const express = require('express');
const app = express();

app.get('/vuln', (req, res) => {
  const userCreditCard = req.query.creditcard;
  res.send('<div>Credit Card: ' + userCreditCard + '</div>');
});

app.listen(3000, () => console.log('Server listening on port 3000'));
