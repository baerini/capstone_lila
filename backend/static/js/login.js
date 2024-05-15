const idDiv = document.getElementById('id');
const pwInput = document.getElementById('pw');

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

pwInput.addEventListener('focus', function() {
    if (this.value === '') {
        this.placeholder = '';
    }
});

pwInput.addEventListener('blur', function() {
    if (this.value === '') {
        this.placeholder = 'password';
    }
});


function submit() {
    var id = document.getElementById('id').innerText;
    var pw = document.getElementById('pw').value;

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
