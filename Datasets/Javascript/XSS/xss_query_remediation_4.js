var userInput = sanitizeInput(getQueryParam('data'));
document.write("<span>" + userInput + "</span>");

function sanitizeInput(input) {
  // Implement proper input sanitization logic here
  return input.replace(/</g, "&lt;").replace(/>/g, "&gt;");
}
