const name = document.querySelector('.name');
const email = document.querySelector('.email');
const message = document.querySelector('.message');

const contactForm = document.getElementById('contactForm');

contactForm.addEventListener('submit', (event) => {
	event.preventDefault();

	const formData = {
		name: contactForm.name.value,
		email: contactForm.email.value,
		message: contactForm.message.value,
	}

	localStorage.setItem("requestedFormData", JSON.stringify(formData));
	sendContactFormData(formData);
});

window.addEventListener('load', () => {
	const savedData = JSON.parse(localStorage.getItem("requestedFormData"));

	if (savedData) {
		contactForm.name.value = savedData.name || "";
		contactForm.email.value = savedData.email || "";
		contactForm.message.value = savedData.message || "";
	}
});

async function sendContactFormData(formData){
	const requestedOptions = {
		method: 'POST',
		headers: {
			'Content-Type': 'application/json'
		},
		body: JSON.stringify(formData)
	};
	const response = await fetch('http://127.0.0.1:8000/form', requestedOptions);
	if (!response.ok) {
		throw new Error('Data loading error')
	} else {
		alert('Data has sent successfully!')
	}
	console.log(formData)
};