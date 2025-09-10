<script lang="ts">
	import Counter from './Counter.svelte';

	// import welcome_fallback from '$lib/images/TheABC_v2.png';
	import young_simba from '$lib/images/simba_young.png';
	import teen_simba from '$lib/images/simba_teen.svg';
	import adult_simba from '$lib/images/simba_adult.svg';
	import lion from '$lib/images/lion.png';
	import logo from '$lib/images/ABC_Profile_Pic.png';
	import color_logo from '$lib/images/ABC Logo_color.svg';
	import rw_logo from '$lib/images/ABC Logo_rw.svg';
	import current_book_cover from '$lib/images/covers/caves-of-steel.jpg';

	import {
		Timeline,
		TimelineItem,
		Activity,
		ActivityItem,
		Group,
		GroupItem,
		Marquee,
		Banner,
		Img
	} from 'flowbite-svelte';

	import { CalendarWeekSolid } from 'flowbite-svelte-icons';
	import { Hr, P } from 'flowbite-svelte';
	import { Rating, AdvancedRating, ScoreRating } from 'flowbite-svelte';

	import { Alert, Card } from 'flowbite-svelte';
	import Drawer from './Drawer.svelte';
	import NextMatch from './NextMatch.svelte';
</script>

<svelte:head>
	<title>Home</title>
	<meta name="description" content="Svelte demo app" />
</svelte:head>

<!-- <div class="m-2 flex-auto">
	<Alert dismissable>
		<span class="font-medium">Reading alert!</span>
		Read through chapter 10!
	</Alert>
</div> -->

<div class="grid min-h-screen grid-flow-row grid-cols-3 gap-4">
	<!--auto-rows-max grid-rows-flow-->
	<!-- <section> -->
	<div class="col-span-3 row-span-2 grid justify-items-center">
		<h1 class="dark:text-white">Welcome to Your New</h1>
		<img src={color_logo} alt="ABC Badge" class="object-cover" />
		<h1 class="dark:text-white">Home</h1>
	</div>

	<div class="col-span-3 row-span-1">
		<Marquee speed={1} hoverSpeed={0.5} class="py-16">
			<img class="h-16 w-16" alt="young Simba" src={young_simba} />
			<img class="h-8 w-16" alt="English lion" src={lion} />
			<img class="h-16 w-16" alt="teen Simba" src={teen_simba} />
			<img class="h-8 w-16" alt="English lion" src={lion} />
			<img class="h-16 w-16" alt="adult Simba" src={adult_simba} />
			<img class="h-8 w-16" alt="English lion" src={lion} />
		</Marquee>
	</div>
</div>

<div
	class="flex grid-flow-row justify-between gap-4 bg-transparent/50 bg-[length:60dvh] bg-fixed bg-center bg-no-repeat bg-blend-multiply"
	style="background-image:  url({rw_logo})"
>
	<div class="min-h-[calc(100dvh-73px)] grow">
		<!-- <h1 class="bg-primary-200 dark:bg-primary-900 dark:text-white">.</h1> -->
	</div>
	<aside class="float-right" style="width: 50dvh;">
		<Card padding="none" class="no-scrollbar relative h-dvh overflow-y-scroll object-cover">
			<a class="table" href="https://www.premierleague.com/tables#!">Premier League Table</a>
			<div
				id="scoreaxis-widget-243be"
				style="border-width:1px;border-color:rgba(0, 0, 0, 0.15);border-style:solid;border-radius:8px;padding:10px;background:rgb(255, 255, 255);width:100%;height:100%"
			>
				<iframe
					title="Table"
					id="Iframe"
					src="https://www.scoreaxis.com/widget/standings-widget/8?autoHeight=1&amp;inst=243be"
					style="height:100%;width:100%;border:none;transition:all 300ms ease "
				></iframe><script>
					window.addEventListener('DOMContentLoaded', (event) => {
						window.addEventListener(
							'message',
							(event) => {
								if (event.data.appHeight && '243be' == event.data.inst) {
									let container = document.querySelector('#scoreaxis-widget-243be iframe');
									container && (container.style.height = parseInt(event.data.appHeight) + 'px');
								}
							},
							!1
						);
					});
				</script>
			</div>
			<div style="font-size: 12px; font-family: Arial, sans-serif; text-align: left;">
				Data provided by <a target="_blank" href="https://www.scoreaxis.com/">Scoreaxis</a>
			</div>
			<!-- <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script> -->
		</Card>
	</aside>

	<aside class="" style="width: 50dvh;">
		<NextMatch />
	</aside>
	<aside class="" style="width: 50dvh;">
		<NextMatch />
	</aside>
	<aside class="float-right" style="width: 50dvh;">
		<Card padding="none" class="no-scrollbar relative h-dvh overflow-y-scroll object-cover">
			<a class="twitter-timeline" href="https://twitter.com/Arsenal?ref_src=twsrc%5Etfw"
				>Tweets by Arsenal</a
			> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
		</Card>
	</aside>
</div>

<h1 class="bg-primary-200 dark:bg-primary-900 dark:text-white">Current Book</h1>

<div class="grid-flow-rows flex justify-center gap-4 pt-20">
	<!-- bg-transparent/50 bg-contain bg-fixed bg-center bg-no-repeat bg-blend-multiply"
	style="background-image:  url({rw_logo}) -->
	<!-- <Drawer /> -->
	<!-- <div class="row-span-1"></div> -->

	<div class="row-span-1 justify-items-center">
		<!-- <Hr classHr="w-48 h-1 mx-auto my-4 rounded md:my-10" /> -->
		<h1 class="bg-primary-200 dark:bg-primary-900 dark:text-white">The Caves of Steel</h1>
		<img src={current_book_cover} alt="Current Book" class="max-w-96" />
	</div>
	<div class="row-span-1 pt-14">
		<Card class="!bg-yellow-400/90">
			<!----->
			<Timeline order="vertical">
				<TimelineItem title="Read through Chapter 10" date="July 23, 2024">
					<svelte:fragment slot="icon">
						<span
							class="bg-primary-200 dark:bg-primary-900 absolute -start-3 flex h-6 w-6 items-center justify-center rounded-full ring-8 ring-white dark:ring-white"
						>
							<CalendarWeekSolid class="text-primary-600 dark:text-primary-400 h-4 w-4" />
						</span>
					</svelte:fragment>
				</TimelineItem>
				<TimelineItem title="Finish the book" date="July 30, 2024">
					<svelte:fragment slot="icon">
						<span
							class="bg-primary-200 dark:bg-primary-900 absolute -start-3 flex h-6 w-6 items-center justify-center rounded-full ring-8 ring-white dark:ring-white"
						>
							<CalendarWeekSolid class="text-primary-600 dark:text-primary-400 h-4 w-4" />
						</span>
					</svelte:fragment>
				</TimelineItem>
			</Timeline>
		</Card>

		<Card class="!bg-blue-800/90">
			<AdvancedRating
				ratings={[
					{ label: '5 star', rating: 0 },
					{ label: '4 star', rating: 50 },
					{ label: '3 star', rating: 50 },
					{ label: '2 star', rating: 0 },
					{ label: '1 star', rating: 0 }
				]}
			>
				<span slot="rating">
					<Rating total={5} rating={3.5} id="example-8">
						<p slot="text" class="ms-2 text-sm font-medium text-gray-500 dark:text-white">
							3.5 out of 5 (Preliminary)
						</p>
					</Rating>
				</span>
				<p slot="globalText" class="mt-2 text-sm font-medium text-gray-500 dark:text-white">
					Pending 2 outstanding global ratings
				</p>
			</AdvancedRating>
		</Card>
	</div>

	<!-- <h2>
				try editing <strong>src/routes/+page.svelte</strong>
			</h2> -->

	<!-- </section> -->
	<!-- <div class="col-span-1 row-span-1">
		<NextMatch />
	</div>

	<div class="col-span-1 row-span-3">
		<Card padding="none" class="no-scrollbar relative h-dvh overflow-y-scroll object-cover">
			<a class="twitter-timeline" href="https://twitter.com/Arsenal?ref_src=twsrc%5Etfw"
				>Tweets by Arsenal</a
			> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
		</Card>
	</div> -->
	<!-- 
	<aside class=" float-right">
		<NextMatch />

		<Card padding="none" class="no-scrollbar relative h-dvh overflow-y-scroll object-cover">
			<a class="twitter-timeline" href="https://twitter.com/Arsenal?ref_src=twsrc%5Etfw"
				>Tweets by Arsenal</a
			> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
		</Card>
	</aside> -->
</div>

<Banner id="bottom-banner" position="fixed" bannerType="bottom">
	<a
		href="arsenalbookclub.com"
		class="mb-2 flex items-center border-gray-200 md:mb-0 md:me-4 md:border-e md:pe-4 dark:border-gray-600"
	>
		<img src={logo} class="me-2 h-6" alt="ABC logo" />
		<span class="self-center whitespace-nowrap text-lg font-semibold dark:text-white">ABC</span>
	</a>
	<p class="flex items-center text-sm font-normal text-gray-500 dark:text-gray-400">
		Finish the book.
	</p>
</Banner>

<Banner id="bottom-banner-1" position="static" bannerType="bottom">
	<a
		href="arsenalbookclub.com"
		class="mb-2 flex items-center border-gray-200 md:mb-0 md:me-4 md:border-e md:pe-4 dark:border-gray-600"
	>
		<img src={logo} class="me-2 h-6" alt="ABC logo" />
		<span class="self-center whitespace-nowrap text-lg font-semibold dark:text-white">ABC</span>
	</a>
	<p class="flex items-center text-sm font-normal text-gray-500 dark:text-gray-400">
		Tim has the next pick.
	</p>
</Banner>

<!-- <div class="p-8"> -->

<!-- </div> -->

<style>
	/* section {
		display: flex;
		flex-direction: column;
		justify-content: center;
		align-items: center;
		flex: 0.6;
	} */

	h1 {
		width: 100%;
	}

	.welcome {
		display: block;
		position: relative;
		width: 100%;
		height: 0;
		padding: 0 0 calc(100% * 495 / 2048) 0;
	}

	.welcome img {
		position: absolute;
		width: 100%;
		height: 100%;
		top: 0;
		display: block;
	}
</style>
