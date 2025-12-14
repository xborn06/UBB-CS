#pragma once
#include "Service.h"

typedef struct {
	Service* service;
}UI;

UI* createUI(Service* service);
void destroyUI(UI* ui);
void run(UI* ui);
void print_menu();
void print_estates(Service* service);