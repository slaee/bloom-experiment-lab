var userInput = sanitizeInput(window.location.hash.substr(1));
document.write("<p>" + userInput + "</p>");

function sanitizeInput(input) {
  // Implement proper input sanitization logic here
  return input.replace(/</g, "&lt;").replace(/>/g, "&gt;");
}
