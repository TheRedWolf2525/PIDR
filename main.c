#include <stdio.h>
#include <math.h>
#include <unistd.h>

#define DEPL_LAT 3
#define NB_LEDS 7
#define SPEED 30000

#define PI 3.14159265358979323846264338327950288

void affichageRuban(int leds[]){
    for (int i = 0; i < NB_LEDS; i++){
        if (leds[i]){
            printf("#");
        }else{
            printf(".");
        }
    }
    printf("\n");
}

int main(){
    // Liste des leds
    // Pourcentage d'intensité
    int leds[NB_LEDS] = {};
    double pc = 0;

    while (1){
        int leds[NB_LEDS] = {};
        pc = fmod(pc+0.1, 2*PI);
        leds[(int)fmod((int) ((DEPL_LAT+0.5)*(sin(pc)+1)), NB_LEDS)] = 1;
        affichageRuban(leds);
        usleep(SPEED);
    }
    affichageRuban(leds);
    return 0;
}
