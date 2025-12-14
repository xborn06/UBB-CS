#include "Repository.h"

void Repository::addMovie(const Movie& m)
{
	this->movies.add(m);
}

void Repository::deleteMovie(const std::string& title)
{
	int index = this->findMovieByTitle(title);
	if (index != -1)
		this->movies.remove(index);
}

void Repository::updateMovie(Movie& m)
{
	int index = this->findMovieByTitle(m.getTitle());
	if (index != -1)
		this->movies.update(index, m);
}

void Repository::increaseLikes(const std::string& title)
{
	int index = this->findMovieByTitle(title);
	if (index != -1)
		this->movies[index].setLikes(this->movies[index].getLikes() + 1);
}

DynamicVector<Movie> Repository::getMovies() const
{
	return this->movies;
}

Movie Repository::getMovieByTitle(const std::string& title)
{
	for (int i = 0; i < this->movies.getSize(); i++)
	{
		Movie m = this->movies[i];
		if (m.getTitle() == title)
			return m;
	}
	return Movie{};
}

int Repository::findMovieByTitle(const std::string& title)
{
	for (int i = 0; i < this->movies.getSize(); i++)
	{
		Movie m = this->movies[i];
		if (m.getTitle() == title)
			return i;
	}
	return -1;
}
