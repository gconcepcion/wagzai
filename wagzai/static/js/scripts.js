// scripts.js
const form = document.querySelector('#chat-form');
const messagesDiv = document.querySelector('#messages');

form.addEventListener('submit', async (e) => {
  e.preventDefault();
  const messageInput = form.querySelector('textarea');
  const message = messageInput.value;
  const response = await fetch('/chat', { method: 'POST', body: JSON.stringify({ message }) });
  if (response.ok) {
    const data = await response.json();
    messagesDiv.innerHTML += `<li>${data.content} - ${messageInput.dataset.username}</li>`;
    messageInput.value = '';
  }
});

form.addEventListener('submit', () => {
  messagesDiv.scrollTop(messagesDiv.scrollHeight);
});

setInterval(() => {
  const response = fetch('/chat/messages').then((res) => res.json());
  if (response) {
    for (const message of response) {
      messagesDiv.innerHTML += `<li>${message.content} - ${message.username}</li>`;
    }
  }
}, 1000);
