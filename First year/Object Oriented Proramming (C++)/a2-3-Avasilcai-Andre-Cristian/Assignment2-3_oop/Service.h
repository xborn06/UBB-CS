#pragma once
#include "Repo.h"

typedef struct {
	Repo* repo;
}Service;

Service* createService(Repo* repo);
void destroyService(Service* service);
int addEstateService(Service* service, char* type, char* address, int surface, int price);
int deleteEstateService(Service* service, char* address);
int updateEstateService(Service* service, char* type, char* address, int surface, int price, char* original_address);
void search_by_address(Service* service, char* address, Estate* result, int* length);
int filter_by_size(Service* service, Estate* result, int* length,char* type,int surface);
Repo* getRepo(Service* service);