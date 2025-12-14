#include "Repository.h"
#include <fstream>
#include "RepositoryExceptions.h"
#include "Utils.h"
#include <algorithm>

Repository::Repository(std::string filePath) : filePath(filePath)
{
	/*
	* Constructor with parameters for a Repository
	* Input: the path to the file where the movies are stored
	* Output: -
	*/
	this->filePath = filePath;
	this->readFromFile();
}

void Repository::addMovie(const Movie& m)
{
	/*
	* Function that adds a movie to the repository
	* Input: a movie
	* Output: it just adds the movie to the dynamic vector
	*/
	Movie m1{};
	try
	{
		m1 = this->getMovieByTitle(m.getTitle());
		throw DuplicateMovieException();
	}
	catch (InexistingMovieException&) {}
	this->movies.push_back(m);
	writeToFile();
}

void Repository::deleteMovie(const std::string& title)
{
	/*
	* Function that deletes a movie from the repository
	* Input: the title of the movie
	* :Output: it searches for the movie with the given title and deletes it 
	*/
	int index = this->findMovieByTitle(title);
	if (index != -1) {
		this->movies.erase(this->movies.begin() + index);
		writeToFile();
	}
	else
		throw InexistingMovieException();
}

void Repository::updateMovie(Movie& m)
{
	/*
	* Function that updates a movie by replacing it with a new entity
	* Input: the new movie with the new details (same title as the old one)
	* Output: searches for the movie and updates it
	*/
	int index = this->findMovieByTitle(m.getTitle());
	if (index != -1) {
		this->movies[index] = m;
		writeToFile();
	}
	else
		throw InexistingMovieException();
}

void Repository::increaseLikes(const std::string& title)
{
	/*
	* Function that increases the likes of a movie
	* Input: the title of the movie
	* Ouput: -
	*/
	int index = this->findMovieByTitle(title);
	if (index != -1) {
		this->movies[index].setLikes(this->movies[index].getLikes() + 1);
		writeToFile();
	}
	else
		throw InexistingMovieException();
}

std::vector<Movie> Repository::getMovies() const
{
	/*
	* Function that returns the movies
	* Input: -
	* Output: the dynamic vector of movies
	*/
	return this->movies;
}

Movie Repository::getMovieByTitle(const std::string& title)
{
	/*
	* Function that returns a movie with a given title
	* Input: the title
	* Output: the movie with the given title or an empty one in case it's not there
	*/
	auto it = std::find_if(this->movies.begin(), this->movies.end(),
		[&title](Movie& m) {
			return m.getTitle() == title;
		});

	if (it != this->movies.end())
		return *it;

	throw InexistingMovieException();
}


int Repository::findMovieByTitle(const std::string& title)
{
	/*
	* Function that returns the index of a movie
	* Input: the title of the movie
	* Output: the index of that movie, or -1 if not found
	*/
	auto it = std::find_if(this->movies.begin(), this->movies.end(),
		[&title](Movie& m) {
			return m.getTitle() == title;
		});

	if (it == this->movies.end())
		throw InexistingMovieException();

	return std::distance(this->movies.begin(), it);
}


void Repository::readFromFile()
{
	/*
	* Function that reads the movies from a file
	* Input: -
	* Output: the movies are read from the file and added to the dynamic vector
	*/
	std::ifstream is(this->filePath);
	if (!is.is_open())
		throw FileException("The file could not be opened!");
	Movie m;
	while (is >> m)
	{
		addMovie(m);
	}
	is.close();
}

void Repository::writeToFile()
{
	/*
	* Function that writes the movies to a file
	* Input: -
	* Output: the movies are written to the file
	*/
	std::ofstream os(this->filePath);
	if (!os.is_open())
		throw FileException("The file could not be opened!");
	for (auto& m : this->movies)
	{

		os << m<<"\n";
	}
	os.close();
}

std::vector<Movie> Repository::getMoviesByGenre(const std::string& genre)
{
	/*
	* Function that returns the movies with a given genre
	* Input: the genre
	* Output: the movies with the given genre
	*/
	std::vector<Movie> result;
	for (auto& m : this->movies)
	{
		if (m.getGenre() == genre)
			result.push_back(m);
	}
	return result;
}