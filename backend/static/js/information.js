const idInput = document.getElementById('id');
const pwInput = document.getElementById('pw');
const nameInput = document.getElementById('name');
const ageInput = document.getElementById('age');

idInput.addEventListener('focus', function() {
    if (this.value === '4~16 characters') {
        this.value = '';
    }
});

idInput.addEventListener('blur', function() {
    if (this.value === '') {
        this.value = '4~16 characters';
    }
});

pwInput.addEventListener('focus', function() {
    if (this.value === '') {
        this.placeholder = '';
    }
});

pwInput.addEventListener('blur', function() {
    if (this.value === '') {
        this.placeholder = '8~16 characters';
    }
});

nameInput.addEventListener('focus', function() {
    if (this.value === 'name') {
        this.value = '';
    }
});

nameInput.addEventListener('blur', function() {
    if (this.value === '') {
        this.value = 'name';
    }
});

ageInput.addEventListener('focus', function() {
    if (this.value === 'age') {
        this.value = '';
    }
});

ageInput.addEventListener('blur', function() {
    if (this.value === '') {
        this.value = 'age';
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

function handleSignupSubmit() {
    var id = idInput.value;
    var pw = pwInput.value;
    var name = nameInput.value;
    var age = ageInput.value;
    var genderElement = document.querySelector('.gender-active');
    var gender = genderElement ? genderElement.innerHTML : '';

    // 모든 입력이 비어있는지 확인
    if (!id || !pw || !name || !age || !genderElement) {
        alert('You forgot something!');
        return;
    }

    // 모든 오류 메시지를 담을 배열
    let errors = [];

    // 유저 아이디 검사
    if (!/^[a-zA-Z0-9]{4,16}$/.test(id)) {
        errors.push('You need to fulfill the user id condition.');
    }

    // 비밀번호 검사
    if (!/^[a-zA-Z0-9]{8,16}$/.test(pw)) {
        errors.push('You need to fulfill the password condition.');
    }

    // 이름 검사
    if (!/^[a-zA-Z]+$/.test(name)) {
        errors.push('Your name should only be in English.');
    }

    // 나이 검사
    if (!/^\d+$/.test(age)) {
        errors.push('Your age should only be in numbers.');
    }

    // 만약 오류가 있으면 모든 오류 메시지를 alert
    if (errors.length > 0) {
        alert(errors.join('\n'));
        return;
    }

    // 여기에서 회원가입 로직을 실행합니다.
    var data = { id: id, pw: pw, name: name, age: age, gender: gender };

    fetch('/signup', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    .then(response => {
        if (response.ok) {
            id = encodeURIComponent(id);
            window.location.href = `/signup_2/` + id;
        } else {
            console.error('Error sending data');
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });
}
