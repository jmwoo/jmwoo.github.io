---
layout: default
title: About
---

<img src="https://imgur.com/BwUfdDc.jpg" alt="jimmammoth" style="max-width: 50%"/>

I love making things, especially software. I write code to solve problems, yet I believe that the best solution requires no code at all.
Creating things that people love brings me joy.

I love technology like robots, computers, and artificial intelligence. My love for computers began with a Macintosh in the early '90s. MacBooks are my favorite, but I use and like Windows and Linux. Raspberry Pis are really cool!

<img src="https://i.imgur.com/tRKlsCo.jpg" alt="coding" style="max-width: 50%"/>

<p>
	I have a son who is <span id="son-age">x</span> old. He’s the greatest thing that’s ever happened to me.
</p>

<img src="https://i.imgur.com/Ailg6dU.jpeg" alt="son" style="max-width: 50%"/>

I enjoy working out. I like the way it makes me feel and look.  
Check out my current [diet](/diet) and [training plan](/training).

<img src="https://i.imgur.com/r91EP3k.jpg" alt="gym" style="max-width: 50%"/>

I love owning a home and sculpting it to fit my tastes exactly. I strive for a home that is safe, functional, and a joy to live in. I like to care for quality things to make them last. I enjoy lawns, vegetable gardens, fruit trees, backyard chicken amd flowers. I like controlling my sprinklers and AC with an app.

Animals hold a special place in my heart. I've had a dog for most of my life and I've raised chickens (with plans to get more soon). One day I want to get a cat. I enjoy zoos, aquariums, nature, and safaris. I’ve seen elephants, rhinos, hippos and leapords in the wild. I was once bitten by a lion cub.

<img src="https://i.imgur.com/SnEMQZj.gif" alt="gym" style="max-width: 50%"/>

I grew up in Utah and have a deep love for the mountains. I enjoy snow skiing and water sports like boating, wakeboarding, and skiing. I’ve also lived in San Diego while working for the navy and absolutely love it there. The ocean and beach are majestic.  I hope to buy a second home in San Diego someday.

<img src="https://i.imgur.com/m9XQcjv.jpg" alt="skiing" style="max-width: 50%"/>
<img src="https://i.imgur.com/xNiPG3K.jpg" alt="beach" style="max-width: 50%"/>

I’m a huge fan of (electric)
vehicles. I have an e-bike and a segway that I LOVE to ride.  My next goal is to get an electric car and, eventually, a passenger drone.

<img src="https://i.imgur.com/qZOpZfD.jpg" alt="bike" style="max-width: 50%"/>

Movies are a bit challenging for me to sit through, but here are some of my favorites (in no particular order):

- The Matrix
- 3:10 to Yuma
- Gladiator
- A Knight’s Tale
- The Lion King (1994 version)
- The Greatest Showman
- Saving Private Ryan
- MacGruber
- Schindler’s List
- The Green Mile
- 90s Adam Sandler (Happy Gilmore, Billy Madison, The Waterboy)
- 90s Jim Carrey (Ace Ventura, The Mask, Dumb and Dumber)

On the other hand, I LOVE YouTube. I enjoy long-form interviews with interesting people (like Lex Fridman), as well as murder mysteries, forensics, and detective work. Here are some of my favorites:

<div class="video-block">
	<iframe class="video-embed" src="https://www.youtube.com/embed/DxREm3s1scA?si=VORsPq2g2srpUp0-" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
	<iframe class="video-embed" src="https://www.youtube.com/embed/I845O57ZSy4?si=pD06lt6ctOrFq0el" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
	<iframe class="video-embed" src="https://www.youtube.com/embed/L_Guz73e6fw?si=prhIBSPUt45Cm-n8" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
	<iframe class="video-embed" src="https://www.youtube.com/embed/uerSx5WfKoc?si=RRwUwHum9kavZ7-1" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
	<iframe class="video-embed" src="https://www.youtube.com/embed/xVxfI7Wv4Rg?si=1B1XbXH2igYGnAcm" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
	<iframe class="video-embed" src="https://www.youtube.com/embed/VISVshpMg6s?si=yLoU450Po7alobSy" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</div>

I admire Elon Musk, the GOAT entrepreneur and internet troll. I look up to builders of all kinds who can take ideas and make them a reality.

I want to understand the world as much as possible. I would like to make it a better place and enjoy my precious time while I'm here.


<script>
        document.addEventListener('DOMContentLoaded', function () {
            const birthDate = new Date(Date.UTC(2022, 2, 11, 8, 0, 0)); // March 11, 2022, 1:00 AM MST (UTC-7)
			const now = new Date();
        
			// Calculate decimal age
			const ageInMilliseconds = now.getTime() - birthDate.getTime();
			const ageInYears = ageInMilliseconds / (1000 * 60 * 60 * 24 * 365.25);
			const decimalAge = ageInYears.toFixed(2);
			
			// Calculate years, months, days
			let years = now.getUTCFullYear() - birthDate.getUTCFullYear();
			let months = now.getUTCMonth() - birthDate.getUTCMonth();
			let days = now.getUTCDate() - birthDate.getUTCDate();

			if (days < 0) {
				months--;
				days += new Date(now.getUTCFullYear(), now.getUTCMonth(), 0).getUTCDate();
			}
			if (months < 0) {
				years--;
				months += 12;
			}

			const ageString = `${years} year${years !== 1 ? 's' : ''}, ${months} month${months !== 1 ? 's' : ''}, and ${days} day${days !== 1 ? 's' : ''}`;
			const fullAgeString = `${ageString} (${decimalAge} years)`;
			
			document.getElementById('son-age').textContent = fullAgeString;
        });
    </script>