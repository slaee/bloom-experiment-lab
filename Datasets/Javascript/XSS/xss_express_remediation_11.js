const express = require('express');
const app = express();

app.get('/remediate', (req, res) => {
  const userInput = sanitizeInput(req.query.input);
  res.send('<p>' + userInput + '</p>');
});

function sanitizeInput(input) {
  // Implement proper input sanitization logic here
  return input.replace(/</g, "&lt;").replace(/>/g, "&gt;");
}

app.listen(3000, () => console.log('Server listening on port 3000'));
