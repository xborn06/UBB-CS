#define _CRT_SECURE_NO_WARNINGS
#include "Repo.h"
#include <stdlib.h>
#include <string.h>

Repo* createRepo() {
	Repo* repo = (Repo*)malloc(sizeof(Repo));
	if (repo == NULL) {
		return NULL;
	}
	repo->length = 0;
	repo->capacity = 1;
	repo->elems = (TElem*)malloc(sizeof(TElem) * repo->capacity);
	if (repo->elems == NULL) {
		return NULL;
	}
	return repo;
}

void resize(Repo* repo) {
	repo->capacity *= 2;
	TElem* new_elems = (TElem*)malloc(sizeof(TElem) * repo->capacity);
	if (new_elems == NULL) {
		return;
	}
	for (int i = 0; i < repo->length; i++) {
		new_elems[i] = repo->elems[i];
	}
	free(repo->elems);
	repo->elems = new_elems;
}

void destroyRepo(Repo* repo) {
	if (repo == NULL) {
		return;
	}
	for (int i = 0; i < repo->length; i++) {
		destroyEstate((Estate*)repo->elems[i]);
	}
	free(repo->elems);
	free(repo);
}

void addEstate(Repo* repo, Estate* estate) {
	if (repo == NULL || estate == NULL) {
		return;
	}
	if (repo->length == repo->capacity) {
		resize(repo);
	}
	repo->elems[repo->length] = estate;
	repo->length++;
}

void deleteEstate(Repo* repo, Estate* estate) {
	if (repo == NULL || estate == NULL) {
		return;
	}
	int index = -1;
	for (int i = 0; i < repo->length; i++) {
		if (strcmp(((Estate*)repo->elems[i])->address, estate->address) == 0) {
			index = i;
			break;
		}
	}
	if (index == -1) {
		return;
	}
	destroyEstate((Estate*)repo->elems[index]);
	for (int i = index; i < repo->length - 1; i++) {
		repo->elems[i] = repo->elems[i + 1];
	}
	repo->length--;
}

void updateEstate(Repo* repo, Estate* estate, char* original_address) {
	if (repo == NULL || estate == NULL) {
		return;
	}
	int index = -1;
	for (int i = 0; i < repo->length; i++) {
		if (strcmp(((Estate*)repo->elems[i])->address, original_address) == 0) {
			index = i;
			break;
		}
	}
	if (index == -1) {
		return;
	}
	destroyEstate((Estate*)repo->elems[index]);
	repo->elems[index] = estate;
}
