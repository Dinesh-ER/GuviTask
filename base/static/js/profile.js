const container = document.querySelector(".main");

container.insertAdjacentHTML(
	"beforeend",
	`
	<div class="profile">
	<div class="profile__photo-wrap">
		<div class="profile__photo">
			<img src="{% static 'assets/images/profile.jpg' %}" alt="">
		</div>
		<p class="profile__username">${userData.username}</p>
	</div>
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
	<a href=${window.location.href + "edit/"} class="main__redirect"><button>Edit profile</button></a>
`
);
