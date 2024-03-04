var userInput = sanitizeInput(getQueryParam('input'));
document.write("<div>" + userInput + "</div>");

function sanitizeInput(input) {
  // Implement proper input sanitization logic here
  return input.replace(/</g, "&lt;").replace(/>/g, "&gt;");
}
