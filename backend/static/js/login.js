const idDiv = document.getElementById('id');
const pwDiv = document.getElementById('pw');

idDiv.addEventListener('focus', function() {
    if (this.textContent === 'user id') {
        this.textContent = '';
    }
});

idDiv.addEventListener('blur', function() {
    if (this.textContent === '') {
        this.textContent = 'user id';
    }
});

pwDiv.addEventListener('focus', function() {
if (this.textContent === 'password') {
    this.textContent = '';
}
});

pwDiv.addEventListener('blur', function() {
    if (this.textContent === '') {
        this.textContent = 'password';
    }
});

function submit() {
    var id = document.getElementById('id').innerText;
    var pw = document.getElementById('pw').innerText;

    var data = {
        id: id,
        pw: pw
    };

    fetch('/login', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    .then(response => {
        if (response.ok) {
            console.log(response)
            url = `/`;
            window.location.href=url;
        } else {
            console.error('Error sending data');
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });
}