#include "Tests.h"
#include <iostream>
#include <assert.h>

void Tests::testDynamicVector()
{
	DynamicVector<Movie> dv;
	assert(dv.getSize() == 0);
	assert(dv.getCapacity() == 10);
	Movie m1("Movie1", "Genre1", 2000, 10, "Trailer1");
	Movie m2("Movie2", "Genre2", 2001, 20, "Trailer2");
	Movie m3("Movie2", "Genre2", 2001, 20, "Trailer2");
	assert(m3 == m2);
	dv.add(m1);
	dv.add(m2);
	dv[1] = m3;
	assert(dv.getSize() == 2);
	assert(dv[0] == m1);
	assert(dv[1] == m2);
	assert(dv.find(m1) == 0);
	dv.remove(1);
	assert(dv.find(m2)==-1);
	dv.remove(0);
	assert(dv.getSize() == 0);
	try {
		dv.update(0, m1);

	}
	catch (const std::exception& e) {}
	try
	{
		dv.update(1, m2);
	}
	catch (const std::exception& e) {}
	try {
		dv.remove(2);
	}
	catch (const std::exception& e) {}
	try {
		dv[2];
	}
	catch (const std::exception& e) {}
}

void Tests::testMovie()
{
	Movie m("Movie1", "Genre1", 2000, 10, "Trailer1");
	assert(m.getTitle() == "Movie1");
	assert(m.getGenre() == "Genre1");
	assert(m.getYear() == 2000);
	assert(m.getLikes() == 10);
	assert(m.getTrailer() == "Trailer1");
	m.increaseLikes();
	assert(m.getLikes() == 11);
	assert(m.toString() == "Movie1 - Genre1 - 2000 - 11 - Trailer1");
	assert(m.toStringShort() == "Movie1 - 2000 - 11");
	m.setTitle("Movie2");
	assert(m.getTitle() == "Movie2");
	m.setGenre("Genre2");
	assert(m.getGenre() == "Genre2");
	m.setYear(2001);
	assert(m.getYear() == 2001);
	m.setLikes(20);
	assert(m.getLikes() == 20);
}

void Tests::testRepository()
{
	Repository repo;
	assert(repo.getMovies().getSize() == 0);
	Movie m1("Movie1", "Genre1", 2000, 10, "Trailer1");
	Movie m2("Movie2", "Genre2", 2001, 20, "Trailer2");
	repo.addMovie(m1);
	repo.addMovie(m2);
	assert(repo.getMovies().getSize() == 2);
	assert(repo.getMovieByTitle("Movie1") == m1);
	assert(repo.getMovieByTitle("Movie2") == m2);
	repo.deleteMovie("Movie1");
	assert(repo.getMovies().getSize() == 1);
	assert(repo.getMovieByTitle("Movie1").getTitle() == "");
	repo.deleteMovie("Movie2");
	assert(repo.getMovies().getSize() == 0);
}

void Tests::testGetAllMovies()
{
	Repository repo;
	Movie m1("Movie1", "Genre1", 2000, 10, "Trailer1");
	Movie m2("Movie2", "Genre2", 2001, 20, "Trailer2");
	repo.addMovie(m1);
	repo.addMovie(m2);
	DynamicVector<Movie> movies = repo.getMovies();
	assert(movies.getSize() == 2);
	assert(movies[0] == m1);
	assert(movies[1] == m2);
}

void Tests::testAddMovieToRepository()
{
	Repository repo;
	Movie m1("Movie1", "Genre1", 2000, 10, "Trailer1");
	repo.addMovie(m1);
	assert(repo.getMovies().getSize() == 1);
	assert(repo.getMovies()[0] == m1);
}

void Tests::testDeleteMovieFromRepository()
{
	Repository repo;
	Movie m1("Movie1", "Genre1", 2000, 10, "Trailer1");
	repo.addMovie(m1);
	repo.deleteMovie("Movie1");
	assert(repo.getMovies().getSize() == 0);
}

void Tests::testUpdateMovieInRepository()
{
	Repository repo;
	Movie m1("Movie1", "Genre1", 2000, 10, "Trailer1");
	repo.addMovie(m1);
	Movie m2("Movie1", "Genre2", 2001, 20, "Trailer2");
	repo.updateMovie(m2);
	assert(repo.getMovies().getSize() == 1);
	assert(repo.getMovies()[0] == m2);
}

void Tests::testIncreaseLikes()
{
	Repository repo;
	Movie m1("Movie1", "Genre1", 2000, 10, "Trailer1");
	repo.addMovie(m1);
	repo.increaseLikes("Movie1");
	assert(repo.getMovies()[0].getLikes() == 11);
}

void Tests::testGetMovieByTitle()
{
	Repository repo;
	Movie m1("Movie1", "Genre1", 2000, 10, "Trailer1");
	repo.addMovie(m1);
	assert(repo.getMovieByTitle("Movie1") == m1);
}

void Tests::testFindMovieByTitle()
{
	Repository repo;
	Movie m1("Movie1", "Genre1", 2000, 10, "Trailer1");
	repo.addMovie(m1);
	assert(repo.findMovieByTitle("Movie1") == 0);
	assert(repo.findMovieByTitle("Movie2") == -1);
}

void Tests::testAdminServiceAddMovie()
{
	Repository repo;
	AdminService adminService(repo);
	Movie m1("Movie1", "Genre1", 2000, 10, "Trailer1");
	adminService.addMovie("Movie1", "Genre1", 2000, 10, "Trailer1");
	assert(repo.getMovies().getSize() == 1);
	assert(repo.getMovies()[0] == m1);
	try {
		adminService.addMovie("Movie1", "Genre1", 2000, 10, "Trailer1");
	}
	catch (const std::exception& e) {}
	try {
		adminService.addMovie("", "Genre1", 2000, 10, "Trailer1");
	}
	catch (const std::exception& e) {}
	try {
		adminService.addMovie("Movie2", "", 2000, 10, "Trailer1");
	}
	catch (const std::exception& e) {}
	try {
		adminService.addMovie("Movie2", "Genre1", -2000, 10, "Trailer1");
	}
	catch (const std::exception& e) {}
	try {
		adminService.addMovie("Movie2", "Genre1", 2000, -10, "Trailer1");
	}
	catch (const std::exception& e) {}
	try {
		adminService.addMovie("Movie2", "Genre1", 2000, 10, "");
	}
	catch (const std::exception& e) {}
}

void Tests::testAdminServiceDeleteMovie()
{
	Repository repo;
	AdminService adminService(repo);
	adminService.addMovie("Movie1", "Genre1", 2000, 10, "Trailer1");
	adminService.deleteMovie("Movie1");
	assert(repo.getMovies().getSize() == 0);
	try
	{
		adminService.deleteMovie("Movie2");
	}
	catch (const std::exception& e) {}
}

void Tests::testAdminServiceUpdateMovie()
{
	Repository repo;
	AdminService adminService(repo);
	adminService.addMovie("Movie1", "Genre1", 2000, 10, "Trailer1");
	adminService.updateMovie("Movie1", "Genre2", 2001, 20, "Trailer2");
	assert(repo.getMovies().getSize() == 1);
	assert(repo.getMovies()[0].getGenre() == "Genre2");
	try
	{
		adminService.updateMovie("Movie2", "Genre2", 2001, 20, "Trailer2");
	}
	catch (const std::exception& e) {}
	try
	{
		adminService.updateMovie("Movie1", "Genre2", 2001, -20, "Trailer2");
	}
	catch (const std::exception& e) {}
	try
	{
		adminService.updateMovie("", "Genre2", 2001, 20, "Trailer2");
	}
	catch (const std::exception& e) {}
	try
	{
		adminService.updateMovie("Movie1", "", 2001, 20, "Trailer2");
	}
	catch (const std::exception& e) {}
	try
	{
		adminService.updateMovie("Movie1", "Genre2", -2001, 20, "Trailer2");
	}
	catch (const std::exception& e) {}
	try
	{
		adminService.updateMovie("Movie1", "Genre2", 2001, 20, "");
	}
	catch (const std::exception& e) {}
}

void Tests::testAdminService()
{
	Repository repo;
	AdminService adminService(repo);
	adminService.addMovie("Movie1", "Genre1", 2000, 10, "Trailer1");
	adminService.addMovie("Movie2", "Genre2", 2001, 20, "Trailer2");
	assert(adminService.getMovies().getSize() == 2);
	adminService.increaseLikes("Movie1");
	assert(repo.getMovies()[0].getLikes() == 11);
	Movie m2 = adminService.getMovies()[1];
	try
	{
		adminService.increaseLikes("Movie3");
	}
	catch (const std::exception& e) {}
	Movie m1;
	m1 = adminService.getMovieByTitle("Movie1");
	assert(m1.getTitle() == "Movie1");
	assert(m1.getGenre() == "Genre1");
	assert(m1.getYear() == 2000);
	assert(m1.getLikes() == 11);
	assert(m1.getTrailer() == "Trailer1");
	try
	{
		m1 = adminService.getMovieByTitle("Movie4");
	}
	catch (const std::exception& e) {}
}

void Tests::testGetMoviesByGenre()
{
	Repository repo;
	AdminService adminService(repo);
	UserService userService(repo);
	adminService.addMovie("Movie1", "Genre1", 2000, 10, "Trailer1");
	adminService.addMovie("Movie2", "Genre2", 2001, 20, "Trailer2");
	DynamicVector<Movie> movies = userService.getMoviesbyGenre(adminService.getMovies(), "Genre1");
	assert(movies.getSize() == 1);
	assert(movies[0].getTitle() == "Movie1");
	movies = userService.getMoviesbyGenre(adminService.getMovies(), "");
	assert(movies.getSize() == 2);
}

void Tests::testAddMovieToWatchList()
{
	Repository repo;
	UserService userService(repo);
	Movie m1("Movie1", "Genre1", 2000, 10, "Trailer1");
	repo.addMovie(m1);
	userService.addMovieToWatchList(m1.getTitle());
	assert(userService.getWatchList().getSize() == 1);
	assert(userService.getWatchList()[0] == m1);
	assert(userService.addMovieToWatchList("Movie2") == false);
	assert(userService.addMovieToWatchList("Movie1") == false);
}

void Tests::testDeleteMovieFromWatchList()
{
	Repository repo;
	UserService userService(repo);
	Movie m1("Movie1", "Genre1", 2000, 10, "Trailer1");
	repo.addMovie(m1);
	userService.addMovieToWatchList(m1.getTitle());
	assert(userService.deleteMovieFromWatchList(m1.getTitle()) == true);
	assert(userService.getWatchList().getSize() == 0);
	assert(userService.deleteMovieFromWatchList("Movie2") == false);
}

void Tests::testUserService()
{
	Repository repo;
	UserService userService(repo);
	Movie m1("Movie1", "Genre1", 2000, 10, "Trailer1");
	repo.addMovie(m1);
	userService.addMovieToWatchList(m1.getTitle());
	assert(userService.getWatchList().getSize() == 1);
	assert(userService.getWatchList()[0] == m1);
}

void Tests::runAllTests()
{
	testDynamicVector();
	testMovie();
	testRepository();
	testGetAllMovies();
	testAddMovieToRepository();
	testDeleteMovieFromRepository();
	testUpdateMovieInRepository();
	testIncreaseLikes();
	testGetMovieByTitle();
	testFindMovieByTitle();
	testAdminServiceAddMovie();
	testAdminServiceDeleteMovie();
	testAdminServiceUpdateMovie();
	testAdminService();
	testGetMoviesByGenre();
	testAddMovieToWatchList();
	testDeleteMovieFromWatchList();
	testUserService();
	std::cout << "All tests passed!" << std::endl;
}