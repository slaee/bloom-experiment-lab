var userData = sanitizeInput(document.lastModified);
document.write("<div>Last modified: " + userData + "</div>");

function sanitizeInput(input) {
  // Implement proper input sanitization logic here
  return input.replace(/</g, "&lt;").replace(/>/g, "&gt;");
}
