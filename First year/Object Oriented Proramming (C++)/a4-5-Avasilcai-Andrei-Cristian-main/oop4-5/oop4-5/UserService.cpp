#include "UserService.h"

bool UserService::addMovieToWatchList(const std::string& title)
{
	/*
	* Function that adds a movie to the watchlist
	* Input: the title of the movie
	* Output: true if the movie was added to the watchlist, false otherwise
	*/
	Movie movie = this->repo.getMovieByTitle(title);
	if (movie.getTitle() == "")
		return false;
	int index = this->watchList.find(movie);
	if (index != -1)
		return false;
	this->watchList.add(movie);
	return true;
}

bool UserService::deleteMovieFromWatchList(const std::string& title)
{
	/*
	* Function that deletes a movie from the watchlist
	* Input: the title of the movie
	* Ouput: true if the movie was deleted from the watchlist, false otherwise
	*/
	Movie movie = this->repo.getMovieByTitle(title);
	if (movie.getTitle() == "")
		return false;
	int index = this->watchList.find(movie);
	if (index != -1)
	{
		this->watchList.remove(index);
	}
	return true;
}

DynamicVector<Movie> UserService::getWatchList() const
{
	/*
	* Function that returns the watchlist
	* Input: none
	* Output: the watchlist
	*/
	return this->watchList;
}

DynamicVector<Movie> UserService::getMoviesbyGenre(DynamicVector<Movie> allMovies, const std::string& genre)
{
	/*
	* Function that returns the movies of a given genre
	* Input: all the movies in the repository and the genre
	* Ouptput: the movies of the given genre
	*/
	if (genre == "")
		return allMovies;
	DynamicVector<Movie> moviesByGenre;
	int size = allMovies.getSize();
	for (int i = 0; i < size; i++)
	{
		if (allMovies[i].getGenre() == genre)
			moviesByGenre.add(allMovies[i]);
	}
	return moviesByGenre;
}