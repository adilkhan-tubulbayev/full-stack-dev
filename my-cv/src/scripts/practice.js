const projectContainer = document.getElementById('project-container');

const contactForm = document.querySelector('.contactForm');

const createButton = document.querySelector('.createButton');
const headerTip = document.querySelector('.header-tip');

function validationName(name){
	const regex = /^[A-Za-zА-Яа-я\s]+$/
	if (regex.test(name)) return name;
	else return false;
}

const formName = document.getElementById('name');
const errorText = document.querySelector('.errorText');
errorText.style.margin = '0px';
// errorText.style.padding = '0px';
errorText.style.display = 'none';


window.addEventListener('load', () => {
	const savedData = JSON.parse(localStorage.getItem("projectRequestData"));

	if (savedData) {
		contactForm.name.value = savedData.name || "";
		contactForm.description.value = savedData.description || "";
	}
	

	
});

contactForm.addEventListener('submit', (event) => {
	event.preventDefault();
	// createButton.disabled = true;
	const formData = {
		name: contactForm.name.value,
		description: contactForm.description.value,
	}

	localStorage.setItem("projectRequestData", JSON.stringify(formData));
	headerTip.style.display = 'none';
	if (validationName(contactForm.name.value) === false) {
		formName.style.borderColor = 'red';
		errorText.style.color = 'red';
		errorText.style.display = 'block';
		console.log('Error. Name must be contain letter only!!!');
	}
	else {
		formName.style.borderColor = 'green';
		const projectCard = document.createElement('div');
		projectCard.className = "project-card";
		projectCard.innerHTML = `
			<h2>${contactForm.name.value}</h2>
			<p>${contactForm.description.value}</p>
			<button class="delete-project">Delete</button>
		`;
		
		const deleteProject = projectCard.querySelector(".delete-project");
		deleteProject.addEventListener("click", () => {
			projectCard.remove();
		});

		projectContainer.appendChild(projectCard);
		contactForm.reset();

		deleteButton.addEventListener('click', () => {
			projectCard.remove();
			headerTip.style.display = 'block';
		});

		// localStorage.removeItem("projectRequestData");
	}
});
