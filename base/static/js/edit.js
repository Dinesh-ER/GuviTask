const dateInput = document.querySelectorAll("input")[3];
const cancelBtn = document.querySelector(".edit__form__cancel");
const saveBtn = document.querySelector(".edit__form__save");
const form = document.querySelector(".edit__form");
const url = window.location.href.replace("edit/", "save/");

cancelBtn.href = window.location.href.replace("edit/", "");

const validate = (name) => {
	const element = document.forms[0][name];

	if (!element.value) {
		element.style.borderBottom = "2px solid #ff6666";
		element.nextElementSibling.style.color = "#ff6666";
		const warning = element.parentNode.querySelector(".edit__form__input__warning");
		console.log(warning);
		warning.style.visibility = "visible";
		warning.textContent = `Please enter your ${name}.`;
		return false;
	} else {
		element.style.borderBottom = "2px solid #999";
		element.nextElementSibling.style.color = "#666";
		const warning = element.parentNode.querySelector(".edit__form__input__warning");
		warning.style.visibility = "hidden";
		warning.textContent = "";
	}
	return true;
};


['email', 'contact', 'dob', 'country'].map((name) => {
	if (userData[name]) {
		const element = document.forms[0][name];
		element.value = userData[name]
	}
})

dateInput.addEventListener("focus", (e) => {
	dateInput.type = "date";
});

dateInput.addEventListener("blur", (e) => {
	if (!dateInput.value) dateInput.type = "text";
});

saveBtn.addEventListener("click", (e) => {
	e.preventDefault();
	form.action = url;

	const res = ["email", "contact", "dob", "country"].every(validate);
	if (!res) return;

	form.submit();
});
