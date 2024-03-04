const express = require('express');
const app = express();

app.get('/remediate', (req, res) => {
  const userData = sanitizeInput(req.query.userdata);
  res.send('<div>User Data: ' + userData + '</div>');
});

function sanitizeInput(input) {
  // Implement proper input sanitization logic here
  return input.replace(/</g, "&lt;").replace(/>/g, "&gt;");
}

app.listen(3000, () => console.log('Server listening on port 3000'));
