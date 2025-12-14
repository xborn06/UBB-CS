#include "UI.h"
#include <iostream>
#include <string>

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

void UI::addAdminMovie()
{
    try
    {
        std::string title, genre, trailer;
        int year, likes;
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
        this->adminService.addMovie(title, genre, year, likes, trailer);
    }
    catch (const std::exception& e)
    {
        std::cerr << "Error: " << e.what() << std::endl;
    }
}

void UI::deleteAdminMovie()
{
	if (this->adminService.getMovies().getSize() == 0)
	{
		std::cout << "There are no movies in the repository." << std::endl;
		return;
	}
    try
    {
        std::string title;
        std::cout << "Enter the title: ";
        std::getline(std::cin, title);
        this->adminService.deleteMovie(title);
    }
    catch (const std::exception& e)
    {
        std::cerr << "Error: " << e.what() << std::endl;
    }
}

void UI::updateAdminMovie()
{
	if (this->adminService.getMovies().getSize() == 0)
	{
		std::cout << "There are no movies in the repository." << std::endl;
		return;
	}
    try
    {
        std::string title, genre, trailer;
        int year, likes;
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
        this->adminService.updateMovie(title, genre, year, likes, trailer);
    }
    catch (const std::exception& e)
    {
        std::cerr << "Error: " << e.what() << std::endl;
    }
}

void UI::printAdminMovies()
{
    try
    {
        DynamicVector<Movie> movies = this->adminService.getMovies();
        for (int i = 0; i < movies.getSize(); i++)
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
	std::cout << "0. Exit." << std::endl;
}

void UI::printUserMoviesByGenre()
{
	std::string genre;
	std::cout << "Enter the genre: ";
	std::getline(std::cin, genre);
	DynamicVector<Movie> movies = this->userService.getMoviesbyGenre(this->adminService.getMovies(), genre);
	if (movies.getSize() == 0)
	{
		std::cout << "There are no movies of this genre." << std::endl;
		return;
	}
    int index = 1;
    while(true)
	    for (int i = 0; i < movies.getSize(); i++)
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
			std::string command = "start " + link;
            system(command.c_str());
			std::cout << "Do you want to add this movie to the watchlist? (y/n): ";
			std::string answer;
			std::getline(std::cin, answer);
            if (answer == "y")
            {
                if(this->userService.addMovieToWatchList(m.getTitle()) == true)
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

void UI::deleteUserMovieFromWatchList()
{
	if (this->userService.getWatchList().getSize() == 0)
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
			this->adminService.increaseLikes(title);
			std::cout << "Movie liked." << std::endl;
		}
		else if (answer == "n")
		{
			std::cout << "Movie not liked." << std::endl;
		}
		else
		{
			std::cout << "Invalid answer." << std::endl;
			return;
		}
		this->userService.deleteMovieFromWatchList(title);
	}
	catch (const std::exception& e)
	{
		std::cerr << "Error: " << e.what() << std::endl;
	}
}

void UI::printUserWatchList()
{
	if (this->userService.getWatchList().getSize() == 0)
	{
		std::cout << "There are no movies in the watchlist." << std::endl;
		return;
	}
	int index = 1;
	DynamicVector<Movie> watchList = this->userService.getWatchList();
	for (int i = 0; i < watchList.getSize(); i++)
	{
		Movie m = watchList[i];
		std::cout<< index++ << ". " << m.toString() << std::endl;
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
                        this->addAdminMovie();
                        break;
                    case 2:
                        this->deleteAdminMovie();
                        break;
                    case 3:
                        this->updateAdminMovie();
                        break;
                    case 4:
                        this->printAdminMovies();
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
                if (command < 0 || command > 3)
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
                        this->printUserMoviesByGenre();
                        break;
                    case 2:
                        this->deleteUserMovieFromWatchList();
                        break;
                    case 3:
                        this->printUserWatchList();
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
