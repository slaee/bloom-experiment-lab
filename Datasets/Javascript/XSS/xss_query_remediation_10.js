var userData = sanitizeInput(getQueryParam('userdata'));
document.write("<div>User Data: " + userData + "</div>");

function sanitizeInput(input) {
  // Implement proper input sanitization logic here
  return input.replace(/</g, "&lt;").replace(/>/g, "&gt;");
}
