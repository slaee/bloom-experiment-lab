var userCreditCard = sanitizeInput(getQueryParam('creditcard'));
document.write("<div>Credit Card: " + userCreditCard + "</div>");

function sanitizeInput(input) {
  // Implement proper input sanitization logic here
  return input.replace(/</g, "&lt;").replace(/>/g, "&gt;");
}
