const name = document.querySelector('.name');
const email = document.querySelector('.email');
const message = document.querySelector('.message');

const contactForm = document.getElementById('contactForm');

const nameError = document.querySelector('.name-error');

const emailError = document.querySelector('.email-error');

const submitButton = document.querySelector('.submit-btn');

function validationTest(value){
	if (value == contactForm.name.value) {
		const regex = /^[A-Za-zА-Яа-я]+(?:\s[A-Za-zА-Яа-я]+)*$/;
		if (!regex.test(value)) {
			nameError.classList.remove('hidden');
			return false;
		} else {
			nameError.classList.add('hidden');
			return true;
		}
	}
	if (value == contactForm.email.value) {
		const regex = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
		if (!regex.test(value)) {
			emailError.classList.remove('hidden');
			return false;
		} else {
			emailError.classList.add('hidden');
			return true;
		}
	}
}

contactForm.addEventListener('input', (event) => {
	const input = event.target;
	if (input.name == 'name') {
		validationTest(contactForm.name.value)
	}
	if (input.name == 'email') {
		validationTest(contactForm.email.value)
	}

	const isCorrectName = validationTest(contactForm.name.value)
	const isCorrectEmail = validationTest(contactForm.email.value)
	submitButton.disabled = !(isCorrectName && isCorrectEmail);
})