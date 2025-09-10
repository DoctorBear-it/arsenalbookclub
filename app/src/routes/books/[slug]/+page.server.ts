import { error } from '@sveltejs/kit';
// import { posts } from '../data.js';
import { books } from "$lib/data/ratings";

// import {readFile} from 'xlsx';
// const books = readFile('$lib/data/ratings.xlsx')


export function load({ params }) {
	const book = books.find((book) => book.slug === params.slug);

	if (!book) throw error(404);

	return {
		book
	};
}
