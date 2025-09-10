<script lang="ts">
	import { Drawer, Button, CloseButton, A, CheckboxButton } from 'flowbite-svelte';
	import { InfoCircleSolid, ArrowRightOutline } from 'flowbite-svelte-icons';
	import { sineIn } from 'svelte/easing';
	import { BarsOutline, BookOpenOutline, BookmarkSolid } from 'flowbite-svelte-icons';
	import {
		Sidebar,
		SidebarBrand,
		SidebarCta,
		SidebarDropdownItem,
		SidebarDropdownWrapper,
		SidebarGroup,
		SidebarItem,
		SidebarWrapper
	} from 'flowbite-svelte';
	import {
		ChartPieSolid,
		CartSolid,
		GridSolid,
		MailBoxSolid,
		UsersSolid,
		ShoppingBagSolid,
		ArrowRightToBracketOutline,
		EditOutline
	} from 'flowbite-svelte-icons';
	import { books } from '$lib/data/ratings';

	let spanClass = 'flex-1 ms-3 whitespace-nowrap';

	let hiddenBackdropFalse = true;
	let transitionParams = {
		x: -320,
		duration: 200,
		easing: sineIn
	};
	function handleClick() {
		hiddenBackdropFalse = !hiddenBackdropFalse;
	}
</script>

<div>
	<!-- <Button outline={true} class="!p-2" size="lg" on:click={handleClick}><BarsOutline /></Button> -->
	<!-- <Button
		outline={true}
		class="!p-2"
		size="lg"
		on:click={() => (hiddenBackdropFalse = !hiddenBackdropFalse)}><BarsOutline /></Button
	> -->
	<CheckboxButton
		outline={true}
		class="!p-2"
		size="lg"
		bind:checked={hiddenBackdropFalse}
		on:click={handleClick}
		><BookmarkSolid />
	</CheckboxButton>
</div>

<Drawer
	leftOffset="top-20 h-screen start-0"
	backdrop={false}
	transitionType="fly"
	{transitionParams}
	bind:hidden={hiddenBackdropFalse}
	id="sidebar1"
>
	<div class="flex items-center">
		<h5
			id="drawer-label"
			class="mb-4 inline-flex items-center text-base font-semibold text-gray-500 dark:text-gray-400"
		>
			<InfoCircleSolid class="me-2.5 h-5 w-5" />Listen Up, Nerds
		</h5>
		<CloseButton on:click={handleClick} class="mb-4 dark:text-white" />
	</div>
	<p class="mb-6 text-sm text-gray-500 dark:text-gray-400">
		Pick a book from the list or check out the <a
			href="/"
			class="text-primary-600 dark:text-primary-500 underline hover:no-underline"
		>
			current read.
		</a>
	</p>
	<!-- <div class="grid grid-cols-2 gap-4">
		<Button color="light" href="/">Learn more</Button>
		<Button href="/" class="px-4">Get access <ArrowRightOutline class="ms-2 h-5 w-5" /></Button>
	</div> -->
	<Sidebar>
		<SidebarWrapper divClass="overflow-y-auto py-4 px-3 rounded dark:bg-gray-800">
			<SidebarGroup>
				{#each books as { slug, book }}
					<SidebarItem label={book} href="/books/{slug}" />
				{/each}
				<!-- <SidebarItem label="Dashboard">
					<svelte:fragment slot="icon">
						<ChartPieSolid
							class="h-5 w-5 text-gray-500 transition duration-75 group-hover:text-gray-900 dark:text-gray-400 dark:group-hover:text-white"
						/>
					</svelte:fragment>
				</SidebarItem>
				<SidebarDropdownWrapper label="E-commerce">
					<svelte:fragment slot="icon">
						<CartSolid
							class="h-5 w-5 text-gray-500 transition duration-75 group-hover:text-gray-900 dark:text-gray-400 dark:group-hover:text-white"
						/>
					</svelte:fragment>
					<SidebarDropdownItem label="Products" />
					<SidebarDropdownItem label="Billing" />
					<SidebarDropdownItem label="Invoice" />
				</SidebarDropdownWrapper>
				<SidebarItem label="Kanban" {spanClass}>
					<svelte:fragment slot="icon">
						<GridSolid
							class="h-5 w-5 text-gray-500 transition duration-75 group-hover:text-gray-900 dark:text-gray-400 dark:group-hover:text-white"
						/>
					</svelte:fragment>
					<svelte:fragment slot="subtext">
						<span
							class="ms-3 inline-flex items-center justify-center rounded-full bg-gray-200 px-2 text-sm font-medium text-gray-800 dark:bg-gray-700 dark:text-gray-300"
						>
							Pro
						</span>
					</svelte:fragment>
				</SidebarItem>
				<SidebarItem label="Inbox" {spanClass}>
					<svelte:fragment slot="icon">
						<MailBoxSolid
							class="h-5 w-5 text-gray-500 transition duration-75 group-hover:text-gray-900 dark:text-gray-400 dark:group-hover:text-white"
						/>
					</svelte:fragment>
					<svelte:fragment slot="subtext">
						<span
							class="text-primary-600 bg-primary-200 dark:bg-primary-900 dark:text-primary-200 ms-3 inline-flex h-3 w-3 items-center justify-center rounded-full p-3 text-sm font-medium"
						>
							3
						</span>
					</svelte:fragment>
				</SidebarItem>
				<SidebarItem label="Users">
					<svelte:fragment slot="icon">
						<UsersSolid
							class="h-5 w-5 text-gray-500 transition duration-75 group-hover:text-gray-900 dark:text-gray-400 dark:group-hover:text-white"
						/>
					</svelte:fragment>
				</SidebarItem>
				<SidebarItem label="Products">
					<svelte:fragment slot="icon">
						<ShoppingBagSolid
							class="h-5 w-5 text-gray-500 transition duration-75 group-hover:text-gray-900 dark:text-gray-400 dark:group-hover:text-white"
						/>
					</svelte:fragment>
				</SidebarItem>
				<SidebarItem label="Sign In">
					<svelte:fragment slot="icon">
						<ArrowRightToBracketOutline
							class="h-5 w-5 text-gray-500 transition duration-75 group-hover:text-gray-900 dark:text-gray-400 dark:group-hover:text-white"
						/>
					</svelte:fragment>
				</SidebarItem>
				<SidebarItem label="Sign Up">
					<svelte:fragment slot="icon">
						<EditOutline
							class="h-5 w-5 text-gray-500 transition duration-75 group-hover:text-gray-900 dark:text-gray-400 dark:group-hover:text-white"
						/>
					</svelte:fragment>
				</SidebarItem> -->
			</SidebarGroup>
		</SidebarWrapper>
	</Sidebar>
</Drawer>
