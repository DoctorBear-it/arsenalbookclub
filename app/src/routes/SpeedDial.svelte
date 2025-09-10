<script>
	import { Avatar, SpeedDial, SpeedDialButton } from 'flowbite-svelte';
	import {
		ShareNodesSolid,
		PrinterSolid,
		DownloadSolid,
		FileCopySolid,
		HomeSolid,
		RedditSolid,
		RocketSolid,
		CartSolid
	} from 'flowbite-svelte-icons';
	import cannon from '$lib/images/cannon.svg';
</script>

<SpeedDial defaultClass="fixed end-6 bottom-6">
	<SpeedDialButton name="Wood" href="http://www.woodnshop.com/index.htm">
		<CartSolid class="h-6 w-6" />
	</SpeedDialButton>
	<SpeedDialButton name="Jam" href="https://www.spacejam.com/1996/">
		<RocketSolid class="h-6 w-6" />
	</SpeedDialButton>
	<SpeedDialButton name="$WSB$" href="https://www.reddit.com/r/wallstreetbets/">
		<RedditSolid class="h-6 w-6" />
	</SpeedDialButton>
	<SpeedDialButton name="Arsenal F.C." href="https://www.arsenal.com/">
		<!-- <HomeSolid class="h-6 w-6" /> -->
		<Avatar src={cannon} size="md" />
	</SpeedDialButton>
</SpeedDial>
