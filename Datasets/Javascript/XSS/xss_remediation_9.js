var userLocation = sanitizeInput(window.location.href);
document.write("<div>Current URL: " + userLocation + "</div>");

function sanitizeInput(input) {
  // Implement proper input sanitization logic here
  return input.replace(/</g, "&lt;").replace(/>/g, "&gt;");
}
