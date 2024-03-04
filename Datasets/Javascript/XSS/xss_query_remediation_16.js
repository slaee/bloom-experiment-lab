var userSession = sanitizeInput(getQueryParam('session'));
document.write("<div>Session ID: " + userSession + "</div>");

function sanitizeInput(input) {
  // Implement proper input sanitization logic here
  return input.replace(/</g, "&lt;").replace(/>/g, "&gt;");
}
