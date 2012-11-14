int whos_the_dumbass(int gimme);
int feed_the_dumbass(unsigned int dumbass_id);


int main(int argc, char *argv[]) {
  unsigned int a_gimme;
  if (argc > 1) {
    a_gimme = whos_the_dumbass(atoi(argv[1]));
    if (feed_the_dumbass(a_gimme) == 1) {
      puts("You fed the dumbass!\n");
    }
  }
  else {
    puts("./deux <number of idiots>\n");
  }
  exit(0);
}

int whos_the_dumbass(int gimme) {
  return gimme * 1337;
}

int feed_the_dumbass(unsigned int dumbass_id) {
  unsigned int gimme;
  char dumbass_buffer[200];
  gimme = dumbass_id;
  gets(dumbass_buffer);
  if (gimme == dumbass_id) {
    printf("Feeding dumbass with %s!\n", dumbass_buffer);
    return 1;
  }
  else {
    puts("You didn't feed the dumbass!\n");
    exit(0);
  }
}

void foot_in_ass() {
  system("cat flag");
}
