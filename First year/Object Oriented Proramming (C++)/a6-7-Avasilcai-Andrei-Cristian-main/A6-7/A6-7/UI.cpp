#include "UI.h"
#include <iostream>
#include <string>
#include "Validation.h"
#include "RepositoryExceptions.h"

int UI::menuMode()
{
	int mode{ 0 };
	std::cout << "Choose the mode of the application:" << std::endl;
	std::cout << "1. Admin mode." << std::endl;
	std::cout << "2. User mode." << std::endl;
	std::cout << "0. Exit." << std::endl;
	std::cin >> mode;
	std::cin.ignore();
	return mode;
}

void UI::printAdminMenu()
{
    std::cout << "1. Add a movie." << std::endl;
    std::cout << "2. Delete a movie." << std::endl;
    std::cout << "3. Update a movie." << std::endl;
    std::cout << "4. Print all the movies." << std::endl;
    std::cout << "0. Exit." << std::endl;
}

void UI::addMovieToRepo()
{
    std::string title, genre, trailer;
    int year, likes;
    try
    {
        std::cout << "Enter the title: ";
        std::getline(std::cin, title);
        std::cout << "Enter the genre: ";
        std::getline(std::cin, genre);
        std::cout << "Enter the year: ";
        std::cin >> year;
        std::cout << "Enter the number of likes: ";
        std::cin >> likes;
        std::cin.ignore();
        std::cout << "Enter the trailer: ";
        std::getline(std::cin, trailer);
    }
    catch (const std::exception& e)
    {
        std::cerr << "Error: " << e.what() << std::endl;
    }
    try
    {
        this->service.addMovieToRepository(title, genre, year, likes, trailer);
    }
    catch (MovieException& e)
    {
        for (auto m : e.getErrors())
            cout << m;
    }
    catch (RepositoryException& e)
    {
        cout << e.what() << endl;
    }
    catch (FileException& e)
    {
        cout << e.what() << endl;
    }
}

void UI::deleteMovieFromRepo()
{
	if (this->service.getMovies().size() == 0)
	{
		std::cout << "There are no movies in the repository." << std::endl;
		return;
	}
    std::string title;
    try
    {
        std::cout << "Enter the title: ";
        std::getline(std::cin, title);
    }
    catch (const std::exception& e)
    {
        std::cerr << "Error: " << e.what() << std::endl;
    }
    try
    {
        this->service.deleteMovieFromWatchlist(title, 0);
        this->service.deleteMovieFromRepository(title);
    }
	catch (RepositoryException& e)
	{
		std::cout << e.what() << std::endl;
	}
	catch (FileException& e)
	{
		std::cout << e.what() << std::endl;
	}
	catch (MovieException& e)
	{
		for (auto m : e.getErrors())
			cout << m;
	}
}

void UI::updateMovie()
{
	if (this->service.getMovies().size() == 0)
	{
		std::cout << "There are no movies in the repository." << std::endl;
		return;
	}
    std::string title, genre, trailer;
    int year, likes;
    try
    {
        std::cout << "Enter the title: ";
        std::getline(std::cin, title);
        std::cout << "Enter the genre: ";
        std::getline(std::cin, genre);
        std::cout << "Enter the year: ";
        std::cin >> year;
        std::cout << "Enter the number of likes: ";
        std::cin >> likes;
        std::cin.ignore();
        std::cout << "Enter the trailer: ";
        std::getline(std::cin, trailer);
    }
    catch (const std::exception& e)
    {
        std::cerr << "Error: " << e.what() << std::endl;
    }
	try
	{
		this->service.updateMovieToRepository(title, genre, year, likes, trailer);
	}
	catch (MovieException& e)
	{
		for (auto m : e.getErrors())
			cout << m;
	}
	catch (RepositoryException& e)
	{
		std::cout << e.what() << std::endl;
	}
	catch (FileException& e)
	{
		std::cout << e.what() << std::endl;
	}
}

void UI::printMoviesRepo()
{
    try
    {
        vector<Movie> movies = this->service.getMovies();
        for (int i = 0; i < movies.size(); i++)
        {
            Movie m = movies[i];
            std::cout << m.toString() << std::endl;
        }
    }
    catch (const std::exception& e)
    {
        std::cerr << "Error: " << e.what() << std::endl;
    }
}

void UI::printUserMenu()
{
	std::cout << "1. Search movies by genre." << std::endl;
	std::cout << "2. Remove movie from watchlist." << std::endl;
	std::cout << "3. See watchlist." << std::endl;
	std::cout << "4. Save watchlist to file." << std::endl;
    std::cout << "5. Display watchlist." << std::endl;
	std::cout << "0. Exit." << std::endl;
}

void UI::printMoviesByGenre()
{
	std::string genre;
	std::cout << "Enter the genre: ";
	std::getline(std::cin, genre);
	vector<Movie> movies = this->service.getMoviesByGenre(genre);
	if (movies.size() == 0)
	{
		std::cout << "There are no movies of this genre." << std::endl;
		return;
	}
    int index = 1;
    while(true)
	    for (int i = 0; i < movies.size(); i++)
	    {
		    Movie m = movies[i];
            std::string title, genre, link;
			int year, likes;
			title = m.getTitle();
			genre = m.getGenre();
			year = m.getYear();
			likes = m.getLikes();
			link = m.getTrailer();
			std::cout << "\n#" << index++ << std::endl;
			std::cout << "Title: " << title << std::endl;
			std::cout << "Genre: " << genre << std::endl;
			std::cout << "Year: " << year << std::endl;
			std::cout << "Likes: " << likes << std::endl;
            m.play();
			std::cout << "Do you want to add this movie to the watchlist? (y/n): ";
			std::string answer;
			std::getline(std::cin, answer);
            if (answer == "y")
            {
                if(this->service.addMovieToWatchlist(m) == true)
                    std::cout << "Movie added to watchlist." << std::endl;
                else
					std::cout << "Movie already in watchlist." << std::endl;
            }
			else if (answer == "n")
			{
				std::cout << "Movie not added to watchlist." << std::endl;
			}
			std::cout << "Do you want to see another movie? (y/n): ";
			std::getline(std::cin, answer);
            if (answer == "n")
            {
                return;
            }

	    }
}

void UI::deleteMovieFromWatchList()
{
	if (this->service.isWatchlistEmpty())
	{
		std::cout << "There are no movies in the watchlist." << std::endl;
		return;
	}
	try
	{
		std::string title;
		std::cout << "Enter the title: ";
		std::getline(std::cin, title);
		std::cout << "Did you like the movie? (y/n): ";
		std::string answer;
		std::getline(std::cin, answer);
		if (answer == "y")
		{
			this->service.deleteMovieFromWatchlist(title, 1);
			std::cout << "Movie liked." << std::endl;
		}
		else if (answer == "n")
		{
            this->service.deleteMovieFromWatchlist(title, 0);
			std::cout << "Movie not liked." << std::endl;
		}
		else
		{
			std::cout << "Invalid answer." << std::endl;
			return;
		}
	}
	catch (const std::exception& e)
	{
		std::cerr << "Error: " << e.what() << std::endl;
	}
}

void UI::printWatchList()
{
	if (this->service.isWatchlistEmpty())
	{
		std::cout << "There are no movies in the watchlist." << std::endl;
		return;
	}
	int index = 1;
	vector<Movie> watchList = this->service.getWatchlist()->getMovies();
	for (int i = 0; i < watchList.size(); i++)
	{
		Movie m = watchList[i];
		std::cout<< index++ << ". " << m.toString() << std::endl;
	}
}

void UI::saveWatchlist()
{
	std::string filename;
	std::cout << "Enter the filename (absolute path): ";
	std::getline(std::cin, filename);
    try
    {
        this->service.saveWatchlist(filename);

        if (this->service.getWatchlist() == nullptr)
        {
			std::cout << "Watchlist cannot be displayed." << std::endl;
			return;
        }
    }
    catch (FileException& e)
    {
		std::cout << e.what() << std::endl;
	}
}


void UI::run()
{
    while (true)
    {
        int mode{ 0 };
        mode = menuMode();

        if (mode == 1)
        {
            while (true)
            {
                UI::printAdminMenu();
                int command{ 0 };
                std::cout << "Enter the command: ";
                std::cin >> command;
                std::cin.ignore();
                if (command == 0)
                    break;
                if (command < 0 || command > 4)
                {
                    std::cout << "Invalid command!" << std::endl;
                    continue;
                }
                if (std::cin.fail())
                {
                    std::cin.clear();
                    std::cin.ignore();
                    std::cout << "Invalid command!" << std::endl;
                    continue;
                }
                try
                {
                    switch (command)
                    {
                    case 1:
                        this->addMovieToRepo();
                        break;
                    case 2:
                        this->deleteMovieFromRepo();
                        break;
                    case 3:
                        this->updateMovie();
                        break;
                    case 4:
                        this->printMoviesRepo();
                        break;
                    default:
                        std::cout << "Invalid command!" << std::endl;
                        continue;
                    }
                }
                catch (const std::exception& e)
                {
                    std::cerr << "Error: " << e.what() << std::endl;
                }
            }
        }
        else if (mode == 2)
        {
            while (true)
            {
                printUserMenu();
                int command{ 0 };
                std::cout << "Enter the command: ";
                std::cin >> command;
                std::cin.ignore();
                if (command == 0)
                    break;
                if (command < 0 || command > 5)
                {
                    std::cout << "Invalid command!" << std::endl;
                    continue;
                }
                if (std::cin.fail())
                {
                    std::cin.clear();
                    std::cin.ignore();
                    std::cout << "Invalid command!" << std::endl;
                    continue;
                }
                try
                {
                    switch (command)
                    {
                    case 1:
                        this->printMoviesByGenre();
                        break;
                    case 2:
                        this->deleteMovieFromWatchList();
                        break;
                    case 3:
                        this->printWatchList();
                        break;
					case 4:
						this->saveWatchlist();
						break;
					case 5:
						this->service.openWatchlist();
						break;
                    default:
                        std::cout << "Invalid command!" << std::endl;
                        continue;
                    }
                }
                catch (const std::exception& e)
                {
                    std::cerr << "Error: " << e.what() << std::endl;
                }
            }
        }
        else if (mode == 0)
        {
            std::cout << "Goodbye!" << std::endl;
            break;
        }
        else
        {
            std::cout << "Invalid command!" << std::endl;
        }
    }
}
