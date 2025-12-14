#include "Repository.h"
#include "Service.h"
#include "UI.h"
#include "Tests.h"
#include "CSVWatchlist.h"
#include <iostream>
#include "HTMLWatchlist.h"
int main()
{
	//Tests tests{};
	//tests.runAllTests();

	Repository repository{"movies.txt"};
	/*repository.addMovie(Movie{"The Shawshank Redemption", "Drama", 1994, 2, "https://www.youtube.com/watch?v=6hB3S9bIaco"});
	repository.addMovie(Movie{ "The Godfather", "Crime", 1972, 5, "https://www.youtube.com/watch?v=sY1S34973zA" });
	repository.addMovie(Movie{ "The Dark Knight", "Action", 2008, 7, "https://www.youtube.com/watch?v=EXeTwQWrcwY" });
	repository.addMovie(Movie{ "The Godfather: Part II", "Crime", 1974, 11, "https://www.youtube.com/watch?v=9O1Iy9od7-A" });
	repository.addMovie(Movie{ "The Lord of the Rings: The Return of the King", "Adventure", 2003, 14, "https://www.youtube.com/watch?v=r5X-hFf6Bwo" });
	repository.addMovie(Movie{ "Schindler's List", "Biography", 1993, 16, "https://www.youtube.com/watch?v=gG22XNhtnoY" });
	repository.addMovie(Movie{ "Inception", "Action", 2010, 18, "https://www.youtube.com/watch?v=YoHD9XEInc0" });
	repository.addMovie(Movie{ "Fight Club", "Drama", 1999, 20, "https://www.youtube.com/watch?v=SUXWAEX2jlg" });
	repository.addMovie(Movie{ "The Lord of the Rings: The Fellowship of the Ring", "Adventure", 2001, 25, "https://www.youtube.com/watch?v=V75dMMIW2B4" });
	repository.addMovie(Movie{ "The Lord of the Rings: The Two Towers", "Adventure", 2002, 30, "https://www.youtube.com/watch?v=LbfMDwc4azU" });
	repository.addMovie(Movie{ "Forrest Gump", "Drama", 1994, 44, "https://www.youtube.com/watch?v=bLvqoHBptjg" });*/
	std::cout << "Which option for the watchlist do you want?\n";
	std::cout << "1. CSV file.\n";
	std::cout << "2. HTML file.\n";
	int option;
	std::cin >> option;
	std::cin.ignore();
	FileWatchlist* w = nullptr;
	if (option == 1)
		w = new CSVWatchlist{};
	else
		w = new HTMLWatchlist{};
	MovieValidator validator{};
	Service service{ repository, w, validator };
	UI ui{ service };
	ui.run();
	return 0;
}