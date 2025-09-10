import {fixtures} from "$lib/data/fixtures";

/** @type {import('./$types').PageServerLoad} */
export async function load({ fetch}) {
	const res = await fetch(`http://localhost:8000/`);
	const item = await res.json();

	return { 
		item:item,
        summaries: fixtures.map((fixture) => ({
            date: fixture.date,
            home: fixture.home,
            away: fixture.away,
            contest: fixture.contest
        }))
	};
}
