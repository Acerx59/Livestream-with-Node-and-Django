var chatSocket = new WebSocket(
    'ws://' + window.location.host +
    '/ws/chat/' + roomName + '/');

chatSocket.onmessage = function (e) {
    var data = JSON.parse(e.data);
    var message = data['message'];

    // Append the message to the chat box
    document.getElementById('chat-history').value += (message + '\n');
};

function sendMessage() {
    var messageInputDom = document.getElementById('message-input');
    var message = messageInputDom.value;

    // Send message to WebSocket
    chatSocket.send(JSON.stringify({
        'message': message
    }));

    // Clear the message input
    messageInputDom.value = '';
}
