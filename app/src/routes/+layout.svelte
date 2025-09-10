<script>
	import Header from './Header.svelte';
	import Navbar from './Navbar.svelte';
	import '../app.css';
	import Counter from './Counter.svelte';
	import SpeedDial from './SpeedDial.svelte';
	import Footer from './Footer.svelte';
</script>

<div class="app">
	<Navbar></Navbar>
	<!-- <Header></Header> -->

	<main>
		<div class="mt-20">
			<slot></slot>
		</div>
	</main>

	<SpeedDial />
	<footer>
		<!-- <Counter />
		<p class="text-center">
			Click the counter if you visited <br /> (we don't know how to program it)
		</p> -->
		<Footer />
		<!-- <p>visit <a href="https://kit.svelte.dev">kit.svelte.dev</a> to learn SvelteKit</p> -->
	</footer>
</div>

<style>
	.app {
		display: flex;
		flex-direction: column;
		min-height: 100vh;
	}

	main {
		flex: 1;
		display: flex;
		flex-direction: column;
		padding: 1rem;
		width: 100%;
		/* max-width: 64rem; */
		margin: 0 auto;
		box-sizing: border-box;
	}

	footer {
		display: flex;
		flex-direction: column;
		justify-content: center;
		align-items: center;
		padding: 12px;
	}

	footer a {
		font-weight: bold;
	}

	@media (min-width: 480px) {
		footer {
			padding: 12px 0;
		}
	}
</style>
