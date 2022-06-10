import sys
from blocker import Mode

if __name__ == '__main__':
    blocker = Mode(sys.argv[1], 'windows')
    if sys.argv[1] == 'write':
        blocker = Mode(sys.argv[1], 'windows')
        blocker.add_blocked_urls(*sys.argv[2:])
        sys.exit(0)
    elif sys.argv[1] == 'block':
        blocker.block([int(sys.argv[2]), int(sys.argv[3])],
                      [int(sys.argv[4]), int(sys.argv[5])])
    else:
        print('Wrong operation!')
        sys.exit(-1)
    