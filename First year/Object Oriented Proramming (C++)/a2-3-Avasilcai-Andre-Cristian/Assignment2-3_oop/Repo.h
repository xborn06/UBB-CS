#pragma once
#include "Estate.h"

typedef void* TElem;

typedef struct {
	TElem* elems;
	int length;
	int capacity;
}Repo;

Repo* createRepo();
void resize(Repo* repo);
void destroyRepo(Repo* repo);
void addEstate(Repo* repo, Estate* estate);
void deleteEstate(Repo* repo, Estate* estate);
void updateEstate(Repo* repo, Estate* estate, char* original_address);