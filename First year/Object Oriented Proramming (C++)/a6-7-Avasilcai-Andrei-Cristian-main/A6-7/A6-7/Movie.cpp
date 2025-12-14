#define _CRT_SECURE_NO_WARNINGS
#include "Movie.h"
#include <iostream>
#include <vector>
#include "Utils.h"
#include <Windows.h>
#include <shellapi.h>

Movie::Movie() : title(""), genre(""), year(0), likes(0), trailer("") {}

Movie::Movie(const std::string& title, const std::string& genre, int year, int likes, const std::string& trailer)
{
	this->title = title;
	this->genre = genre;
	this->year = year;
	this->likes = likes;
	this->trailer = trailer;
}

std::string Movie::getTitle() const
{
	return this->title;
}

std::string Movie::getGenre() const
{
	return this->genre;
}

int Movie::getYear() const
{
	return this->year;
}

int Movie::getLikes() const
{
	return this->likes;
}

std::string Movie::getTrailer() const
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

void Movie::setTrailer(std::string trailer)
{
	this->trailer = trailer;
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

void Movie::play()
{
	ShellExecuteA(NULL, NULL, "firefox.exe", this->getTrailer().c_str(), NULL, SW_SHOWMAXIMIZED);
}

istream& operator >> (istream& is, Movie& m)
{
	string input;
	
	getline(is, input);

	vector<string> result = tokenize(input, ',');
	if (result.size() != 5)
		return is;

	m.setTitle(result[0]);
	m.setGenre(result[1]);
	m.setYear(stoi(result[2]));
	m.setLikes(stoi(result[3]));
	m.setTrailer(result[4]);

	return is;
}

ostream& operator << (ostream& os, Movie& m)
{
	os << m.getTitle() << "," << m.getGenre() << "," << m.getYear() << "," << m.getLikes() << "," << m.getTrailer();
	return os;
}