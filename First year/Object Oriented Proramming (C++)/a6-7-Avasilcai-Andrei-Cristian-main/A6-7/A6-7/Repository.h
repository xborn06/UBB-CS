#pragma once
#include "Movie.h"
#include <vector>

class Repository
{
private:
	std::vector<Movie> movies;
	std::string filePath;
public:
	// Default constructor for a Repository
	Repository() {}
	// Constructor with parameters for a Repository
	Repository(std::string filePath);
	// Returns the movies with the given genre
	std::vector<Movie> getMoviesByGenre(const std::string& genre);
	// Adds a movie to the repository
	void addMovie(const Movie& m);
	// Deletes a movie from the repository
	void deleteMovie(const std::string& title);
	// Updates a movie from the repository
	void updateMovie(Movie& m);
	// Increases the number of likes for a movie
	void increaseLikes(const std::string& title);
	// Returns the movies from the repository
	std::vector<Movie> getMovies() const;
	// Returns the movie with the given title
	Movie getMovieByTitle(const std::string& title);
	// Returns the movie with the given title
	int findMovieByTitle(const std::string& title);
	//Reads the movies from a file
	void readFromFile();
	//Writes the movies to a file
	void writeToFile();
};