#define _CRT_SECURE_NO_WARNINGS
#include "Estate.h"
#include <string.h>
#include <stdlib.h>


Estate* createEstate(char* type, char* address, int surface, int price) {
	Estate* estate = (Estate*)malloc(sizeof(Estate));
	if (estate == NULL) {
		return NULL;
	}
	estate->type = (char*)malloc(strlen(type) + 1);
	strcpy(estate->type, type);
	estate->address = (char*)malloc(strlen(address) + 1);
	strcpy(estate->address, address);
	estate->surface = surface;
	estate->price = price;
	return estate;
}

void destroyEstate(Estate* estate) {
	if (estate == NULL) {
		return;
	}
	free(estate->type);
	free(estate->address);
	free(estate);
}