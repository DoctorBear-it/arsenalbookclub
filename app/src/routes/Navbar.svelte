<script lang="ts">
	import logo from '$lib/images/ABC_Profile_Pic.png';
	import { page } from '$app/stores';
	import { Navbar, NavBrand, NavLi, NavUl, NavHamburger } from 'flowbite-svelte';
	import { DarkMode } from 'flowbite-svelte';
	import { UserCircleOutline } from 'flowbite-svelte-icons';
	import Drawer from './Drawer.svelte';
	import { Button } from 'flowbite-svelte';
	import jim_media from '$lib/images/JimMedia.png';

	import {
		Avatar,
		Dropdown,
		DropdownHeader,
		DropdownItem,
		DropdownDivider,
		Tooltip
	} from 'flowbite-svelte';

	$: activeUrl = $page.url.pathname;
	let activeClass =
		'text-white bg-green-700 md:bg-transparent md:text-green-700 md:dark:text-white dark:bg-green-600 md:dark:bg-transparent';
	let nonActiveClass =
		'text-gray-700 hover:bg-gray-100 md:hover:bg-transparent md:border-0 md:hover:text-green-700 dark:text-gray-400 md:dark:hover:text-white dark:hover:bg-gray-700 dark:hover:text-white md:dark:hover:bg-transparent';
</script>

<header>
	<div>
		<Navbar class="fixed start-0 top-0 z-20 w-full border-b px-2 py-2.5 sm:px-4">
			<div class="corner">
				<Drawer />
			</div>
			<NavBrand href="/">
				<img src={logo} class="me-3 h-6 sm:h-9" alt="ABC Book Club Logo" />
				<span class="dark:text-red self-center whitespace-nowrap text-xl font-semibold"
					>The Arsenal Book Club</span
				>
			</NavBrand>
			<div class="flex items-center md:order-2">
				<Avatar id="avatar-menu" src={jim_media} />
				<DarkMode class="text-primary-500 dark:text-primary-600 border dark:border-gray-800" />
				<NavHamburger class1="w-full md:flex md:w-auto md:order-1" />
			</div>
			<Dropdown placement="bottom" triggeredBy="#avatar-menu">
				<DropdownHeader>
					<span class="block text-sm">Jim Media</span>
					<span class="block truncate text-sm font-medium">Jim.Media@gmail.com</span>
				</DropdownHeader>
				<DropdownItem>Dashboard</DropdownItem>
				<DropdownItem>Settings</DropdownItem>
				<DropdownItem>Earnings</DropdownItem>
				<DropdownDivider />
				<DropdownItem>Sign out</DropdownItem>
			</Dropdown>
			<!-- <NavHamburger /> -->
			<NavUl {activeClass} {nonActiveClass}>
				<NavLi href="/">Home</NavLi>
				<NavLi href="/about">About</NavLi>
				<NavLi href="/table">Table</NavLi>
				<NavLi href="/info">Fixtures</NavLi>
				<NavLi href="/books">Books</NavLi>
				<NavLi href="/404">Youth Leagues</NavLi>
				<NavLi href="/hqg">HQG</NavLi>
				<NavLi href="/sverdle">Sverdle</NavLi>
			</NavUl>
		</Navbar>
	</div>
</header>
