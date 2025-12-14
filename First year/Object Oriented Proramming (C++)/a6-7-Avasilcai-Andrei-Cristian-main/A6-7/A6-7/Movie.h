#pragma once
#include <string>

using namespace std;

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
	std::string getTitle() const;
	// Returns the genre of the movie
	std::string getGenre() const;
	// Returns the year of the movie
	int getYear() const;
	// Returns the number of likes of the movie
	int getLikes() const;
	// Returns the trailer of the movie
	std::string getTrailer() const;
	// Increases the number of likes of the movie by 1
	void increaseLikes();
	// Returns a string representation of the movie
	void setTitle(std::string title);
	void setGenre(std::string genre);
	void setYear(int year);
	void setLikes(int likes);
	void setTrailer(std::string trailer);
	std::string toString();
	// Returns a string representation of the movie, with a different format
	std::string toStringShort();
	// Overloading the equality operator
	bool operator==(const Movie& m);

	void play();

	friend istream& operator>>(istream& is, Movie& m);
	friend ostream& operator<<(ostream& os, Movie& m);
};
