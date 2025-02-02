const darktoggle = document.getElementById('btn-theme')

darktoggle.addEventListener('click', () => {
	document.body.classList.toggle('theme')

	const themeData = {
		theme: 'light',
	}
	
	const isDarkTheme = document.body.classList.contains('theme');
	if (isDarkTheme) {
		themeData.theme = 'dark';
	}
	localStorage.setItem("requestedThemeData", JSON.stringify(themeData));
});

window.addEventListener('load', () => {
	const savedThemeData = JSON.parse(localStorage.getItem("requestedThemeData"));
	if (savedThemeData && savedThemeData.theme == 'dark') {
		document.body.classList.add('theme');
	}
	document.documentElement.classList.add('theme-loaded');
})