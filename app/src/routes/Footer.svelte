<script lang="ts">
	import {
		Footer,
		FooterLinkGroup,
		FooterLink,
		FooterBrand,
		FooterIcon,
		FooterCopyright
	} from 'flowbite-svelte';
	import { FacebookSolid, GithubSolid, DiscordSolid, TwitterSolid } from 'flowbite-svelte-icons';
	import Counter from './Counter.svelte';
</script>

<Footer footerType="logo">
	<div class="sm:flex sm:items-end sm:justify-between">
		<!-- <FooterBrand href="https://flowbite.com" src="/images/flowbite-svelte-icon-logo.svg" alt="Flowbite Logo" name="Flowbite" /> -->
		<div class="box-content h-16 w-32">
			<Counter />
		</div>
		<!-- <Counter /> -->

		<FooterLinkGroup
			ulClass="flex flex-wrap items-center mb-6 text-sm text-gray-500 sm:mb-0 dark:text-gray-400"
		>
			<FooterLink href="/">About</FooterLink>
			<FooterLink href="/">Privacy Policy</FooterLink>
			<FooterLink href="/">Licensing</FooterLink>
			<FooterLink href="/">Contact</FooterLink>
		</FooterLinkGroup>
	</div>
	<hr class="my-6 border-gray-200 sm:mx-auto lg:my-8 dark:border-gray-700" />
	<div class="bg-gray-700 px-4 py-6 md:flex md:items-center md:justify-between">
		<FooterCopyright
			spanClass="text-sm text-gray-300 sm:text-center"
			href="/"
			by="The Arsenal Book Club™"
		/>
		<div class="mt-4 flex space-x-6 sm:justify-center md:mt-0 rtl:space-x-reverse">
			<FooterIcon href="https://www.facebook.com/marketplace/london/">
				<FacebookSolid
					class="h-5 w-5 text-gray-500 hover:text-gray-900 dark:text-gray-500 dark:hover:text-white"
				/>
			</FooterIcon>
			<FooterIcon href="/">
				<DiscordSolid
					class="h-5 w-5 text-gray-500 hover:text-gray-900 dark:text-gray-500 dark:hover:text-white"
				/>
			</FooterIcon>
			<FooterIcon href="https://x.com/arsenalbookclub">
				<TwitterSolid
					class="h-5 w-5 text-gray-500 hover:text-gray-900 dark:text-gray-500 dark:hover:text-white"
				/>
			</FooterIcon>
			<FooterIcon href="https://github.com/DoctorBear-it/arsenalbookclub">
				<GithubSolid
					class="h-5 w-5 text-gray-500 hover:text-gray-900 dark:text-gray-500 dark:hover:text-white"
				/>
			</FooterIcon>
			<!-- <FooterIcon href="/">
				<Dribble />
			</FooterIcon> -->
		</div>
	</div>
</Footer>

<style>
</style>
