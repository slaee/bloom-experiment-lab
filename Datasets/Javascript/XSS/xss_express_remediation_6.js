const express = require('express');
const app = express();

app.get('/remediate', (req, res) => {
  const userQuery = sanitizeInput(req.query.query);
  res.send('<p>Your search: ' + userQuery + '</p>');
});

function sanitizeInput(input) {
  // Implement proper input sanitization logic here
  return input.replace(/</g, "&lt;").replace(/>/g, "&gt;");
}

app.listen(3000, () => console.log('Server listening on port 3000'));
