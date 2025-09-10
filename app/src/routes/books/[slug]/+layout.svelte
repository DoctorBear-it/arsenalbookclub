<script>
	export let data;
</script>

<div class="layout">
	<main>
		<slot />
	</main>

	<aside>
		<h2 class="dark:text-white">More books</h2>
		<ul>
			{#each data.summaries as { slug, book, goodreads }}
				<li>
					<a href="/books/{slug}">{book}</a>
				</li>
			{/each}
		</ul>
	</aside>
</div>

<style>
	@media (min-width: 640px) {
		.layout {
			display: grid;
			gap: 2em;
			grid-template-columns: 1fr 16em;
		}
	}
</style>
