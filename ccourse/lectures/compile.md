### how to compile a `c` file with `gcc`?

note: everything is written in the terminal

1. check if you have `gcc` installed in your system

```bash
gcc --version
```
2. install gcc if you dont have it installed.

```bash
sudo apt install build-essential
```
3. compile the file.

```bash
gcc -o name_of_the_executable name_of_the_file_to_compile.c
```
for example
```bash
gcc -o myProg ex1.c
```
4. execute the obtained compiled file.

```bash
./myProg
```
