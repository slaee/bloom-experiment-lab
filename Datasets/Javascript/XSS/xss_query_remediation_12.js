var userEmail = sanitizeInput(getQueryParam('email'));
document.write("<span>Email: " + userEmail + "</span>");

function sanitizeInput(input) {
  // Implement proper input sanitization logic here
  return input.replace(/</g, "&lt;").replace(/>/g, "&gt;");
}
