var userId = sanitizeInput(getQueryParam('id'));
document.write("<div>Your ID: " + userId + "</div>");

function sanitizeInput(input) {
  // Implement proper input sanitization logic here
  return input.replace(/</g, "&lt;").replace(/>/g, "&gt;");
}
