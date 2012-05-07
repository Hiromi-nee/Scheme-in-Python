import pexpect
import re

r = re.compile(r"(\d)          (\d)          (\d)          (\d)          (\d)          (\d)")
answer = 0

child = pexpect.spawn("./x86/petals.elf32")

while True:
    read = child.read_nonblocking(10000)
    match = r.search(read)
    if match:
        answer = 0
        d = [int(i) for i in match.groups()]
        for i in d:
            if i == 3:
                answer += 2
            elif i == 5:
                answer += 4
        child.sendline("%d" % answer);
    print read
c.close()


