// Paste AI Function:
function isValid(email) {
    return email.includes('@') && email.includes('.');
}

// Write your own "Unit Tests" quickly:
console.log(isValid("test@gmail.com")); // Should be true
console.log(isValid("testgmail.com"));  // Should be false
console.log(isValid("test@gmailcom"));  // Edge case: missing dot?