const express = require('express');
const app = express();

app.get('/remediate', (req, res) => {
  const userAuthToken = sanitizeInput(req.query.authtoken);
  res.send('<div>Auth Token: ' + userAuthToken + '</div>');
});

function sanitizeInput(input) {
  // Implement proper input sanitization logic here
  return input.replace(/</g, "&lt;").replace(/>/g, "&gt;");
}

app.listen(3000, () => console.log('Server listening on port 3000'));
