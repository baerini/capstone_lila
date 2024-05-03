const messageDiv = document.getElementById('message');

messageDiv.addEventListener('focus', function() {
if (this.textContent === 'Enter your message') {
    this.textContent = '';
}
});

messageDiv.addEventListener('blur', function() {
    if (this.textContent === '') {
        this.textContent = 'Enter your message';
    }
});

