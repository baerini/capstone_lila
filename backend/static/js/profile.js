const professionDiv = document.getElementById('profession');
const hobbyDiv = document.getElementById('hobby');

professionDiv.addEventListener('focus', function() {
if (this.textContent === 'e.g. student, accountant') {
    this.textContent = '';
}
});

professionDiv.addEventListener('blur', function() {
    if (this.textContent === '') {
        this.textContent = 'e.g. student, accountant';
    }
});

hobbyDiv.addEventListener('focus', function() {
if (this.textContent === 'e.g. hiking, painting') {
    this.textContent = '';
}
});

hobbyDiv.addEventListener('blur', function() {
    if (this.textContent === '') {
        this.textContent = 'e.g. hiking, painting';
    }
});

function submit() {
    var profession = document.getElementById('profession').innerText;
    var hobby = document.getElementById('hobby').innerText;
    var fluent = document.querySelector('.fluent-active').innerHTML;
    var learning = document.querySelector('.learning-active').innerHTML;
    var level = document.querySelector('.level-active').innerHTML;
    
    level_int = 0;
    if(level=="beginner") {
        level_int = 1;
    }else if(level=="not very fluent") {
        level_int = 2;
    }else if(level=="already fluent"){
        level_int = 3;
    }

    var data = {
        profession: profession,
        hobby: hobby,
        fluent: fluent,
        learning: learning,
        level: level_int
    };

    current_url = window.location.href;
    fetch(current_url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    .then(response => {
        if (response.ok) {
            console.log(response)
            url = `/success`;
            window.location.href=url;
        } else {
            console.error('Error sending data');
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });
}

function fluentChangeStyle(button) {
    var buttons = document.querySelectorAll('.fluent');
    buttons.forEach(function(btn) {
        btn.classList.remove('fluent-active');
    });

    button.classList.add('fluent-active');
}

function learningChangeStyle(button) {
    var buttons = document.querySelectorAll('.learning');
    buttons.forEach(function(btn) {
        btn.classList.remove('learning-active');
    });

    button.classList.add('learning-active');
}

function levelChangeStyle(button) {
    var buttons = document.querySelectorAll('.fluent-button');
    buttons.forEach(function(btn) {
        btn.classList.remove('level-active');
    });

    button.classList.add('level-active');
}