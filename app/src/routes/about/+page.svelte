<script lang="ts">
	import jim_media from '$lib/images/JimMedia.png';

	import { Hr, P } from 'flowbite-svelte';
</script>

<svelte:head>
	<title>About</title>
	<meta name="description" content="About this app" />
</svelte:head>

<div class="text-column dark:text-white">
	<h1>By Arsenal Fans, For Book Fans.</h1>

	<!-- <h2>Meet the President</h2> -->
	<Hr classHr="w-48 h-1 mx-auto my-4 rounded md:my-10" />
	<span class="jim">
		<picture>
			<!-- <source srcset={welcome} type="image/webp" /> -->
			<img src={jim_media} alt="James 'Jim' Media" />
		</picture>
	</span>
	<Hr classHr="w-48 h-1 mx-auto my-4 rounded md:my-10" />
	<p>
		James "Jim" Media <br />
		President, The Arsenal Book Club
	</p>

	<!-- <p>
		This is a <a href="https://kit.svelte.dev">SvelteKit</a> app. You can make your own by typing the
		following into your command line and following the prompts:
	</p>

	<pre>npm create svelte@latest</pre>

	<p>
		The page you're looking at is purely static HTML, with no client-side interactivity needed.
		Because of that, we don't need to load any JavaScript. Try viewing the page's source, or opening
		the devtools network panel and reloading.
	</p>

	<p>
		The <a href="/sverdle">Sverdle</a> page illustrates SvelteKit's data loading and form handling. Try
		using it with JavaScript disabled!
	</p> -->
</div>
