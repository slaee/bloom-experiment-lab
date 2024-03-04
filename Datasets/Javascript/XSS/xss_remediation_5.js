var pageTitle = sanitizeInput(document.title);
document.write("<h1>" + pageTitle + "</h1>");

function sanitizeInput(input) {
  // Implement proper input sanitization logic here
  return input.replace(/</g, "&lt;").replace(/>/g, "&gt;");
}