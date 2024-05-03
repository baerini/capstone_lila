const idDiv = document.getElementById('id');
const pwDiv = document.getElementById('pw');
const nameDiv = document.getElementById('name');
const ageDiv = document.getElementById('age');

idDiv.addEventListener('focus', function() {
    if (this.textContent === '4~16 characters') {
        this.textContent = '';
    }
});

idDiv.addEventListener('blur', function() {
    if (this.textContent === '') {
        this.textContent = '4~16 characters';
    }
});

pwDiv.addEventListener('focus', function() {
if (this.textContent === '8~16 characters') {
    this.textContent = '';
}
});

pwDiv.addEventListener('blur', function() {
    if (this.textContent === '') {
        this.textContent = '8~16 characters';
    }
});

nameDiv.addEventListener('focus', function() {
if (this.textContent === 'name') {
    this.textContent = '';
}
});

nameDiv.addEventListener('blur', function() {
    if (this.textContent === '') {
        this.textContent = 'name';
    }
});

ageDiv.addEventListener('focus', function() {
if (this.textContent === 'age') {
    this.textContent = '';
}
});

ageDiv.addEventListener('blur', function() {
    if (this.textContent === '') {
        this.textContent = 'age';
    }
});

function genderChangeStyle(button) {
    var buttons = document.querySelectorAll('.gender-button');
    buttons.forEach(function(btn) {
        btn.classList.remove('gender-active');
    });

    button.classList.add('gender-active');
    var activeElement = document.querySelector('.gender-active');
    console.log(activeElement.innerHTML);
}

function submit() {
    var id = document.getElementById('id').innerText;
    var pw = document.getElementById('pw').innerText;
    var name = document.getElementById('name').innerText;
    var age = document.getElementById('age').innerText;
    var gender = document.querySelector('.gender-active').innerHTML;

    var data = {
        id: id,
        pw: pw,
        name: name,
        age: age,
        gender: gender
    };

    fetch('/signup', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    .then(response => {
        if (response.ok) {
            console.log(response)
            id = encodeURIComponent(id);
            url = `/signup_2/` + id;
            window.location.href=url;
        } else {
            console.error('Error sending data');
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });
}

