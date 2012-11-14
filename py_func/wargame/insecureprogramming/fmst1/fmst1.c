int main(int argv,char **argc) {
  short int zero=0;
  int *plen=(int*)malloc(sizeof(int));
  char buf[256];

  strcpy(buf,argc[1]);
  printf("%s%hn\n",buf,plen);
  while(zero);
}
