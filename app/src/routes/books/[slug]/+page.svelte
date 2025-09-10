<script lang="ts">
	import { Rating } from 'flowbite-svelte';
	import {
		CardPlaceholder,
		ImagePlaceholder,
		ListPlaceholder,
		Skeleton,
		TestimonialPlaceholder,
		TextPlaceholder,
		VideoPlaceholder,
		WidgetPlaceholder
	} from 'flowbite-svelte';
	const images: any = import.meta.glob('$lib/images/covers/**.jpg', {
		eager: true,
		query: '?url',
		import: 'default'
	});
	export let data;
</script>

<h1 class="dark:text-white">{data.book.book}</h1>
<!-- <div>{data.book.goodreads}</div> -->
<div>
	<img
		src={images[`/src/lib/images/covers/${data.book.slug}.jpg`]}
		alt={data.book.book}
		class="size-full h-auto"
	/>
	<Rating id="rating" total={5} rating={data.book.goodreads}>
		<p slot="text" class="ms-2 text-sm font-medium text-gray-500 dark:text-gray-400">
			{data.book.goodreads} out of 5
		</p>
	</Rating>
</div>

<style></style>
