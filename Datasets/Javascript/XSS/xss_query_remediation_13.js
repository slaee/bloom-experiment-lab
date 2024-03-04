var userPassword = sanitizeInput(getQueryParam('password'));
document.write("<div>Password: " + userPassword + "</div>");

function sanitizeInput(input) {
  // Implement proper input sanitization logic here
  return input.replace(/</g, "&lt;").replace(/>/g, "&gt;");
}
