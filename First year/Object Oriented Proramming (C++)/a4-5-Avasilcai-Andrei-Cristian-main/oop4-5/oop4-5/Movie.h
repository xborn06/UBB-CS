#pragma once
#include <string>

class Movie
{
private:
	std::string title;
	std::string genre;
	int year;
	int likes;
	std::string trailer;

public:
	// Default constructor for a Movie
	Movie();
	// Constructor with parameters for a Movie
	Movie(const std::string& title, const std::string& genre, int year, int likes, const std::string& trailer);
	// Returns the title of the movie
	std::string getTitle();
	// Returns the genre of the movie
	std::string getGenre();
	// Returns the year of the movie
	int getYear();
	// Returns the number of likes of the movie
	int getLikes();
	// Returns the trailer of the movie
	std::string getTrailer();
	// Increases the number of likes of the movie by 1
	void increaseLikes();
	// Returns a string representation of the movie
	void setTitle(std::string title);
	void setGenre(std::string genre);
	void setYear(int year);
	void setLikes(int likes);
	std::string toString();
	// Returns a string representation of the movie, with a different format
	std::string toStringShort();
	// Overloading the equality operator
	bool operator==(const Movie& m);
};
