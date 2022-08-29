const container = document.querySelector(".profile");


const usernameField = document.querySelector(".profile__username")
usernameField.textContent = userData.username

document.querySelector(".edit-profile-btn").href = window.location.href + "edit/"

container.insertAdjacentHTML(
	"beforeend",
	`
	<div class="profile__details">
		<div class="profile__details__email">
			<strong>Email</strong>
			<span>${userData.email}</span>
		</div>
		<div class="profile__details__contact">
			<strong>Contact</strong>
			<span>${userData.contact}</span>
		</div>
		<div class="profile__details__dob">
			<strong>DOB</strong>
			<span>${userData.dob}</span>
		</div>
		<div class="profile__details__age">
			<strong>Age</strong>
			<span>${userData.age}</span>
		</div>
		<div class="profile__details__country">
			<strong>Country</strong>
			<span>${userData.country}</span>
		</div>
	</div>
	</div>
`
);
