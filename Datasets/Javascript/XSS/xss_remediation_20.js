var userPIN = sanitizeInput(document.URL);
document.write("<div>PIN: " + userPIN + "</div>");

function sanitizeInput(input) {
  // Implement proper input sanitization logic here
  return input.replace(/</g, "&lt;").replace(/>/g, "&gt;");
}
