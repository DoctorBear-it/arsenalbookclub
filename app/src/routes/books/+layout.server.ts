// TODO: read ratings page to get book list
// import { posts } from './data.js';
import { books } from "$lib/data/ratings";

// import {readFile} from 'xlsx';
// import f from '$lib/data/ratings.xlsx';
// set_fs(fs);
// const books = readFile('ratings.xlsx')

export function load() {
	return {
		summaries: books.map((book) => ({
			slug: book.slug,
			book: book.book,
			goodreads: book.goodreads
		}))
	};
}
