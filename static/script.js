function sendMessage() {
    var user_input = document.getElementById('user_input').value;
    // Add user message to chatbox
    var chatbox = document.getElementById('chatbox');
    var user_message = document.createElement('div');
    user_message.className = 'user-message';
    user_message.textContent = 'User: ' + user_input;
    chatbox.appendChild(user_message);
    // Send user message to server and get response
    fetch('/get?msg=' + user_input)
        .then(response => response.text())
        .then(data => {
            // Add bot response to chatbox
            var bot_message = document.createElement('div');
            bot_message.className = 'bot-message';
            bot_message.textContent = 'Bot: ' + data;
            chatbox.appendChild(bot_message);
        });
    // Clear user input
    document.getElementById('user_input').value = '';
}
