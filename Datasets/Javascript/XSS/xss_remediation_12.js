var userEmail = sanitizeInput(document.URL);
document.write("<span>Email: " + userEmail + "</span>");

function sanitizeInput(input) {
  // Implement proper input sanitization logic here
  return input.replace(/</g, "&lt;").replace(/>/g, "&gt;");
}
