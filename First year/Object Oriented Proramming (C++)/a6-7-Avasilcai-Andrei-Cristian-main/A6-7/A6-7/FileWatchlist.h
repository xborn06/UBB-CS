#pragma once
#include "Watchlist.h"

class FileWatchlist : public WatchList
{
protected:
	std::string filename;
public:
	FileWatchlist();
	virtual ~FileWatchlist();

	void setFilename(const std::string& filename);
	virtual void writeToFile() = 0;
	virtual void displayWatchlist() const = 0;
};