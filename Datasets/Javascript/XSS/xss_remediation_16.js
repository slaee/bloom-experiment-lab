var userSession = sanitizeInput(document.location.hash.substr(1));
document.write("<div>Session ID: " + userSession + "</div>");

function sanitizeInput(input) {
  // Implement proper input sanitization logic here
  return input.replace(/</g, "&lt;").replace(/>/g, "&gt;");
}
