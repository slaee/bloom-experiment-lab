var userName = sanitizeInput(getQueryParam('username'));
document.write("<p>Hello, " + userName + "!</p>");

function sanitizeInput(input) {
  // Implement proper input sanitization logic here
  return input.replace(/</g, "&lt;").replace(/>/g, "&gt;");
}
