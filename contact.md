---
layout: default
title: Contact
---

# Contact

<form action="https://api.staticforms.xyz/submit" method="post" id="contact-form">
	<input type="hidden" name="accessKey" value="acae2770-b574-49b9-82a4-41644158490e">
	<div class="field">
		<div class="control">
		<textarea class="textarea" name="message" placeholder="Message" required></textarea>
		</div>
	</div>
	<div class="field">
		<div class="control">
		<input class="input" type="email" name="email" placeholder="Email" required>
		</div>
	</div>
	<button class="button is-primary" type="Submit">Submit</button>
</form>

<div class="social-links">

<a href="https://x.com/jimmammoth" target="_blank">
	<i class="fa-brands fa-x-twitter"></i>
	<span class="handle">@jimmammoth</span>
</a>

<a href="https://www.instagram.com/jimmammoth" target="_blank">
	<i class="fa-brands fa-instagram fa-lg"></i>
	<span class="handle">@jimmammoth</span>
</a>

<a href="https://www.snapchat.com/add/jimmammoth" target="_blank">
	<i class="fa-brands fa-snapchat fa-lg"></i>
	<span class="handle">@jimmammoth</span>
</a>

<a href="https://github.com/jmwoo" target="_blank">
	<i class="fa-brands fa-github"></i>
	<span class="handle">@jmwoo</span>
</a>

<div>

<script>
document.getElementById("contact-form").addEventListener("submit", function (event) {
	event.preventDefault();

	fetch('https://api.staticforms.xyz/submit', {
		method: 'POST',
		body: new FormData(event.target),
		headers: {
			'Accept': 'application/json'
		}
	})
	.then(response => response.json())
	.then(result => {
		alert(JSON.stringify(result))
	})
	.catch(error => {
		// Handle any errors
		alert('An error occurred: ' + error)
	})
})
</script>