#include <stdio.h>
#define G 9.8
int main() {
    float t, v0, y0;
    printf("enter the time: ");
    scanf("%f", &t);
    printf("enter the initial velocity: ");
    scanf("%f", &v0);
    printf("enter the initial height: ");
    scanf("%f", &y0);
    printf("vf=%f\n", v0 + G*t);
    printf("y=%f\n", y0 + v0*t - 0.5*G*t*t);

    return 0;
}

