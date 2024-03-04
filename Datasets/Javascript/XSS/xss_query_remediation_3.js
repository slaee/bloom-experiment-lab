var errorMsg = sanitizeInput(getQueryParam('error'));
document.getElementById("error-message").textContent = errorMsg;

function sanitizeInput(input) {
  // Implement proper input sanitization logic here
  return input.replace(/</g, "&lt;").replace(/>/g, "&gt;");
}
