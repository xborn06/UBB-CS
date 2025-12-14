#include "Validation.h"


MovieException::MovieException(std::vector<std::string>_errors) : errors{ _errors }
{
}

std::vector<std::string>MovieException::getErrors() const
{
	return this->errors;
}

void MovieValidator::validate(const Movie& m)
{
	std::vector<std::string> errors;
	if (m.getTitle().size() < 2)
		errors.push_back("The title name cannot be less than 2 characters!\n");
	if (m.getGenre().size() < 3)
		errors.push_back("The genre name cannot be less than 3 characters!\n");
	if (m.getLikes() < 0)
		errors.push_back("The likes cannot be negative!\n");
	if (m.getYear() < 1930)
		errors.push_back("The release year cannot be earlier than 1930!\n");
	if (!isupper(m.getGenre()[0]))
		errors.push_back("The genre name must start with a capital letter!\n");

	size_t posWww = m.getTrailer().find("www");
	size_t posHttp = m.getTrailer().find("http");
	if (posWww != 0 && posHttp != 0)
		errors.push_back("The trailer link must start with one of the following strings: \"www\" or \"http\"");

	if (errors.size() > 0)
		throw(MovieException(errors));
}