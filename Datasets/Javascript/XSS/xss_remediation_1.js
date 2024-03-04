var userInput = sanitizeInput(location.hash.substring(1));
document.write("<div>" + userInput + "</div>");

function sanitizeInput(input) {
  // Implement proper input sanitization logic here
  return input.replace(/</g, "&lt;").replace(/>/g, "&gt;");
}
