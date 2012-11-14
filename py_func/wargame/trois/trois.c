// Compiled with gcc -m32 -mpreferred-stack-boundary=2 -fno-stack-protector -o trois trois.c

#include <stdio.h>
#include <string.h>

void light(int count);
void omg_the_fuzz();
void token(char* stuff, int count);

int main(int argc, char* argv[]) {
  if (argc > 1) {
    int count = atoi(argv[1]);
    light(count);
  }
  else {
    puts("./trois <no. of bytes to read>\n");
  }
}

void light(int count) {
  unsigned int brownies = 0xdeadbeef;
  unsigned int hash = 0xBBBBBBBB;
  char avitas_grass[30];
  puts("What sort of brownies do you want: ");
  fgets(avitas_grass, 30, stdin);
  puts("Taking a token...\n");
  token(avitas_grass, count);
  if (brownies == 0x42424242 && hash == 0xdeadcafe) {
    omg_the_fuzz();
  }
  else {
    puts("It was great success.\n");
    printf("The two stuff in the stash, %x and %x were so freaky.\n", brownies, hash);
  }
}

void token(char* stuff, int count) {
  char candy[24];
  printf("The stash is located at %9$x.\n");
  if (count <= 25) {
    memcpy(candy, stuff, count);
  }
}

void omg_the_fuzz() {
  puts("We've been set us up the bomb!\n");
  system("cat flag");
}
