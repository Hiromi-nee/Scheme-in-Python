// Run on server with socat TCP-LISTEN:9999,fork EXEC:./manhattan

#include <stdio.h>
#include <stdlib.h>

int gen_num(int seed);

int main(int argc, char **argv) {
  printf("Welcome\n");
  srand(time(NULL) >> 3);
  int ran = gen_num(rand());
  
  printf("%d", ran);
}

int gen_num(int seed) {
  int res = (0x1337 ^ 0x42) ^ seed;
  return res;
}

