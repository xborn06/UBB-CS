#pragma once
#include "DynamicVector.h"
#include "Movie.h"

class Repository
{
private:
	DynamicVector<Movie> movies;
public:
	// Default constructor for a Repository
	Repository() {}
	// Returns the movies with the given genre
	DynamicVector<Movie> getMoviesByGenre(const std::string& genre);
	// Adds a movie to the repository
	void addMovie(const Movie& m);
	// Deletes a movie from the repository
	void deleteMovie(const std::string& title);
	// Updates a movie from the repository
	void updateMovie(Movie& m);
	// Increases the number of likes for a movie
	void increaseLikes(const std::string& title);
	// Returns the movies from the repository
	DynamicVector<Movie> getMovies() const;
	// Returns the movie with the given title
	Movie getMovieByTitle(const std::string& title);
	// Returns the movie with the given title
	int findMovieByTitle(const std::string& title);
};