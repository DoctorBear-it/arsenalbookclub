<script lang="ts">
	import { Gallery, Video } from 'flowbite-svelte';
	import img from '$lib/hqg/ABC_HQG_1.gif';
	import { hqg_1, hqg_2, hqg_3, hqg_4, hqg_5, mov_1, mov_2, mov_3 } from '$lib/hqg';

	const images = [
		// { alt: 'the OG ABC HQG', src: img },
		{ alt: 'the OG ABC HQG', src: hqg_1 },
		{ alt: 'the OG ABC HQG', src: hqg_2 },
		{ alt: 'the OG ABC HQG', src: hqg_3 },
		{ alt: 'the OG ABC HQG', src: hqg_4 },
		{ alt: 'the OG ABC HQG', src: hqg_5 }
	];

	const movs = [
		{ alt: 'the OG ABC HQG', src: mov_1 },
		{ alt: 'the OG ABC HQG', src: mov_2 },
		{ alt: 'the OG ABC HQG', src: mov_3 }
	];
</script>

<Gallery items={images} class="grid-cols-2 gap-4 md:grid-cols-3" />

<Video src={mov_1} controls muted />
<Video src={mov_2} controls muted />
<Video src={mov_3} controls muted />

<style></style>
