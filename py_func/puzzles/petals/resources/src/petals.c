#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#define CORRECT_THRESHOLD 1000

#define A(c)            (c) - 0x19
#define UNHIDE_STR(str) do { char *p = str;  while (*p) *p++ += 0x19; } while (0)
#define HIDE_STR(str)   do { char *p = str;  while (*p) *p++ -= 0x19; } while (0)

void populate_dice(int dice_array[]);
int check_answer(int dice_array[]);
void print_dice(int roll_number, int dice_array[]);

int main (int argc, char **argv)
{
  /* introduction */
  printf("\n\n                   Petals Around a Rose\n");
  printf("                        xCTF Style\n");
  printf("                          by amon\n\n");
  printf("Rules:\n");
  printf("  1. The name of the game is \"Petals Around the Rose\",\n");
  printf("     and the name of the game is the key to the secret rule.\n");
  printf("  2. The answer is always zero or an even number.\n");
  printf("  3. Anyone who knows the game may give the answer to any roll,\n");
  printf("     but they must not disclose the reasoning.\n\n");
  printf("To obtain the flag for this problem, you must supply the correct\n");
  printf("answer a thousand times.\n\n");
  printf("Are you ready to start?\n");
  printf("                                             It begins.\n\n");

  /* initialize random generator */
  srand(time(NULL));

  /* declare the program variables */
  int times_correct = 0;
  int current_dice_array[6];
  int current_dice_answer;
  int user_answer;

  /* begin the game */
  while (times_correct < CORRECT_THRESHOLD)
    {
      populate_dice(current_dice_array);
      current_dice_answer = check_answer(current_dice_array);
      print_dice(times_correct, current_dice_array);
      printf("\nYour answer: ");
      scanf("%d", &user_answer);
      if (user_answer == current_dice_answer)
	{
	  times_correct++;
	  if ((times_correct != CORRECT_THRESHOLD))
	    {
	      printf("\nYes, that answer was correct! On to the next one!\n\n");
	    }
	}
      else
	{
	  break;
	}
    }

  if (times_correct < CORRECT_THRESHOLD) {
    printf("\nI'm sorry that answer was wrong. The correct answer was %d.\n", current_dice_answer);
    printf("You need %d more correct answers to get the flag.\n\n", CORRECT_THRESHOLD - times_correct);
  }
  else {
    char flag[] = {
      A('T'), A('h'), A('e'), A(' '), A('P'), A('o'), A('w'), A('e'), A('r'), A(' '),
      A('o'), A('f'), A(' '), A('T'), A('h'), A('r'), A('e'), A('e'), A(' '), A('W'),
      A('i'), A('l'), A('l'), A(' '), A('S'), A('e'), A('t'), A(' '), A('U'), A('s'),
      A(' '), A('F'), A('r'), A('e'), A('e'), 0
    };
    UNHIDE_STR(flag);
    printf("Very good! Here is your flag: \'%s'.\n\n", flag);
    HIDE_STR(flag);
  }

  return 0;
}

void populate_dice(int dice_array[])
{
  int i = 0;
  for (i = 0; i < 6; i++) 
    {
      dice_array[i] = (rand() % 6) + 1;
    }
  return;
}

int check_answer(int dice_array[])
{
  int i = 0;
  int count = 0;
  for (i = 0; i < 6; i++)
    {
      if (dice_array[i] == 3) 
	{
	  count += 2;
	}
      else if (dice_array[i] == 5)
	{
	  count += 4;
	}
    }
  return count;
}

/*
  Roll Number 1

    ,.....,    ,.....,    ,.....,    ,.....,    ,.....,    ,....., 
    |o   o|    |o   o|    |o   o|    |o   o|    |o   o|    |o   o|
    |o   o|    |o   o|    |o   o|    |o   o|    |o   o|    |o   o|
    |o   o|    |o   o|    |o   o|    |o   o|    |o   o|    |o   o|
    ```````    ```````    ```````    ```````    ```````    ```````
       6          6          6          6          6          6
*/
void print_dice(int roll_number, int dice_array[])
{
  /* print the roll number. */
  printf("Roll Number %d\n\n", roll_number);
  
  /* print dice tops */
  printf("    ,.....,    ,.....,    ,.....,    ,.....,    ,.....,    ,.....,\n");

  /* build the first dot layer. */
  int i;
  for (i = 0; i < 6; i++) 
    {
      if (dice_array[i] == 1)
	{
	  printf("    |     |");
	}
      else if (dice_array[i] == 2)
	{
	  printf("    |    o|");
	}
      else if (dice_array[i] == 3)
	{
	  printf("    |    o|");
	}
      else if (dice_array[i] == 4)
	{
	  printf("    |o   o|");
	}
      else if (dice_array[i] == 5)
	{
	  printf("    |o   o|");
	}
      else if (dice_array[i] == 6)
	{
	  printf("    |o   o|");
	}
    }
  printf("\n");

  /* build the second dot layer. */
  for (i = 0; i < 6; i++) 
    {
      if (dice_array[i] == 1)
	{
	  printf("    |  o  |");
	}
      else if (dice_array[i] == 2)
	{
	  printf("    |     |");
	}
      else if (dice_array[i] == 3)
	{
	  printf("    |  o  |");
	}
      else if (dice_array[i] == 4)
	{
	  printf("    |     |");
	}
      else if (dice_array[i] == 5)
	{
	  printf("    |  o  |");
	}
      else if (dice_array[i] == 6)
	{
	  printf("    |o   o|");
	}
    }
  printf("\n");

  /* build the third dot layer. */
  for (i = 0; i < 6; i++) 
    {
      if (dice_array[i] == 1)
	{
	  printf("    |     |");
	}
      else if (dice_array[i] == 2)
	{
	  printf("    |o    |");
	}
      else if (dice_array[i] == 3)
	{
	  printf("    |o    |");
	}
      else if (dice_array[i] == 4)
	{
	  printf("    |o   o|");
	}
      else if (dice_array[i] == 5)
	{
	  printf("    |o   o|");
	}
      else if (dice_array[i] == 6)
	{
	  printf("    |o   o|");
	}
    }
  printf("\n");

  /* print the dice bottom */
  printf("    ```````    ```````    ```````    ```````    ```````    ```````\n");

  /* print the dice numbers */
  printf("       %d          %d          %d          %d          %d          %d\n",
	 dice_array[0], dice_array[1], dice_array[2], dice_array[3], dice_array[4],
	 dice_array[5]);

  return;
}
