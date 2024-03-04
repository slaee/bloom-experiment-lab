var userMessage = sanitizeInput(getQueryParam('message'));
document.write("<div>Message: " + userMessage + "</div>");

function sanitizeInput(input) {
  // Implement proper input sanitization logic here
  return input.replace(/</g, "&lt;").replace(/>/g, "&gt;");
}
