#pragma once
#include <exception>
#include <string>

class RepositoryException : std::exception {
protected:
	std::string message;
public:
	RepositoryException(std::string msg) : message(msg) {}
	const char *what() {return message.c_str(); }
};