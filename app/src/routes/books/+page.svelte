<script lang="ts">
	import { Gallery } from 'flowbite-svelte';
	export let data;
	const images: any = import.meta.glob('$lib/images/covers/**.jpg', {
		eager: true,
		query: '?url',
		import: 'default'
	});
</script>

<h1 class="dark:text-white">On Our Bookshelf</h1>

<Gallery
	class="grid-cols-4 items-center justify-items-center gap-4"
	items={data.summaries}
	let:item
>
	<div class=" justify-items-center p-1">
		<!-- {#await import('') then { default: src }} -->
		<a href="/books/{item.slug}">
			<img
				src={images[`/src/lib/images/covers/${item.slug}.jpg`]}
				alt={item.book}
				class="size-full h-auto"
			/>
			<!-- {/await} -->
			{item.book}</a
		>
	</div>
</Gallery>

<!-- <ul>
	{#each data.summaries as { slug, book, goodreads }}
		<li>
			<enhanced:img src="/lib/images/covers/{slug}.jpg" alt={book} />
			<img src={images[`/src/lib/images/covers/${slug}.jpg`]} alt={book} />
			<a href="/books/{slug}">{book}</a>
		</li>
	{/each}
</ul> -->

<!-- <ul>
	{#each Object.entries(images) as [_path, module]}
		<enhanced:img src={module.default} alt="alt text" />
	{/each}
</ul> -->
