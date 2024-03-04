var userInput = sanitizeInput(getQueryParam('input'));
document.write("<p>" + userInput + "</p>");

function sanitizeInput(input) {
  // Implement proper input sanitization logic here
  return input.replace(/</g, "&lt;").replace(/>/g, "&gt;");
}
