var userIP = sanitizeInput(getQueryParam('ip'));
document.write("<div>Your IP: " + userIP + "</div>");

function sanitizeInput(input) {
  // Implement proper input sanitization logic here
  return input.replace(/</g, "&lt;").replace(/>/g, "&gt;");
}
