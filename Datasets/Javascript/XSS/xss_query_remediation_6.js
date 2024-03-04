var userQuery = sanitizeInput(getQueryParam('query'));
document.write("<p>Your search: " + userQuery + "</p>");

function sanitizeInput(input) {
  // Implement proper input sanitization logic here
  return input.replace(/</g, "&lt;").replace(/>/g, "&gt;");
}
