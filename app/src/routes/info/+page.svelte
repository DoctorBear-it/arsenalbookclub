<script lang="ts"> 
    // @ts-check
    export let data;

    //Don't do this, make these calls in +page.ts or +page.server.ts
    async function fetchData() {
        const res = await fetch("https://jsonplaceholder.typicode.com/todos");
        const data = await res.json();

        if (res.ok) {
        return data;
        } else {
        throw new Error(data);
        }
    }

    let promise;
	const handleClick = () => {
		promise = fetch('https://jsonplaceholder.typicode.com/posts/1').then((x) => x.json());
	};

    let resourcesList: Record<string, string>[] = [
        {id: "Example Repo", url: "https://github.com/shinokada/sveltekit-githubpages"},
        {id:"Example Repo", url : "https://github.com/vercel/examples/tree/main/storage/postgres-sveltekit"},
        {id:"Example Repo", url : "https://github.com/sveltejs/kit-template-default"},
        {id:"Example Repo", url : "https://github.com/nextauthjs/next-auth/tree/main/apps/examples/sveltekit"},
        {id:"Example Repo", url : "https://github.com/ivanhofer/sveltekit-typescript-showcase/tree/main"},
        {id:"Example Repo", url : "https://vercel.com/templates/svelte"},
        {id:"Resource", url : "https://scottspence.com/"},
        {id:"Resource", url : "https://www.sveltesociety.dev/recipes/component-recipes/using-fetch-to-consume-apis"},
        {id:"Resource", url : "https://www.sveltesociety.dev/recipes"},
        {id:"Resource", url : "https://www.sveltesociety.dev/packages"},
        {id:"Code Examples", url : "https://svelte.dev/repl/5c95e18702764aefa71ff2b4616a6c6e?version=3.20.1"},
        {id:"Course", url : "https://vercel.com/docs/beginner-sveltekit"},
        {id:"Course", url : "https://github.com/vercel/beginner-sveltekit"},
        {id:"Docs", url : "https://svelte.dev/docs/typescript"},
        {id:"Docs", url : "https://kit.svelte.dev/docs/load"},
        {id:"Fake Data", url : "https://jsonplaceholder.typicode.com/"},
        {id:"Tutorial", url : "https://learn.svelte.dev/tutorial/universal-load-functions"},
        {id:"Tutorial", url : "https://learn.svelte.dev/tutorial/onmount"},
        {id:"Code Examples", url : "https://svelte.dev/examples/each-blocks"},
        {id:"Code Examples", url : "https://svelte.dev/repl/9fb792271c324da5bf1df6ccc617a902?version=3.29.7"},
        {id:"Docs", url : "https://kit.svelte.dev/docs/load#making-fetch-requests"},
        {id:"Tutorial", url : "https://learn.svelte.dev/tutorial/each-blocks"}
    ];

    // let groupedResourcesList=Object.groupBy(resourcesList, (site) => {return });

</script> 

<svelte:head>
	<title>Info</title>
	<meta name="information" content="Info about this app" />
</svelte:head>

<!-- <button on:click={handleClick}>fetch from api</button> -->
<h1>{JSON.stringify(data.item.message, null, 2)}</h1>

<ul>
	{#each resourcesList as { id, url }, i}
		<li>
			<a target="_blank" rel="noreferrer" href="{url}">
				{i + 1}: {id}
			</a>
		</li>
        <p1>{url}</p1>
	{/each}
</ul>

<h1>
    <button on:click={handleClick}> Click to Load Data </button>
    {#await promise}
	<!-- optionally show something while promise is pending -->
    {:then newdata}
        <!-- promise was fulfilled -->
        <pre>
        {JSON.stringify(newdata, null, 2)}
    </pre>
    {:catch error}
        <!-- optionally show something while promise was rejected -->
    {/await}
</h1>
<!-- {#await promise}
    <p>...waiting</p>
{:then text} 
    <p>{text.message}</p>
{:catch error}
    <p style="color: red">{error.message}</p>
{/await} -->

<h1>
    {#await fetchData()}
        <p>loading</p>
    {:then items}
        {#each items as item}
            <li>{item.id}. {item.title}</li>
        {/each}
    {:catch error}
        <p style="color: red">{error.message}</p>
    {/await}
</h1>

<style> </style> 


