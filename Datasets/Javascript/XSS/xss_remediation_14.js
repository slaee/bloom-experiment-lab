var userProfile = sanitizeInput(document.URL);
document.write("<div>User Profile: " + userProfile + "</div>");

function sanitizeInput(input) {
  // Implement proper input sanitization logic here
  return input.replace(/</g, "&lt;").replace(/>/g, "&gt;");
}