var userMessage = sanitizeInput(document.referrer);
document.write("<div>Referrer: " + userMessage + "</div>");

function sanitizeInput(input) {
  // Implement proper input sanitization logic here
  return input.replace(/</g, "&lt;").replace(/>/g, "&gt;");
}
