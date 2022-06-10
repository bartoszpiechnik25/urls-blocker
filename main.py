import sys
from blocker import Blocker

if __name__ == '__main__':
    blocker = Blocker(sys.argv[1], sys.argv[2])
    if sys.argv[1] == 'write':
        blocker.add_blocked_urls(*sys.argv[2:])
        sys.exit(0)
    elif sys.argv[1] == 'block':
        blocker.block([int(sys.argv[3]), int(sys.argv[4])],
                      [int(sys.argv[5]), int(sys.argv[6])])
    elif sys.argv[1] == 'clear':
        blocker.clear_url_file()
    else:
        print('Wrong operation!')
        sys.exit(-1)
    