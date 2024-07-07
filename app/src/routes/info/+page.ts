//Provides a Universal load, which renders both on the server and the client

// Only non-localhost calls work here.

// /** @type {import('./$types').PageLoad} */
// export async function load({ fetch}) {
// 	const res = await fetch(`https://jsonplaceholder.typicode.com/posts/1`);
// 	const item = await res.json();

// 	return { item };
// }

// 
// export const prerender = true;

//Disables server side render 
// export const ssr = false;

//Disables client side render (can enable to render javascript-free pages)
// export const csr = false;