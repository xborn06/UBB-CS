#include "FileWatchlist.h"

FileWatchlist::FileWatchlist() : WatchList{}, filename{ "" }
{
}

void FileWatchlist::setFilename(const std::string& filename)
{
	this->filename = filename;
}

FileWatchlist::~FileWatchlist()
{
}