int get_stack() {
  __asm__("mov %esp, %eax");
}

int main() {
  printf("The address of the stack is: %x.\n", get_stack());
}
