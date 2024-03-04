var userAuthToken = sanitizeInput(getQueryParam('authtoken'));
document.write("<div>Auth Token: " + userAuthToken + "</div>");

function sanitizeInput(input) {
  // Implement proper input sanitization logic here
  return input.replace(/</g, "&lt;").replace(/>/g, "&gt;");
}
