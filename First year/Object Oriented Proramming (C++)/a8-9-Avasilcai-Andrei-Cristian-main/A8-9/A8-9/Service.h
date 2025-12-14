#pragma once
#include "Repository.h"
#include "FileWatchlist.h"
#include "Validation.h"
#include <memory>

class Service
{
private:
	Repository& repository;
	FileWatchlist* watchlist;
	MovieValidator validator;
public:
	// Default constructor for an Service
	Service(Repository& r, FileWatchlist* w, MovieValidator v) : repository{ r }, watchlist{ w }, validator{ v } {}

	Repository getRepo() const { return repository; }
	WatchList* getWatchlist() const { return watchlist; }

	// Adds a movie to the repository
	void addMovieToRepository(const std::string& title, const std::string& genre, int year, int likes, const std::string& trailer);
	// Deletes a movie from the repository
	void deleteMovieFromRepository(const std::string& title);
	// Updates a movie from the repository
	void updateMovieToRepository(const std::string& title, const std::string& genre, int year, int likes, const std::string& trailer);
	// Increases the number of likes for a movie
	void increaseLikes(const std::string& title);
	// Returns the movies from the repository
	std::vector<Movie> getMovies() const;
	// Returns the movie with the given title
	Movie getMovieByTitle(const std::string& title);
	//Adds a movie to the watchlist
	bool addMovieToWatchlist(const Movie& movie);

	void deleteMovieFromWatchlist(const std::string& title, bool isLiked);

	std::vector<Movie> getMoviesByGenre(const std::string& genre) const;

	void startWatchlist();
	void nextMovieWatchlist();

	void saveWatchlist(const std::string& filename);
	void openWatchlist() const;

	bool isWatchlistEmpty() const;
	void setWatchlist(FileWatchlist* watchlist) { this->watchlist = watchlist; }
};