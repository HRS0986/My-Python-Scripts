#! python 3.8
# Website Blocker Program
# By Hirusha Fernando

'''
```````````````````````````````````````````
`  ||||||  ||        ||||||   ||    ||    `
`  ||   || ||       ||    ||   ||  ||     `
`  ||||||  ||       ||    ||     ||       ` 
`  ||   || ||       ||    ||   ||  ||     `
`  ||||||  ||||||||  ||||||   ||    ||    `
`                                         `
```````````````````````````````````````````
'''

import os
import re


_URL_PATTERN = r'(.+?\s+)(.+)'


class Blocker():

    def __init__(self):
        self.__hostPath = ''
        self.__platform = os.name

        if self.__platform == "nt":
            self.__hostPath = r'C:\Windows\System32\drivers\etc\hosts'
        
        elif self.__platform == "posix":
            self.__hostPath = r'/etc/hosts'

        
    def block_site(self, url):
        # This function blocks URL

        _already = False
        with open(self.__hostPath, 'r+') as host:
            host_list = host.readlines()

            for line in host_list:
                if url in line:
                    print('\n[!] URL Already Blocked.\n')
                    _already = True
                    break

            if not _already:
                host.write(f'0.0.0.0    {url}\n')
                print('\n[!] URL Blocked.\n')


    def unblock(self, url):
        # This function unblocks URL

        with open(self.__hostPath, 'r') as host:
            host_content = host.readlines()
            
        with open(self.__hostPath, 'w') as host:
            _blocked = False
            for line in host_content:
                if not url in line: host.write(line)
                else: _blocked = True
              
            if not _blocked:
                raise UrlNotFoundError('URL cannot be found')     
            else:
                print('\n[!] URL Unblocked\n')


    def is_blocked(self, url) -> bool:
        # This function checks, if url is blocked

        __content = ''
        
        with open(self.__hostPath, 'r') as host:
            __content = host.read()

        if url in __content:
            return True
        
        return False


    def get_blocked(self) -> list:
        # This function return blocked URL list

        self.__urlRegex = re.compile(_URL_PATTERN)

        with open(self.__hostPath, 'r') as host:
            host_content = host.readlines()        

        for line in host_content:
            if line[0] != '#' and line[0] != '\n':
                tmp = self.__urlRegex.findall(line)[0][1]
                yield tmp


class UrlNotFoundError(Exception):
    def __init__(self, error):
        super(UrlNotFoundError, self).__init__(error)
        self.error_code = '02'