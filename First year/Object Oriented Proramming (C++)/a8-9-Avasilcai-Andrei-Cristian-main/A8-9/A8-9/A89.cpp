#include "A89.h"
#include <qboxlayout.h>
#include <QtWidgets/QLabel>
#include <QtWidgets/QFormLayout>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QMessageBox>
#include <string>
#include <exception>
#include <sstream>
#include "CSVWatchlist.h"
#include "HTMLWatchlist.h"
#include "RepositoryExceptions.h"


A89::A89(Service service) : service(service)
{
	this->setupUI();
	this->createOperationsLayout();
}

void A89::setupUI()
{
	this->movieListW = nullptr;
	this->watchListW = nullptr;
	this->filteredMoviesW = nullptr;
	this->titleLE = nullptr;
	this->genreLE = nullptr;
	this->yearLE = nullptr;
	this->likesLE = nullptr;
	this->trailerLE = nullptr;
	this->filenameLE = nullptr;

	this->setWindowTitle("Movie Manager");
	this->resize(800, 600);
}

void A89::createOperationsLayout()
{
	QMessageBox* messageBox = new QMessageBox{};
	messageBox->setWindowTitle("Choose mode");
	messageBox->setText("Choose mode");
	QPushButton* adminModeButton = new QPushButton{ "Admin mode" };
	QPushButton* userModeButton = new QPushButton{ "User mode" };
	connect(adminModeButton, &QPushButton::clicked, this, &A89::handleAdminModeButton);
	connect(userModeButton, &QPushButton::clicked, this, &A89::handleUserModeButton);
	messageBox->addButton(adminModeButton, QMessageBox::AcceptRole);
	messageBox->addButton(userModeButton, QMessageBox::RejectRole);
	messageBox->exec();
}


void A89::handleAdminModeButton()
{
	QVBoxLayout* mainLayout = new QVBoxLayout{ this };
    QFormLayout* formLayout = new QFormLayout{};
    QLabel* titleLabel = new QLabel{ "Title" };
    QLabel* genreLabel = new QLabel{ "Gnere" };
    QLabel* yearLabel = new QLabel{ "Year" };
    QLabel* likesLabel = new QLabel{ "Likes" };
    QLabel* trailerLabel = new QLabel{ "Trailer" };
    this->titleLE = new QLineEdit();
    this->genreLE = new QLineEdit();
    this->yearLE = new QLineEdit();
    this->likesLE = new QLineEdit();
    this->trailerLE = new QLineEdit();
    formLayout->addRow(titleLabel, this->titleLE);
    formLayout->addRow(genreLabel, this->genreLE);
    formLayout->addRow(yearLabel, this->yearLE);
    formLayout->addRow(likesLabel, this->likesLE);
    formLayout->addRow(trailerLabel, this->trailerLE);

    this->movieListW = new QListWidget{};
    this->populateList();
    mainLayout->addWidget(movieListW);
    mainLayout->addLayout(formLayout);

	QPushButton* addButton = new QPushButton{ "Add" };
	connect(addButton, &QPushButton::clicked, this, &A89::handleAddButton);
	QPushButton* removeButton = new QPushButton{ "Remove" };
	connect(removeButton, &QPushButton::clicked, this, &A89::handleRemoveButton);
	QPushButton* update = new QPushButton{ "Update" };
	connect(update, &QPushButton::clicked, this, &A89::handleUpdateButton);
	mainLayout->addWidget(addButton);
	mainLayout->addWidget(removeButton);
	mainLayout->addWidget(update);
}

void A89::populateWatchlist()
{
	std::vector<Movie> movies = this->service.getWatchlist()->getMovies();
		this->watchListW->clear();
	for (int i = 0; i < movies.size(); ++i)
	{
		std::stringstream stream;
		stream << movies[i];
		new QListWidgetItem(tr(stream.str().c_str()), watchListW);
	}
}

void A89::populateFilteredMovies(int index)
{
	//this should show one by one the movies of a given genre and using the next button
	this->filteredMoviesW->clear();
	std::stringstream stream;
	if (index >= 0 && index < this->filteredMovies.size()) {
		stream << this->filteredMovies[index];
		Movie m = this->filteredMovies[index];
		m.play();
	}

	new QListWidgetItem(tr(stream.str().c_str()), filteredMoviesW);
}


void A89::handleUserModeButton()
{
    //firstly we ask the user to choose in which mode he wants to store the watchlist (html or csv)
	QMessageBox* messageBox = new QMessageBox{};
	messageBox->setWindowTitle("Choose mode");
	messageBox->setText("Choose mode");
	QPushButton* csvModeButton = new QPushButton{ "CSV mode" };
	QPushButton* htmlModeButton = new QPushButton{ "HTML mode" };
	connect(csvModeButton, &QPushButton::clicked, this, &A89::handleCSV);
    connect(htmlModeButton, &QPushButton::clicked, this, &A89::handleHTML);
	messageBox->addButton(csvModeButton, QMessageBox::AcceptRole);
	messageBox->addButton(htmlModeButton, QMessageBox::RejectRole);
	messageBox->exec();
    QVBoxLayout* mainLayout = new QVBoxLayout{ this };
    QFormLayout* formLayout = new QFormLayout{};
	QLabel* genreLabel = new QLabel{ "Genre" };
	QLabel* filenameLabel = new QLabel{ "Filename" };
	this->genreLE = new QLineEdit();
	this->filenameLE = new QLineEdit();
	this->titleLE = new QLineEdit();
	this->yearLE = new QLineEdit();
	this->likesLE = new QLineEdit();
	this->trailerLE = new QLineEdit();
	formLayout->addRow(genreLabel, this->genreLE);
	formLayout->addRow(filenameLabel, this->filenameLE);
	formLayout->addRow("Title", this->titleLE);
	mainLayout->addLayout(formLayout);

	
	QLabel* watchlistLabel = new QLabel{ "Watchlist" };
	this->watchListW = new QListWidget{};
	this->populateWatchlist();

	QLabel* filteredMoviesLabel = new QLabel{ "Filtered movies" };
	this->filteredMoviesW = new QListWidget{};
	this->populateFilteredMovies(this->currentIndex);
	QPushButton* filterButton = new QPushButton{ "Filter" };
	connect(filterButton, &QPushButton::clicked, this, [this]() {
		this->currentIndex = 0;
		std::string genre = this->genreLE->text().toStdString();
		this->filteredMovies = this->service.getRepo().getMoviesByGenre(genre);
		this->populateFilteredMovies(this->currentIndex);
		});



	mainLayout->addWidget(this->watchListW);
	mainLayout->addWidget(watchlistLabel);
	mainLayout->addWidget(this->filteredMoviesW);
	mainLayout->addWidget(filteredMoviesLabel);
	mainLayout->addWidget(filterButton);
	mainLayout->addWidget(filteredMoviesLabel);
	mainLayout->addWidget(this->filteredMoviesW);
	mainLayout->addWidget(filterButton);



	QPushButton* addToWatchlistButton = new QPushButton{ "Add to watchlist" };
	connect(addToWatchlistButton, &QPushButton::clicked, this, [this]() {
		if (this->filteredMovies.empty() || this->currentIndex < 0 || this->currentIndex >= this->filteredMovies.size()) {
			QMessageBox::warning(this, "Error", "No movie selected to add to watchlist.");
			return;
		}
		const Movie& m = this->filteredMovies[this->currentIndex];
		this->service.addMovieToWatchlist(m);
		this->populateWatchlist();
		});

	QPushButton* nextButton = new QPushButton{ "Next" };
	connect(nextButton, &QPushButton::clicked, this, [this]() {
		if (this->currentIndex == this->filteredMovies.size())
			this->currentIndex = 0;
		else
			this->currentIndex++;
		this->populateFilteredMovies(this->currentIndex);
		});

	QPushButton* removeButton = new QPushButton{ "Remove from watchlist" };
	connect(removeButton, &QPushButton::clicked, this, [this]() {
		std::string title = this->titleLE->text().toStdString();
		if (title.empty()) {
			QMessageBox::warning(this, "Error", "Please enter the title of the movie to remove from the watchlist.");
			return;
		}

		QMessageBox::StandardButton reply;
		reply = QMessageBox::question(this, "Like Movie", "Did you like the movie?",
			QMessageBox::Yes | QMessageBox::No);
		bool isLiked = (reply == QMessageBox::Yes);
		this->service.deleteMovieFromWatchlist(title, isLiked);
		this->populateWatchlist();
		});


	QPushButton* saveButton = new QPushButton{ "Save" };
	connect(saveButton, &QPushButton::clicked, this, [this]() {
		std::string filename = this->filenameLE->text().toStdString();
		if (filename.empty()) {
			QMessageBox::warning(this, "Error", "Please enter a filename.");
			return;
		}
		this->service.saveWatchlist(filename);
		});

	QPushButton* openWatchlistButton = new QPushButton{ "Open watchlist" };
	connect(openWatchlistButton, &QPushButton::clicked, this, [this]() {
		this->service.openWatchlist();
		});


	QPushButton* exitButton = new QPushButton{ "Exit" };
	connect(exitButton, &QPushButton::clicked, this, [this]() {
		this->close();
		});

	mainLayout->addWidget(saveButton);
	mainLayout->addWidget(openWatchlistButton);
	mainLayout->addWidget(addToWatchlistButton);
	mainLayout->addWidget(nextButton);
	mainLayout->addWidget(removeButton);
	mainLayout->addWidget(exitButton);
	this->setLayout(mainLayout);
}

void A89::handleCSV()
{
    FileWatchlist* watchlist = nullptr;
    watchlist = new CSVWatchlist{};
	watchlist->setFilename("");
	this->service.setWatchlist(watchlist);
}

void A89::handleHTML()
{
	FileWatchlist* watchlist = nullptr;
	watchlist = new HTMLWatchlist{};
	watchlist->setFilename("");
	this->service.setWatchlist(watchlist);
}

void A89::handleAddButton()
{
    try
    {
        std::string title = this->titleLE->text().toStdString();
        std::string genre = this->genreLE->text().toStdString();
        int year = stoi(this->yearLE->text().toStdString());
        int likes = stoi(this->likesLE->text().toStdString());
        std::string trailer = this->trailerLE->text().toStdString();
        service.addMovieToRepository(title, genre, year, likes, trailer);
        this->populateList();
    }
    catch (std::exception e)
    {
        QMessageBox* messageBox = new QMessageBox{};
        messageBox->setWindowTitle("Error when adding!");
        messageBox->setText(e.what());
        messageBox->exec();
    }
}

void A89::handleUpdateButton()
{
    try
    {
		std::string title = this->titleLE->text().toStdString();
		std::string genre = this->genreLE->text().toStdString();
		int year = stoi(this->yearLE->text().toStdString());
		int likes = stoi(this->likesLE->text().toStdString());
		std::string trailer = this->trailerLE->text().toStdString();
		this->service.updateMovieToRepository(title, genre, year, likes, trailer);
		this->populateList();
    }
    catch (std::exception e)
	{
		QMessageBox* messageBox = new QMessageBox{};
		messageBox->setWindowTitle("Error when updating!");
		messageBox->setText(e.what());
		messageBox->exec();

    }
}

void A89::populateList()
{
    std::vector<Movie> movies = this->service.getRepo().getMovies();
    this->movieListW->clear();
    for (int i = 0; i < movies.size(); ++i)
    {
        std::stringstream stream;
        stream << movies[i];
        new QListWidgetItem(tr(stream.str().c_str()), movieListW);
    }
}

void A89::handleRemoveButton() {
	try {
		this->service.deleteMovieFromRepository(this->titleLE->text().toStdString());
		this->populateList();
	}
	catch (std::exception e)
	{
		QMessageBox* messageBox = new QMessageBox{};
		messageBox->setWindowTitle("Error when removing!");
		messageBox->setText(e.what());
		messageBox->exec();
	}
}

A89::~A89()
{}
