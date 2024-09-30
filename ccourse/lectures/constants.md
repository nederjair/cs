When a program contains constants is a good idea to give them names. The meaning of a nameless constant is often not clear to the person who is reading a program. Using a feature known as **macro definition** we can name a constant.
```c title:"macro definition"
#define CONSTANTNAME CONSTANTVALUE
```
**usually constants are written in uppercase however this is not mandatory.**
**if a constant value is an expression it is required to be written between parenthesis**

`{c} #define` is a directive just as `{c} #include` is that's why there is no need of a `;` at the end of the line.

### example
lets examine an example where the formulas of the free fall are used.
```c title:freefall.c
#include <stdio.h>
#define G 9.8f
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
```
here the gravitational constant $g = 9.8$ is used for the calculations and it conveys the idea of a physic's constant. When the program is compiled the preprocessor replaces each macro by the value that it represents for example the two lines where G is used transform internally in:

```c
    printf("vf=%f\n", v0 + 9.8*t);
    printf("y=%f\n", y0 + v0*t - 0.5*9.8*t*t);
```
