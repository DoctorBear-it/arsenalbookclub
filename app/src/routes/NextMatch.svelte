<script lang="ts">
	import { Card } from 'flowbite-svelte';
	import arsenal from '$lib/logos/arsenal.webp';
	import bournemouth from '$lib/logos/bournemouth.webp';
</script>

<div class="col-span-1 row-span-1">
	<Card class="dark:bg-primary-900/75">
		<div>
			<h3 class=" text-2xl font-bold tracking-tight text-gray-900 dark:text-white">Next Match</h3>
		</div>
		<div class="flex flex-row items-center justify-evenly">
			<div>
				<img src={arsenal} alt="Arsenal" />
			</div>
			<div>
				<p class="font-bold text-gray-900 dark:text-white">V</p>
			</div>
			<div>
				<img src={bournemouth} alt="bournemouth" />
			</div>
		</div>
		<div class="flex flex-row items-center justify-evenly">
			<div>
				<p class="font-bold text-gray-900 dark:text-white">THU</p>
			</div>
			<div>
				<p class="font-bold text-gray-900 dark:text-white">JUL 25</p>
			</div>
			<div>
				<p class="font-bold text-gray-900 dark:text-white">@ 3:30</p>
			</div>
		</div>
	</Card>
</div>

<style>
</style>
