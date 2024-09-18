### C general program structure
 a common program structure in C  in general looks like:

```c title:general.c
directives

int main(void){

    statements

}
```

a C program structure example: 

```c title:structure_example.c
#include <stdio.h>

int main(){
    printf("hello world!");
return 0;
}
```

#### directives
the program to be compiled is edited or modified by something called the *preprocessor*. commands intended for the preprocessor are called *directives*. Directives start with the `#` (hashtag symbol).

in the `{c icon} structure_example.c` program just given the `{c} #include` directive states that the information in the `{c} stdio` *library* is to be included in the program before it is to be compiled.

C has a number of headers like `{c} <stdio.h>`.......

