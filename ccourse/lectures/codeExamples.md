```c title:printf.c
#include <stdio.h>

int main() {
    int i, j;
    float x, y;
    i =10;
    j = 20;
    x = 43.2f;
    y = 5527.0f;

    printf("i = %d, j = %d, x = %d, y = %d\n", i);
    printf("i = %d\n", i, j, x, y);
    printf("i = %d, j = %d, x = %d, y = %d\n", i, j, x, y);

    printf("i = %d, j = %d, x = %f, y = %f\n", i, j, x, y);
    return 0;
}
```

```c title:printf.c
#include <stdio.h>

int main() {
    int i, j;
    float k;
    i =123456789;
    j = 5;
    k = 0.53f;
    printf("%8.2d\n", i);
    printf("%8.2d\n", j);
    printf("%8.2f\n", k);
    return 0;
}
```

```c title:printf.c
#include <stdio.h>

int main() {
    int i, j;
    float k;
    i =1234567891;
    j = 5;
    k = 0.53f;
    printf("%7.2d\n", i);
    printf("%7.2d\n", j);
    printf("%7.2f\n", k);
    printf("%7.1e\n", k);
    return 0;
}
```

```c title:remainder.c
#include <stdio.h>

int main() {
    int i, j;
    float x, y;
    scanf("%d%d%f%f", &i, &j, &x, &y);
    printf("i=%d\n", i);
    printf("j=%d\n", j);
    printf("x=%f\n", x);
    printf("y=%f\n", y);
    return 0;
}
```

```c title:remainder.c
#include <stdio.h>

int main() {
    printf("9/7 remainder = %d\n", 9%7);
    printf("-9/7 remainder = %d\n", -9%7);
    return 0;
}
```
