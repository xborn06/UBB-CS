#pragma once
#include "FileWatchlist.h"
#include <string>

class CSVWatchlist : public FileWatchlist
{
	/*
	* Writes the watchlist to file
	* Throws: FileException - if it cannot write.
	*/
	void writeToFile() override;

	/*
	* Displays the watchlist using Microsoft Excel.
	*/
	void displayWatchlist() const override;
};