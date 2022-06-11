import time
from datetime import datetime as dt
import sys


class Blocker:

    def __init__(self, mode: str, default: str) -> None:
        self.__mode = mode
        self.__linux_path = '/etc/hosts'
        self.__windows_path = r'C:\Windows\System32\drivers\etc\hosts'
        self.__macos = '/private/etc/hosts'
        self.__default = ''
        if default.lower() == 'windows':
            self.__default = self.__windows_path
        elif default.lower() == 'macos':
            self.__default = self.__macos
        else:
            self.__default = self.__linux_path
        self.__blockedlist = open('websites_urls.txt', 'r+').readlines()
        self.__local_host = '127.0.0.1'
    
    def add_blocked_urls(self, *args) -> None:
        """
        This function add specified urls from sys.argv[2:] to file containing
        those blocked urls used for blocking.
        """
        if self.__mode == 'write':
            file = open('websites_urls.txt', 'a+')
            for url in args:
                if url + '\n' not in self.__blockedlist:
                    file.write(url + '\n')
            file.close()

    def __save_original(self) -> None:
        """
        This function save original hosts file to load it in the end of program
        excecution.
        """
        f = open(self.__default, 'r')
        original_file = f.readlines()
        with open('original.txt', 'w+') as file:
            file.writelines(original_file)
        f.close()

    def __create_blocked(self) -> None:
        """
        This fuction create hosts file with blocked urls.
        """
        with open(self.__default, 'a+') as file:
            hosts = file.readlines()
            for url in self.__blockedlist:
                if self.__local_host + ' ' + url+'\n' not in hosts:
                    file.write(self.__local_host + ' ' + url)
    
    def __reset_hosts(self) -> None:
        """
        This function reset hosts file.
        """
        origin = open('original.txt', 'r+').readlines()
        with open(self.__default, 'w+') as file:
            file.writelines(origin)


    def block(self, start_time, end_time) -> None:
        """
        This function is blocking urls from start_time = [17, 34] is equivalent
        to 17:34 current day, end_time = [18, 54] is equivalent to 18:54.
        """
        start = dt(
                    dt.now().year,
                    dt.now().month,
                    dt.now().day,
                    start_time[0],
                    start_time[1])
        
        finish = dt(
                    dt.now().year,
                    dt.now().month,
                    dt.now().day,
                    end_time[0],
                    end_time[1])
        
        self.__save_original()

        try:
            self.__create_blocked()
            if start < dt.now() < finish:
                print('Websites: \n' + 
                ''.join(self.__blockedlist) + 'Blocked' + 
                f' from {start} to {finish}')
                print('Focus time....')
            while True:
                if not (start < dt.now() < finish):
                    self.__reset_hosts()
                    print('Free time')
                    break
                time.sleep(60)
        except KeyboardInterrupt:
            self.__reset_hosts()
        finally:
            print("Finishing execution")
            sys.exit(0)
    
    def clear_url_file(self) -> None:
        with open('websites_urls.txt', 'r+') as file:
            file.truncate(0)

    

if __name__ == '__main__':
    # path =  r'C:\Windows\System32\drivers\etc\hosts'
    # with open(path, 'r') as file:
    #     new = file.readlines()
    #     print(*new)
    test = Blocker('block', 'windows')
    test.reset_hosts()

