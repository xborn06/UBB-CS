#include "A89.h"
#include <QtWidgets/QApplication>
#include "Repository.h"
#include "Service.h"
#include "UI.h"
#include "CSVWatchlist.h"
#include <iostream>
#include "HTMLWatchlist.h"
int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    
    Repository repository{ "movies.txt" };
    FileWatchlist* watchlist = nullptr;
    watchlist = new CSVWatchlist{};
    MovieValidator validator{};
    Service service{ repository, watchlist, validator };
    
    A89 w{ service };
    w.show();
    
    return a.exec();
}
