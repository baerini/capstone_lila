function submit(element) {
    var user_id = element.id;

    var data = {
        id: user_id,
    };

    fetch('/create_chatroom', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    .then(response => {
        if (response.ok) {
            return response.json()
            // response에서 채팅방 아이디 받아야함
            // id = encodeURIComponent(id);
            // url = `/chatroom/` + id;
            // window.location.href=url;
        } else {
            console.error('Error sending data');
        }
    })
    .then(data => {
        console.log(data);
        console.log(data.id);
        url = `/chatroom/` + data.id;
        window.location.href=url;
    })
    .catch(error => {
        console.error('Error:', error);
    });
}

function sendRating(userId, rating) {
    fetch('/add_rating', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ to_user_id: userId, rating: rating })
    })
    .then(response => response.json())
    .then(data => {
        if (data.status === 'success') {
            alert("rating is reflected.");
        }
    })
    .catch((error) => {
        console.error('Error:', error);
    });
}

function handleClick(event, userId, rating) {
    event.preventDefault();
    sendRating(userId, rating);
}
