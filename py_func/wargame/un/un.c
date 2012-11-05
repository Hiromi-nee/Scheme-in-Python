void do_nothing_lol();

int main() {
  printf("I print your nonsense! Enter nonsense:\n");
  char buffer[100];
  gets(buffer);
  printf("Your nonsense:\n%s\n", buffer);
}

void do_nothing_lol() {
  system("cat flag");
}
