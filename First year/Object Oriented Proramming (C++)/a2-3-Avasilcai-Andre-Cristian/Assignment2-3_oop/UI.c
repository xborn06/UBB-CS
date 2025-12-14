#define _CRT_SECURE_NO_WARNINGS
#include "UI.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define MAX_LENGTH 100

UI* createUI(Service* service) {
	UI* ui = (UI*)malloc(sizeof(UI));
	if (ui == NULL) {
		return NULL;
	}
	ui->service = service;
	return ui;
}

void destroyUI(UI* ui) {
	if (ui == NULL) {
		return;
	}
	free(ui);
}

void print_menu() {
	printf("1. Add estate\n");
	printf("2. Delete estate\n");
	printf("3. Update estate\n");
	printf("4. Search by address\n");
	printf("5. Print estates\n");
	printf("6. Filter by size\n");
	printf("0. Exit\n");
}

void print_estates(Service* service) {
	Repo* repo = getRepo(service);
	for (int i = 0; i < repo->length; i++) {
		Estate* estate = (Estate*)repo->elems[i];
		printf("Type: %s, Address: %s, Surface: %d, Price: %d\n", estate->type, estate->address, estate->surface, estate->price);
	}
}

void run(UI* ui) {
	char user_input[100];
	int option = -1;
	while (option != 0) {
		print_menu();
		printf("Enter option: ");
		scanf("%s", &user_input);
		if (user_input[0] >= '0' && user_input[0] <= '9') {
			option = user_input[0] - '0';
		}
		else 
		{
			option = -1;
		}
		if (option == 1) {
			char type[50], address[50];
			int surface, price;
			printf("Enter type: ");
			scanf("%s", type);
			printf("Enter address: ");
			scanf("%s", address);
			printf("Enter surface: ");
			scanf("%d", &surface);
			printf("Enter price: ");
			scanf("%d", &price);
			if(addEstateService(ui->service, type, address, surface, price)==1)
				printf("Estate added successfully!\n");
			else
				printf("Invalid estate!\n");
		}
		else if (option == 2) {
			char address[50];
			printf("Enter address: ");
			scanf("%s", address);
			if(deleteEstateService(ui->service, address)==1)
				printf("Estate deleted successfully!\n");
			else
				printf("Estate not found!\n");
		}
		else if (option == 3) {
			char type[50], address[50], original_address[50];
			int surface, price;
			printf("Enter type: ");
			scanf("%s", type);
			printf("Enter address: ");
			scanf("%s", address);
			printf("Enter surface: ");
			scanf("%d", &surface);
			printf("Enter price: ");
			scanf("%d", &price);
			printf("Enter original address: ");
			scanf("%s", original_address);
			if (updateEstateService(ui->service, type, address, surface, price, original_address) == 1) {
				printf("Estate updated successfully!\n");
			}
			else {
				printf("Estate not found!\n");
			}
		}
		else if (option == 4) {
			char address[50];
			printf("Enter address: ");
			while (getchar() != '\n');
			fgets(address, sizeof(address), stdin);
			address[strcspn(address, "\n")] = 0;
			
			Estate result[100];
			int length = 0;
			search_by_address(ui->service, address, result, &length);
			for (int i = 0; i < length; i++) {
				printf("Type: %s, Address: %s, Surface: %d, Price: %d\n", result[i].type, result[i].address, result[i].surface, result[i].price);
			}
		}
		else if (option == 5) {
			print_estates(ui->service);
		}
		else if (option == 6) {
			char type[50];
			int surface;
			printf("Enter type: ");
			scanf("%s", type);
			printf("Enter surface: ");
			scanf("%d", &surface);
			//printf("%s,%d\n", type, surface);
			Estate result[100];
			int length = 0;
			int ok = filter_by_size(ui->service, result, &length, type, surface);
			if (ok==1)
				for (int i = 0; i < length; i++) {
					printf("Type: %s, Address: %s, Surface: %d, Price: %d\n", result[i].type, result[i].address, result[i].surface, result[i].price);
				}
			else
				printf("Invalid filters!\n");
		}
		else
			if (option != 0) {
				printf("Invalid option!\n");
			}
	}
}