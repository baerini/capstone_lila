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

function handleClick(event, userId, rating, type) {
    event.preventDefault();
    sendRating(userId, rating);
    
    const badImg = document.getElementById(`bad-${userId}`);
    const justImg = document.getElementById(`just-${userId}`);
    const smileImg = document.getElementById(`smile-${userId}`);
    
    if (type === 'bad') {
        toggleImage(badImg, 'bad');
        justImg.src = "/static/img/just-1.png";
        smileImg.src = "/static/img/smile-1.png";
    } else if (type === 'just') {
        toggleImage(justImg, 'just');
        badImg.src = "/static/img/bad-1.png";
        smileImg.src = "/static/img/smile-1.png";
    } else if (type === 'smile') {
        toggleImage(smileImg, 'smile');
        badImg.src = "/static/img/bad-1.png";
        justImg.src = "/static/img/just-1.png";
    }
}

function toggleImage(imgElement, type) {
    if (imgElement.src.includes(`${type}-1.png`)) {
        imgElement.src = `/static/img/${type}-2.png`;
    } else {
        imgElement.src = `/static/img/${type}-1.png`;
    }
}