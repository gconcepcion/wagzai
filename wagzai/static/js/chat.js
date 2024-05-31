const input = document.getElementById('input');
const output = document.getElementById('output');
const sendMessageButton = document.getElementsByTagName('button')[0];

sendMessageButton.addEventListener('click', () => {
    const message = input.value;
    fetch('/chat', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({input: message}),
    })
        .then(response => response.json())
        .then(data => {
            output.innerHTML = data.response;
            input.value = '';
        });
});
