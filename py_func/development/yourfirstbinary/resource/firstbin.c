#include <stdio.h>

int main(int argc, char *argv[])
{
  if (argc != 2)
    {
      printf("Please call the program like thus: ./firstbin <guess>\n");
      return 0;
    }
  int password = 0;
  password = atoi(argv[1]);
  if (password == 3133742)
    {
      printf("Correct! Here is your answer: take the password and multiply it by 42, add 42, then mod it by 1337, then bring it to the 3rd exponent.\n");
    }
  else
    {
      printf("Incorrect! Try again!\n");
    }
  return 0;
}
