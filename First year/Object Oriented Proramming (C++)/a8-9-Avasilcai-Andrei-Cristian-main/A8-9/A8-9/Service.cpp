#include "Service.h"

void Service::addMovieToRepository(const std::string& title, const std::string& genre, int year, int likes, const std::string& trailer)
{
	/*
	* Function that adds a movie
	* Input: title, genre, year, likes, trailer
	* Output: creates the movie entity and adds it to the repository
	*/
	Movie m{ title, genre, year, likes, trailer };
	this->validator.validate(m);
	this->repository.addMovie(m);
}

void Service::deleteMovieFromRepository(const std::string& title)
{
	/*
	* Function that deletes a movie
	* Input: the title of the movie
	* Output: checks if the title is valid and then passes it onto the repository function 
	*/
	Movie m = this->repository.getMovieByTitle(title);
	this->repository.deleteMovie(title);
}

void Service::updateMovieToRepository(const std::string& title, const std::string& genre, int year, int likes, const std::string& trailer)
{
	/* Function that updates a movie
	* Input: the new data of the movie
	* Output: creates the movie entity and passes it on to the repository function
	*/
	Movie m{ title, genre, year, likes, trailer };
	this->validator.validate(m);
	this->repository.updateMovie(m);
}

void Service::increaseLikes(const std::string& title)
{
	/*
	* Function that increases the likes of a movie
	* Input: the title of the movie
	* Output: checks if the title is valid and then passes it onto the repository function
	*/
	Movie m = this->repository.getMovieByTitle(title);
	this->validator.validate(m);
	this->repository.increaseLikes(title);
}

std::vector<Movie> Service::getMovies() const
{
	/*
	* Function that returns the movies
	* Input: -
	* Output: the dynamic vector of movies
	*/
	return this->repository.getMovies();
}

Movie Service::getMovieByTitle(const std::string& title)
{
	/*
	* Function that returns the movie with a given title
	* Input: the title
	* Output: the movie with the given title or an empty one in case it's not there
	*/
	Movie m = this->repository.getMovieByTitle(title);
	this->validator.validate(m);
	return this->repository.getMovieByTitle(title);
}

bool Service::addMovieToWatchlist(const Movie& movie)
{
	if (this->watchlist == nullptr)
		return 0;
	this->watchlist->add(movie);
}

void Service::deleteMovieFromWatchlist(const std::string& title,bool isLiked)
{
	if (this->watchlist == nullptr)
		return;
	this->watchlist->remove(title);
	if (isLiked)
		this->repository.increaseLikes(title);
}

std::vector<Movie> Service::getMoviesByGenre(const std::string& genre) const
{
	/*
	* Function that returns the movies with a given genre
	* Input: the genre
	* Output: the movies with the given genre
	*/
	return this->repository.getMoviesByGenre(genre);
}

void Service::startWatchlist()
{
	if (this->watchlist == nullptr)
		return;
	this->watchlist->play();
}

void Service::nextMovieWatchlist()
{
	if (this->watchlist == nullptr)
		return;
	this->watchlist->next();
}

void Service::saveWatchlist(const std::string& filename)
{
	if (this->watchlist == nullptr)
		return;
	this->watchlist->setFilename(filename);
	this->watchlist->writeToFile();
}

void Service::openWatchlist() const
{
	if (this->watchlist == nullptr)
		return;
	this->watchlist->displayWatchlist();
}

bool Service::isWatchlistEmpty() const
{
	if (this->watchlist == nullptr)
		return 1;
	return this->watchlist->isEmpty();
}