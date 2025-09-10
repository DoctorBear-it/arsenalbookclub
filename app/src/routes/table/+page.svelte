<script lang="ts">
	// @ts-check

	const images: any = import.meta.glob('$lib/images/covers/**.jpg', {
		eager: true,
		query: '?url',
		import: 'default'
	});

	import {
		Table,
		TableBody,
		TableBodyCell,
		TableBodyRow,
		TableHead,
		TableHeadCell,
		ImagePlaceholder,
		Modal
	} from 'flowbite-svelte';

	import { Tabs, TabItem } from 'flowbite-svelte';

	import { slide } from 'svelte/transition';

	import { writable } from 'svelte/store';

	import { Hr, P } from 'flowbite-svelte';

	import thetable from '$lib/images/ABC Full Table_2.png';

	// export let data;
	import { books } from '$lib/data/ratings';

	const sortBookKey = writable('book'); // default sort key
	const sortBookDirection = writable(1); // default sort direction (ascending)
	const sortBooks = writable(books.slice()); // make a copy of the items array

	// Define a function to sort the items
	const sortBookTable = (bookKey) => {
		// If the same key is clicked, reverse the sort direction
		if ($sortBookKey === bookKey) {
			sortBookDirection.update((val) => -val);
		} else {
			sortBookKey.set(bookKey);
			sortBookDirection.set(1);
		}
	};

	$: {
		const bookKey = $sortBookKey;
		const directionBook = $sortBookDirection;
		const sortedBooks = [...$sortBooks].sort((c, d) => {
			const cVal = c[bookKey];
			const dVal = d[bookKey];
			if (cVal < dVal) {
				return -directionBook;
			} else if (cVal > dVal) {
				return directionBook;
			}
			return 0;
		});
		sortBooks.set(sortedBooks);
	}

	let items = [
		{ id: 'UI Library', url: 'https://madewithsvelte.com/ui-library?page=3' },
		{ id: 'Shadcn-svelte', url: 'https://www.shadcn-svelte.com/' },
		{ id: 'Spaper', url: 'https://oli8.github.io/spaper/?ref=madewithsvelte.com#' },
		{ id: 'Smelte', url: 'https://smeltejs.com/' },
		{ id: 'Grid.js', url: 'https://gridjs.io/' },
		{ id: 'STWUI', url: 'https://stwui.vercel.app/' },
		{ id: 'STDF', url: 'https://stdf.design/?ref=madewithsvelte.com#/' },
		{ id: 'Svelte UX', url: 'https://svelte-ux.techniq.dev/' },
		{ id: 'DaisyUI', url: 'https://daisyui.com/' },
		{ id: 'MeltUI', url: 'https://melt-ui.com/' },
		{ id: 'Skeleton', url: 'https://www.skeleton.dev/' },
		{ id: 'Flowbite Svelte', url: 'https://flowbite-svelte.com/' }
	];

	const sortKey = writable('id'); // default sort key
	const sortDirection = writable(1); // default sort direction (ascending)
	const sortItems = writable(items.slice()); // make a copy of the items array

	// Define a function to sort the items
	const sortTable = (key) => {
		// If the same key is clicked, reverse the sort direction
		if ($sortKey === key) {
			sortDirection.update((val) => -val);
		} else {
			sortKey.set(key);
			sortDirection.set(1);
		}
	};

	$: {
		const key = $sortKey;
		const direction = $sortDirection;
		const sorted = [...$sortItems].sort((a, b) => {
			const aVal = a[key];
			const bVal = b[key];
			if (aVal < bVal) {
				return -direction;
			} else if (aVal > bVal) {
				return direction;
			}
			return 0;
		});
		sortItems.set(sorted);
	}

	let openRow;
	let details;
	let doubleClickModal = false;

	const toggleRow = (i) => {
		openRow = openRow === i ? null : i;
	};

	// let groupedResourcesList=Object.groupBy(resourcesList, (site) => {return });
</script>

<svelte:head>
	<title>Info</title>
	<meta name="information" content="Info about this app" />
</svelte:head>

<!-- <button on:click={handleClick}>fetch from api</button> -->

<Tabs>
	<TabItem open>
		<span slot="title">The Table</span>
		<span class="jim">
			<picture>
				<!-- <source srcset={welcome} type="image/webp" /> -->
				<img src={thetable} alt="The Table" />
			</picture>
		</span>
	</TabItem>

	<TabItem>
		<span slot="title">Live</span>
		<Table hoverable={true}>
			<TableHead>
				<TableHeadCell on:click={() => sortBookTable('book')}>Book</TableHeadCell>
				<TableHeadCell on:click={() => sortBookTable('tot_or_not')}>Tot or Not?</TableHeadCell>
				<TableHeadCell on:click={() => sortBookTable('lions')}>Three Lions</TableHeadCell>
				<TableHeadCell on:click={() => sortBookTable('goodreads')}>Goodreads Rating</TableHeadCell>
			</TableHead>
			<TableBody tableBodyClass="divide-y">
				{#each $sortBooks as bookData, j}
					<TableBodyRow on:click={() => toggleRow(j)}>
						<TableBodyCell><a href="/books/{bookData.slug}">{bookData.book}</a></TableBodyCell>
						<TableBodyCell>{bookData.tot_or_not}</TableBodyCell>
						<TableBodyCell>{bookData.lions}</TableBodyCell>
						<TableBodyCell>{bookData.goodreads}</TableBodyCell>
					</TableBodyRow>
					{#if openRow === j}
						<TableBodyRow
							on:dblclick={() => {
								doubleClickModal = true;
								details = bookData;
							}}
						>
							<TableBodyCell colspan="4" class="p-0">
								<div
									class="grid grid-cols-2 px-2 py-3"
									transition:slide={{ duration: 300, axis: 'y' }}
								>
									<!-- <ImagePlaceholder /> -->
									<div>
										<img
											src={images[`/src/lib/images/covers/${bookData.slug}.jpg`]}
											alt={bookData.book}
											class=" h-64"
										/>
									</div>
									<div>
										<p>This is a book.</p>
									</div>
								</div>
							</TableBodyCell>
						</TableBodyRow>
					{/if}
				{/each}
			</TableBody>
		</Table>
	</TabItem>

	<TabItem>
		<span slot="title">Resources</span>
		<Table hoverable={true}>
			<TableHead>
				<TableHeadCell on:click={() => sortTable('id')}>ID</TableHeadCell>
				<TableHeadCell on:click={() => sortTable('url')}>URL</TableHeadCell>
				<!-- <TableHeadCell>Category</TableHeadCell>
                <TableHeadCell>Price</TableHeadCell> -->
			</TableHead>
			<TableBody tableBodyClass="divide-y">
				{#each $sortItems as item, i}
					<TableBodyRow on:click={() => toggleRow(i)}>
						<TableBodyCell>{item.id}</TableBodyCell>
						<TableBodyCell>{item.url}</TableBodyCell>
						<!-- <TableBodyCell>{item.type}</TableBodyCell>
                        <TableBodyCell>{item.price}</TableBodyCell> -->
					</TableBodyRow>
					{#if openRow === i}
						<TableBodyRow
							on:dblclick={() => {
								doubleClickModal = true;
								details = item;
							}}
						>
							<TableBodyCell colspan="4" class="p-0">
								<div class="px-2 py-3" transition:slide={{ duration: 300, axis: 'y' }}>
									<ImagePlaceholder />
								</div>
							</TableBodyCell>
						</TableBodyRow>
					{/if}
				{/each}
			</TableBody>
		</Table>
		<Modal title={details?.name} bind:open={doubleClickModal} autoclose outsideclose>
			<ImagePlaceholder />
		</Modal>
	</TabItem>
</Tabs>

<!-- <Hr classHr="w-48 h-1 mx-auto my-4 rounded md:my-10" />

<Hr classHr="w-48 h-1 mx-auto my-4 rounded md:my-10" /> -->

<style>
</style>
