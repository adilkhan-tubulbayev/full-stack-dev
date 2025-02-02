const menuToggle = document.getElementById("menu-toggle");
const menu = document.getElementById("menu");

menuToggle.addEventListener("click", () =>{
	menu.classList.toggle("hidden");
	menu.classList.toggle("flex");

	if (menu.classList.contains("flex")) {
    document.body.classList.toggle("overflow-hidden");
  } else {
    document.body.classList.remove("overflow-hidden");
  }
});