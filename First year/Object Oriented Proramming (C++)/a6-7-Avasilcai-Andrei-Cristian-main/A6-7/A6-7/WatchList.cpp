#include "Watchlist.h"
#include <algorithm>
#include <vector>
#include <iterator>

WatchList::WatchList()
{
	this->current = 0;
}

bool WatchList::add(const Movie& movie)
{
	for (const auto& m : this->movies)
		if (m.getTitle() == movie.getTitle())
			return 0;
	this->movies.push_back(movie);
	return 1;
}

Movie WatchList::getCurrentMovie()
{
	if (this->current == this->movies.size())
		this->current = 0;
	return this->movies[this->current];
	return Movie{};
}

void WatchList::play()
{
	if (this->movies.size() == 0)
		return;
	this->current = 0;
	Movie currentMovie = this->getCurrentMovie();
	currentMovie.play();
}

void WatchList::next()
{
	if (this->movies.size() == 0)
		return;
	this->current++;
	Movie currentMovie = this->getCurrentMovie();
	currentMovie.play();
}

void WatchList::remove(const std::string& title)
{
	auto it = std::remove_if(this->movies.begin(), this->movies.end(),
		[&title](Movie& m) {
			return m.getTitle() == title;
		});
	this->movies.erase(it, this->movies.end());
}

bool WatchList::isEmpty()
{
	return this->movies.size() == 0;
}

WatchList::~WatchList()
{
}