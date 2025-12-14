#pragma once
#include <vector>
#include "Movie.h"

class WatchList
{
protected:
	std::vector<Movie> movies;
	int current;
public:
	WatchList();
	// Adds a movie to the watchlist
	bool add(const Movie& movie);

	//Returns the movie that is currently playing
	Movie getCurrentMovie();

	//Starts the watchlist - plays the first movie trailer
	void play();

	//Plays the next movie trailer
	void next();

	//Checks if the playlist is empty
	bool isEmpty();

	//removes a movie from the watchlist
	void remove(const std::string& title);

	virtual ~WatchList();

	std::vector<Movie> getMovies() const
	{
		return this->movies;
	}
};