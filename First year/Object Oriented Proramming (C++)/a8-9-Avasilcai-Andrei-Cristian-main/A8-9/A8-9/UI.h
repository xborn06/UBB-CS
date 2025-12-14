#pragma once
#include "Service.h"
class UI
{
private:
	Service& service;
public:
	// Default constructor for an UI
	UI(Service& s) : service(s) {}
	// Runs the UI
	void run();
private:

	//Chooses the mode of the application
	int menuMode();

	// Prints the admin menu
	static void printAdminMenu();
	// Adds a movie
	void addMovieToRepo();
	// Deletes a movie
	void deleteMovieFromRepo();
	// Updates a movie
	void updateMovie();
	// Prints all the movies
	void printMoviesRepo();
	// Prints the movies with a given genre

	// Prints the watchlist
	void printWatchList();
	// Deletes a movie from the watchlist
	void deleteMovieFromWatchList();
	// Prints the movies of a given genre
	void printMoviesByGenre();
	// Prints the user menu
	static void printUserMenu();
	//Saves the watchlist to file
	void saveWatchlist();
};
