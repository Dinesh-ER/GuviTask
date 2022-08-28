const form = document.querySelector(".register__form");
const submitBtn = document.querySelector(".register__form__submit");

const validate = (name) => {
	const element = document.forms[0][name];

	if (!element.value) {
		element.style.borderBottom = "2px solid #ff6666";
		element.nextElementSibling.style.color = "#ff6666";
		const warning = element.parentNode.querySelector('.register__form__input__warning')
		warning.style.visibility = "visible"
		warning.textContent = `Please enter your ${name}.`
		return false;
	} else {
		element.style.borderBottom = "2px solid #999";
		element.nextElementSibling.style.color = "#666";
		const warning = element.parentNode.querySelector('.register__form__input__warning')
		warning.style.visibility = "hidden"
		warning.textContent = ""
	}

	if (name == "email"){
		let pattern = /^\S+@\S+\.\S+$/
		if (!pattern.test(element.value)){
			element.style.borderBottom = "2px solid #ff6666";
			element.nextElementSibling.style.color = "#ff6666";
			const warning = element.parentNode.querySelector('.register__form__input__warning')
			warning.style.visibility = "visible"
			warning.textContent = "Enter a valid email."
			return false;
		} else {
			element.style.borderBottom = "2px solid #999";
			element.nextElementSibling.style.color = "#666";
			const warning = element.parentNode.querySelector('.register__form__input__warning')
			warning.style.visibility = "hidden"
			warning.textContent = ""
		}
	}

	if (name == "password"){
		let pattern = /^(?=.*[0-9])(?=.*[!@#$%^&*])[a-zA-Z0-9!@#$%^&*]{6,32}$/
		if (!pattern.test(element.value)){
			element.style.borderBottom = "2px solid #ff6666";
			element.nextElementSibling.style.color = "#ff6666";
			const warning = element.parentNode.querySelector('.register__form__input__warning')
			warning.style.visibility = "visible"
			warning.textContent = "Your password must contain at least one number and special character."
			return false;
		} else {
			element.style.borderBottom = "2px solid #999";
			element.nextElementSibling.style.color = "#666";
			const warning = element.parentNode.querySelector('.register__form__input__warning')
			warning.style.visibility = "hidden"
			warning.textContent = ""
		}
	}

	return true;
};

submitBtn.addEventListener("click", (e) => {
	e.preventDefault();

	const res = ['name', 'email', 'password'].every(validate)
	if (!res) return;

	form.submit()
});
