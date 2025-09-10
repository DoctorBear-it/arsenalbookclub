import { books } from "$lib/data/ratings";

export function load() {
	return {
		summaries: books.map((book) => ({
			slug: book.slug,
			book: book.book,
			rating: book.goodreads
		}))
	};
}
