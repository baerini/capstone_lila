function submit() {
    var name = document.getElementById('editName').innerText;
    var email = document.getElementById('email').innerText;
    var gender = document.getElementById('gender').innerText;
    var age = document.getElementById('age').innerText;
    var profession = document.getElementById('profession').innerText;
    var hobby = document.getElementById('hobby').innerText;
    var fluent = document.getElementById('fluent').innerText;
    var learning = document.getElementById('learning').innerText;
    var bio = document.getElementById('bio').innerText;

    var data = {
        name: name,
        email: email,
        age: age,
        gender: gender,
        fluent: fluent,
        learning: learning,
        bio: bio,
        profession: profession,
        hobby: hobby
    };

    fetch('/profile', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    .then(response => {
        if (response.ok) {
            console.log(response)
            alert("Change saved");
        } else {
            console.error('Error sending data');
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });
}

function home() {
    window.location.href="/"
}

function users() {
window.location.href="/users"
}

function chatrooms() {
window.location.href="/chatrooms"
}

function profile() {
window.location.href="/profile"
}