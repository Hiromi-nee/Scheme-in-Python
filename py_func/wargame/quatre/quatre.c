int main() {
  char to_eval[200];
  puts("Let's calculate something:");
  gets(to_eval);
  do_stuff(to_eval);
}

do_stuff(char* stuff) {
  char form_eval[223];
  sprintf(form_eval, "python -c \'a=%s; print a\'", stuff);
  system(form_eval);
}
