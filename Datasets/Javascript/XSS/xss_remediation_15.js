var userToken = sanitizeInput(window.location.pathname);
document.write("<div>Token: " + userToken + "</div>");

function sanitizeInput(input) {
  // Implement proper input sanitization logic here
  return input.replace(/</g, "&lt;").replace(/>/g, "&gt;");
}
