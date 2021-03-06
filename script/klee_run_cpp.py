import sys
import os
from termcolor import colored
from subprocess import Popen, call, PIPE
import argparse


os.environ['LD_LIBRARY_PATH'] = '/home/klee/klee_build/klee/lib/:$LD_LIBRARY_PAT'
lib_path = '/home/klee/klee_build/klee/lib/'

parser = argparse.ArgumentParser()
parser.add_argument("-e", "--expected", type=int, help="Expected amount of results")
args = parser.parse_args()
print(colored('[+] Compiling ...', 'green'))

# os.system('sh /home/klee/ConcTrignr/klee/run_program.sh')
cmd = 'clang++ -Iinclude -L ' + lib_path + ' -Lbuild -o klee/a.out klee/a.c -lkleeRuntest -lpthread -lutils -lcrypto -lm'
p = Popen(cmd.split(' '))
rt_value = p.wait()
if rt_value != 0:
    exit(3)

running_res = set()
for file in os.listdir(os.path.join('klee', 'klee-last')):
    if file.endswith('.ktest'):
        # show = 'ktest-tool --write-ints klee/klee-last/%s' % file
        # os.system(show)
        cmd = 'KTEST_FILE=klee/klee-last/%s' % file
        res = os.system(cmd + ' klee/a.out') >> 8
        running_res.add(res)

tests = running_res
# print(tests)
# if args.expected is None:
#     standard = {0, 1}
# elif args.expected == 2:
#     standard = {0, 1}
# elif args.expected == 1:
#     standard = {0, }
# else:
#     exit(-1)

if 1 in tests:
    exit(1)
elif 139 in tests:
    exit(-1)
else:
    exit(0)
