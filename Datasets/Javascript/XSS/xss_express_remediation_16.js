const express = require('express');
const app = express();

app.get('/remediate', (req, res) => {
  const userSession = sanitizeInput(req.query.session);
  res.send('<div>Session ID: ' + userSession + '</div>');
});

function sanitizeInput(input) {
  // Implement proper input sanitization logic here
  return input.replace(/</g, "&lt;").replace(/>/g, "&gt;");
}

app.listen(3000, () => console.log('Server listening on port 3000'));
