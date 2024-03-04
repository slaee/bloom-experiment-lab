const express = require('express');
const app = express();

app.get('/remediate', (req, res) => {
  const userId = sanitizeInput(req.query.id);
  res.send('<div>Your ID: ' + userId + '</div>');
});

function sanitizeInput(input) {
  // Implement proper input sanitization logic here
  return input.replace(/</g, "&lt;").replace(/>/g, "&gt;");
}

app.listen(3000, () => console.log('Server listening on port 3000'));
