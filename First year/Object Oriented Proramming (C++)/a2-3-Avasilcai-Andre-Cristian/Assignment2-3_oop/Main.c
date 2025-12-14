#define _CRT_SECURE_NO_WARNINGS
#include "UI.h"
#include "Service.h"
#include "Repo.h"
#include "Estate.h"

int main() {
    Repo* repo = createRepo();
    Estate* estate1 = createEstate("house", "Kogalniceanu", 120, 250000);
    Estate* estate2 = createEstate("apartment", "Prieteniei", 80, 150000);
    Estate* estate3 = createEstate("penthouse", "Eroilor", 200, 500000);

    addEstate(repo, estate1);
    addEstate(repo, estate2);
    addEstate(repo, estate3);

    Service* service = createService(repo);
    UI* ui = createUI(service);

    run(ui);

    destroyUI(ui);
    destroyService(service);
    return 0;
}