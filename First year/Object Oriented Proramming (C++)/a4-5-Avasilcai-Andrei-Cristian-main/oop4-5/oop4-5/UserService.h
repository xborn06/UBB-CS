#pragma once
#include "Repository.h"

class UserService
{
private:
	Repository& repo;
	DynamicVector<Movie> watchList;
public:
	UserService(Repository& repo) : repo(repo) {}
	// Adds a movie to the watchlist
	bool addMovieToWatchList(const std::string& title);
	// Deletes a movie from the watchlist
	bool deleteMovieFromWatchList(const std::string& title);
	// Returns the watchlist
	DynamicVector<Movie> getWatchList() const;
	// Returns the movies from the repository
	DynamicVector<Movie> getMoviesbyGenre(DynamicVector<Movie>allMovies, const std::string& genre);
	// Returns the movies of a given genre
};