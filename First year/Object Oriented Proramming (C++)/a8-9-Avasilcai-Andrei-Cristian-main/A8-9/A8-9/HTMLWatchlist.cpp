#include "HTMLWatchlist.h"
#include <fstream>
#include <Windows.h>
#include "RepositoryExceptions.h"

void HTMLWatchlist::writeToFile()
{
	std::ofstream f(this->filename);
	if (!f.is_open())
		throw FileException("The file could not be openned!");
	f << "<!DOCTYPE html>\n";
	f << "<html>\n";
	f << "<head>\n";
	f << "<title>Watchlist</title>\n";
	f << "</head>\n";
	f << "<body>\n";
	f << "<h1>Watchlist</h1>\n";
	f << "<table border=\"1\">\n";
	f << "<tr><th>Title</th><th>Genre</th><th>Year</th><th>Likes</th><th>Trailer</th></tr>\n";
	for (auto m : this->movies)
	{
		f << "<tr>";
		f << "<td>" << m.getTitle() << "</td>";
		f << "<td>" << m.getGenre() << "</td>";
		f << "<td>" << m.getYear() << "</td>";
		f << "<td>" << m.getLikes() << "</td>";
		f << "<td><a href=\"" + m.getTrailer() + "\">" + m.getTrailer() + "</a></td>";
		f << "</tr>\n";
	}
	f << "</table>\n";
	f << "</body>\n";
	f << "</html>\n";
	f.close();
}

void HTMLWatchlist::displayWatchlist() const
{
	std::string aux = "\"" + this->filename + "\"";
	ShellExecuteA(NULL, NULL, "C:\\Program Files\\Mozilla Firefox\\firefox.exe", aux.c_str(), NULL, SW_SHOWMAXIMIZED);
}