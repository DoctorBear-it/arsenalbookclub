/** @type {import('./$types').PageServerLoad} */
export async function load({ fetch}) {
	const res = await fetch(`http://localhost:8000/`);
	const item = await res.json();

	return { item };
}