// compiled with gcc -m32 -fno-stack-protector -mpreferred-stack-boundary=2 -o sept sept.c

void generate_stack(void (*cb) (int));
void squeezebox_cb();
int get_stack();

int main() {
  srand(time(0)); // only seed the time once
  generate_stack(&squeezebox_cb);
}

void generate_stack(void (*cb)()) {
  int size = rand() % 256; // 0 to 255
  char *lol_aslr = alloca(size);
  cb();
}

void squeezebox_cb () {
  // yeah we're using callbacks now.
  puts("\n\"Mama's got a squeeze box\nDaddy never sleeps at night\"\n\nWhat song?");
  char music[400];
  gets(music);
  puts("I have no idea if that's the right answer or not.");
}
