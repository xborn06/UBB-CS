#pragma once
#include "Repository.h"

class AdminService
{
private:
	Repository& repository;

public:
	// Default constructor for an AdminService
	AdminService(Repository& repository) : repository{ repository } {}
	// Adds a movie to the repository
	void addMovie(const std::string& title, const std::string& genre, int year, int likes, const std::string& trailer);
	// Deletes a movie from the repository
	void deleteMovie(const std::string& title);
	// Updates a movie from the repository
	void updateMovie(const std::string& title, const std::string& genre, int year, int likes, const std::string& trailer);
	// Increases the number of likes for a movie
	void increaseLikes(const std::string& title);
	// Returns the movies from the repository
	DynamicVector<Movie> getMovies() const;
	// Returns the movie with the given title
	Movie getMovieByTitle(const std::string& title);
};