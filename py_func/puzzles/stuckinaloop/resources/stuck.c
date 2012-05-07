#include <stdio.h>

#define A(c)            (c) - 0x19
#define UNHIDE_STR(str) do { char *p = str;  while (*p) *p++ += 0x19; } while (0)
#define HIDE_STR(str)   do { char *p = str;  while (*p) *p++ -= 0x19; } while (0)


void printGalf()
{
  char galf[] = 
    {
      A('W'), A('o'), A('u'), A('l'), A('d'), A('Y'), A('o'), A('u'), A('L'), A('i'), A('k'),
      A('e'), A('G'), A('r'), A('e'), A('e'), A('n'), A('E'), A('g'), A('g'), A('s'), A('A'),
      A('n'), A('d'), A('S'), A('p'), A('a'), A('m'), A('?'), 0
    };

  UNHIDE_STR(galf);
  printf("Yes, you did it! The flag is %s\n", galf);
}

int main()
{
  int good = 0, bad = 0;

  while (!good) 
    {
      if (bad <= 99999999999)
	{      
	  printf("Sorry for the spam.\n");
	  fflush(stdout);
	  sleep(1);
	}
      else
	{
	  good = 1;
	}
      bad++;
    }
  printGalf();
  return 0;
}


