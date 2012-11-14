#!/usr/bin/python

def main():
    replace = [('i', '1'),
               ('a', '4'),
               (' ', '_'),
               ('e', '3'),
               ('o', '0'),
               ('s', '5'),]
    flag = raw_input()
    flag = flag.lower()
    for i in replace:
        flag = flag.replace(i[0], i[1])
    print flag

if __name__ == "__main__":
    main()
