#include <sstream>
#include <string>
#include <vector>


std::vector<std::string> tokenize(const std::string& input, char delimiter) {
	std::vector<std::string> result;
	std::stringstream stream{ input };
	std::string token;

	while (getline(stream, token, delimiter))
		result.push_back(token);

	return result;
}