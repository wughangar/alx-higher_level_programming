$(document).ready(function() {
	const apiUrl = "https://swapi-api.alx-tools.com/api/films/?format=json";
	$.get(apiUrl, function(data) {
		const listMovies = $("#list_movies");
		$.each(data.results, function(index, movie) {
			const listItem = $("<li>").text(movie.title);
			listMovies.append(listItem);
		});
	});
});
