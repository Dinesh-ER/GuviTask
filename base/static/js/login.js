const form = document.querySelector(".login__form");
const submitBtn = document.querySelector(".login__form__submit");

const validate = (name) => {
	const element = document.forms[0][name];

	if (!element.value) {
		element.style.borderBottom = "2px solid #ff6666";
		element.nextElementSibling.style.color = "#ff6666";
		const warning = element.parentNode.querySelector(".login__form__input__warning");
		warning.style.visibility = "visible";
		warning.textContent = `Please enter your ${name}.`;
		return false;
	} else {
		element.style.borderBottom = "2px solid #999";
		element.nextElementSibling.style.color = "#666";
		const warning = element.parentNode.querySelector(".login__form__input__warning");
		warning.style.visibility = "hidden";
		warning.textContent = "";
	}
	return true;
};

submitBtn.addEventListener("click", (e) => {
	e.preventDefault();

	const res = ["username", "password"].every(validate);
	if (!res) return;

	let data = new FormData(form);

	fetch(url, {
		method: "post",
		body: data,
	})
		.then((res) => res.json())
		.then((data) => {
			error = data.error;
			msg = data.msg;

			if (error) {
				let element;
				if (error == "user") {
					element = document.forms[0]["username"];
				} else {
					element = document.forms[0]["password"];
				}
				element.style.borderBottom = "2px solid #ff6666";
				element.nextElementSibling.style.color = "#ff6666";
				const warning = element.parentNode.querySelector(".login__form__input__warning");
				warning.style.visibility = "visible";
				warning.textContent = msg;
			} else {
				form.submit();
			}
		})
		.catch((err) => {
			console.log(err);
		});
});
