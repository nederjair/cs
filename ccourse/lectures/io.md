#### writing output

printing the value of a variable is as simple as:

```c title:printValueOfAVariable.c
#include <stdio.h>
int main(){
    int radius = 10;
    printf("radius: %d\n", radius);
}
```
the f in printf stands for *formatted* it means that both printf and scanf require the use of a format string to specify the appearence and type of input and output data. scanf needs to know what form the input data will take (type) and printf needs to know how to display the output data.

#### reading input
to read an `{c} int` variable we use `{c} scanf("%d", &i)` :
- `{c} "%d"` tells scanf to read input that represents an integer.
- `{c} &i` tells scanf to store the obtained input in a variable named `{c} i` of `{c} int` type.


to read a `{c} float` variable we use `{c} scanf("%f", &x)` :
- `{c} "%f"` tells scanf to read input that represents an float.
- `{c} &x` tells scanf to store the obtained input in a variable named `{c} x` of `{c} float` type.


