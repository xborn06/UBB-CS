#include "AdminService.h"

void AdminService::addMovie(const std::string& title, const std::string& genre, int year, int likes, const std::string& trailer)
{
	if (this->repository.getMovieByTitle(title).getTitle() != "")
		throw std::exception("The movie already exists!");
	if (likes < 0)
		throw std::exception("The number of likes must be a positive integer!");
	if (year < 0)
		throw std::exception("The year must be a positive integer!");
	if (title == "")
		throw std::exception("The title must not be empty!");
	if (genre == "")
		throw std::exception("The genre must not be empty!");
	if (trailer == "")
		throw std::exception("The trailer must not be empty!");
	Movie m{ title, genre, year, likes, trailer };
	this->repository.addMovie(m);
}

void AdminService::deleteMovie(const std::string& title)
{
	if (this->repository.getMovieByTitle(title).getTitle() == "")
		throw std::exception("The movie does not exist!");
	this->repository.deleteMovie(title);
}

void AdminService::updateMovie(const std::string& title, const std::string& genre, int year, int likes, const std::string& trailer)
{
	if (title == "")
		throw std::exception("The title must not be empty!");
	if (this->repository.getMovieByTitle(title).getTitle() == "")
		throw std::exception("The movie does not exist!");
	if (likes < 0)
		throw std::exception("The number of likes must be a positive integer!");
	if (year < 0)
		throw std::exception("The year must be a positive integer!");
	if (genre == "")
		throw std::exception("The genre must not be empty!");
	if (trailer == "")
		throw std::exception("The trailer must not be empty!");
	Movie m{ title, genre, year, likes, trailer };
	this->repository.updateMovie(m);
}

void AdminService::increaseLikes(const std::string& title)
{
	if (this->repository.getMovieByTitle(title).getTitle() == "")
		throw std::exception("The movie does not exist!");
	this->repository.increaseLikes(title);
}

DynamicVector<Movie> AdminService::getMovies() const
{
	return this->repository.getMovies();
}

Movie AdminService::getMovieByTitle(const std::string& title)
{
	if (this->repository.getMovieByTitle(title).getTitle() == "")
		throw std::exception("The movie does not exist!");
	return this->repository.getMovieByTitle(title);
}