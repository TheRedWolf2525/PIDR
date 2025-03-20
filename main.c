#include <stdio.h>
#include <math.h>
#include <unistd.h>

#define DEPL_LAT 3
#define NB_LEDS 7

#define PI 3.14159265358979323846264338327950288

void affichageRuban(double leds[]){
    for (int i = 0; i < NB_LEDS; i++){
        printf("%f ", leds[i]);
    }
    printf("\n");
}

int main(){
    // Liste des leds
    // Pourcentage d'intensité
    double leds[NB_LEDS] = {};
    double pc = 0;

    while (1){
        pc = fmod(pc+0.1, 2*PI);
        leds[0] = sin(pc);
        printf("pc = %f; sin(pc) = %f\n", pc, leds[0]);
        usleep(600000);
    }
    affichageRuban(leds);
    return 0;
}
