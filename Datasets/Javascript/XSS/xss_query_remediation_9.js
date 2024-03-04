var userLocation = sanitizeInput(getQueryParam('location'));
document.write("<div>Location: " + userLocation + "</div>");

function sanitizeInput(input) {
  // Implement proper input sanitization logic here
  return input.replace(/</g, "&lt;").replace(/>/g, "&gt;");
}
