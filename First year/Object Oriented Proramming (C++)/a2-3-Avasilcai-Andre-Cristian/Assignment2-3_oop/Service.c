#define _CRT_SECURE_NO_WARNINGS
#include "Service.h"
#include <string.h>
#include <stdlib.h>

Service* createService(Repo* repo) {
	Service* service = (Service*)malloc(sizeof(Service));
	if (service == NULL) {
		return NULL;
	}
	service->repo = repo;
	return service;
}

void destroyService(Service* service) {
	if (service == NULL) {
		return;
	}
	destroyRepo(service->repo);
	free(service);
}

int addEstateService(Service* service, char* type, char* address, int surface, int price) {
	if (service == NULL) {
		return 0;
	}
	if (strlen(type) == 0 || strlen(address) == 0 || surface <= 0 || price <= 0) {
		return 0;
	}
	if (type != "house" && type != "apartment" && type != "penthouse") {
		return 0;
	}
	Estate* estate = createEstate(type, address, surface, price);
	addEstate(service->repo, estate);
	return 1;
}

int deleteEstateService(Service* service, char* address) {
	if (service == NULL) {
		return 0;
	}
	if (strlen(address) == 0) {
		return 0;
	}
	Estate* estate = createEstate("", address, 0, 0);
	deleteEstate(service->repo, estate);
	return 1;
}

int updateEstateService(Service* service, char* type, char* address, int surface, int price, char* original_address) {
	if (service == NULL) {
		return 0;
	}
	if (strlen(type) == 0 || strlen(address) == 0 || surface <= 0 || price <= 0 || strlen(original_address) == 0) {
		return 0;
	}
	Estate* estate = createEstate(type, address, surface, price);
	updateEstate(service->repo, estate, original_address);
	return 1;
}

void search_by_address(Service* service, char* address, Estate* result, int* length) {
	if (service == NULL) {
		return;
	}
	if (strlen(address) == 0 || strcmp(address,"\n")==0) {
		for (int i = 0; i < getRepo(service)->length - 1; i++) {
			for (int j = i + 1; j < getRepo(service)->length; j++) {
				if (((Estate*)getRepo(service)->elems[i])->price > ((Estate*)getRepo(service)->elems[j])->price) {
					Estate aux = *((Estate*)getRepo(service)->elems[i]);
					*((Estate*)getRepo(service)->elems[i]) = *((Estate*)getRepo(service)->elems[j]);
					*((Estate*)getRepo(service)->elems[j]) = aux;
				}
			}
		}
		*length = getRepo(service)->length;
		for (int i = 0; i < getRepo(service)->length; i++) {
			result[i] = *((Estate*)getRepo(service)->elems[i]);
		}
		return;
	}
	*length = 0;
	for (int i = 0; i < getRepo(service)->length; i++) {
		if (strstr(((Estate*)getRepo(service)->elems[i])->address, address) != NULL) {
			result[*length] = *((Estate*)getRepo(service)->elems[i]);
			(*length)++;
		}
	}
	for (int i = 0; i < *length - 1; i++) {
		for (int j = i + 1; j < *length; j++) {
			if (result[i].price > result[j].price) {
				Estate aux = result[i];
				result[i] = result[j];
				result[j] = aux;
			}
		}
	}
}

int filter_by_size(Service* service, Estate* result, int* length, char* type, int surface) {
	if (service == NULL) {
		return 0;
	}
	if (strlen(type) == 0 || surface <= 0) {
		return 0;
	}
	//check that the type is either house, apartment or penthouse with strcmp
	if (strcmp(type, "house") != 0 && strcmp(type, "apartment") != 0 && strcmp(type, "penthouse") != 0) {
		return 0;
	}
	*length = 0;
	for (int i = 0; i < getRepo(service)->length; i++) {
		if (strcmp(((Estate*)getRepo(service)->elems[i])->type, type) == 0 && ((Estate*)getRepo(service)->elems[i])->surface > surface) {
			result[*length] = *((Estate*)getRepo(service)->elems[i]);
			(*length)++;
		}
	}
	return 1;
}

Repo* getRepo(Service* service) {
	if (service == NULL) {
		return NULL;
	}
	return service->repo;
}