#pragma once

#include <QtWidgets/QMainWindow>
#include <QtWidgets/QWidget>
#include <QtWidgets/QVBoxLayout>
#include <QtWidgets/QLineEdit>
#include <QtWidgets/QListWidget>
#include "ui_A89.h"
#include "Service.h"

class A89 : public QWidget
{
    Q_OBJECT

public:
    A89(Service service);
    ~A89();

private:
    std::vector<Movie> filteredMovies;
    int currentIndex = 0;
    Service service;
    Ui::A89Class ui;
    QListWidget* movieListW;
	QListWidget* watchListW;
	QListWidget* filteredMoviesW;
    QLineEdit* titleLE;
    QLineEdit* genreLE;
    QLineEdit* yearLE;
    QLineEdit* likesLE;
    QLineEdit* trailerLE;
	QLineEdit* filenameLE;

    void setupUI();
    void populateList();
    void createOperationsLayout();
    void handleAddButton();
    void handleRemoveButton();
	void handleUpdateButton();
	void handleAdminModeButton();
	void handleUserModeButton();
	void handleCSV();
	void handleHTML();
	void populateFilteredMovies(int index);
    void populateWatchlist();
};
