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
the program to be compiled is edited or modified by something called the *preprocessor*. commands intended for the preprocessor are called *directives*. Directives start with the `#` (hashtag symbol). By default there is no semicolon (;) symbol at the end of a directive because directives are usually one line long therefore there is no need for a special symbol at the end of the line in a directive.

in the `{c icon} structure_example.c` program just given the `{c} #include` directive states that the information in the `{c} stdio` *library* is to be included in the program before it is to be compiled.

C has a number of headers like `{c} <stdio.h>` each one contains information about some part of the *standard library*. `C` by default cannot input or output information, these functions are accomplished using the `{c} <stdio.h>` *library*

#### statements

a statement is a command or instruction to be executed when the program runs. `C` requires that each statement ends with a semicolon (;) so `C` knows where the statement ends.

### comments

```c title:comments.c
#include <stdio.h>
//this is a comment
int main(){
/*this is a comment that 
can be expanded over many lines
*/
    printf("hello world!");
return 0;
}

