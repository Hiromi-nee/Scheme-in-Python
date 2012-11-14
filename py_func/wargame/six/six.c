#include <stdio.h>
#include <stdlib.h>

char* read_file(char *file_name);

int main() {
  char *flag_stuff = read_file("flag");
  dark_side(flag_stuff);

  // We totally need to free memory. No way!
  free(flag_stuff);
}

void dark_side(char *stuff) {
  char album_name[200];
  // excuse me while I take a strange interlude
  printf("I've forgotten which Pink Floyd album had a prism on it. Remind me?\n");
  fgets(album_name, 200, stdin);
  printf("Thanks! Didn't think of that album. Sounds real good on the tongue:\n");
  printf(album_name); // I forgot how to concatenate :/
}

char *read_file(char *file_name) {
  FILE *f = fopen(file_name, "rb");
  fseek(f, 0, SEEK_END);
  long pos = ftell(f);
  fseek(f, 0, SEEK_SET);

  char *bytes = malloc(pos);
  fread(bytes, pos, 1, f);
  fclose(f);

  return bytes;
}
