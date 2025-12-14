#include <sstream>
#include <string>
#include <vector>

using namespace std;

vector<string> tokenize(const string& input, char delimiter) {
	vector<string> result;
	stringstream stream{ input };
	string token;

	while (getline(stream, token, delimiter))
		result.push_back(token);

	return result;
}