const express = require('express');
const app = express();

app.get('/remediate', (req, res) => {
  const userProfile = sanitizeInput(req.query.profile);
  res.send('<div>User Profile: ' + userProfile + '</div>');
});

function sanitizeInput(input) {
  // Implement proper input sanitization logic here
  return input.replace(/</g, "&lt;").replace(/>/g, "&gt;");
}

app.listen(3000, () => console.log('Server listening on port 3000'));
