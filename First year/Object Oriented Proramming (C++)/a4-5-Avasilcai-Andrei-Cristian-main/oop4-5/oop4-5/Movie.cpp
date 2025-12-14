#include "Movie.h"

Movie::Movie() : title(""), genre(""), year(0), likes(0), trailer("") {}

Movie::Movie(const std::string& title, const std::string& genre, int year, int likes, const std::string& trailer)
{
	this->title = title;
	this->genre = genre;
	this->year = year;
	this->likes = likes;
	this->trailer = trailer;
}

std::string Movie::getTitle()
{
	return this->title;
}

std::string Movie::getGenre()
{
	return this->genre;
}

int Movie::getYear()
{
	return this->year;
}

int Movie::getLikes()
{
	return this->likes;
}

std::string Movie::getTrailer()
{
	return this->trailer;
}

void Movie::increaseLikes()
{
	this->likes++;
}

void Movie::setTitle(std::string title)
{
	this->title = title;
}

void Movie::setGenre(std::string genre)
{
	this->genre = genre;
}

void Movie::setYear(int year)
{
	this->year = year;
}

void Movie::setLikes(int likes)
{
	this->likes = likes;
}

std::string Movie::toString()
{
	return this->title + " - " + this->genre + " - " + std::to_string(this->year) + " - " + std::to_string(this->likes) + " - " + this->trailer;
}

std::string Movie::toStringShort()
{
	return this->title + " - " + std::to_string(this->year) + " - " + std::to_string(this->likes);
}

bool Movie::operator==(const Movie& m)
{
	return this->title == m.title;
}

