document.getElementById('contactForm').addEventListener('submit', async function(event) {
  event.preventDefault(); // Остановить стандартное поведение формы

  const name = document.getElementById('name').value;
  const email = document.getElementById('email').value;
  const message = document.getElementById('message').value;

  const data = {
    name: name,
    email: email,
    message: message
  };

  try {
    const response = await fetch('http://127.0.0.1:8000/contact', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(data),
    });

    if (response.ok) {
      alert('Message sent successfully!');
    } else {
      alert('Failed to send message.');
    }
  } catch (error) {
    console.error('Error:', error);
    alert('An error occurred. Please try again later.');
  }
});
