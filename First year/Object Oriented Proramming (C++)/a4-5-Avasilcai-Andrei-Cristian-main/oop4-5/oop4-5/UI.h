#pragma once
#include "AdminService.h"
#include "UserService.h"
class UI
{
private:
	AdminService& adminService;
	UserService& userService;
public:
	// Default constructor for an UI
	UI(AdminService& adminService, UserService& userService) : adminService{ adminService }, userService{ userService } {}
	// Runs the UI
	void run();
private:

	//Chooses the mode of the application
	int menuMode();

	// Prints the admin menu
	static void printAdminMenu();
	// Adds a movie
	void addAdminMovie();
	// Deletes a movie
	void deleteAdminMovie();
	// Updates a movie
	void updateAdminMovie();
	// Prints all the movies
	void printAdminMovies();
	// Prints the movies with a given genre

	// Prints the watchlist
	void printUserWatchList();
	// Adds a movie to the watchlist
	void addUserMovieToWatchList();
	// Deletes a movie from the watchlist
	void deleteUserMovieFromWatchList();
	// Prints the movies of a given genre
	void printUserMoviesByGenre();
	// Prints the user menu
	static void printUserMenu();
};
