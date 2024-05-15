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