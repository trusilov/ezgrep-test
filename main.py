# -*- coding: utf-8 -*-
import re
'''
Enter 3 attributes. Example: "^some.*?thing example.txt 0"
1. Regular expression or word. "^some.*?thing"
2. File name and directory . "example.txt"
3. Exclusive search. 0 or 1.
'''

HELP = 'Enter 3 attributes. Example: "^some.*?thing example.txt 0"'
print(HELP)
print('SET:')
SET = list(map(str, input().split()))

try:
    PATTERN = SET[0]
    DIRECTORY = SET[1]
    REVERS = SET[2]
except IndexError:
    print('Please, set only 3 attribute.')
except FileNotFoundError:
    print('Please, enter correctly file directory or name.')


class Grep(object):
    def __init__(self):
        self.directory = DIRECTORY
        self.pattern = PATTERN
        self.revers = REVERS

    def set_data(self):
        handle = open(self.directory, 'r')
        text = handle.read()
        handle.close()
        self.data_list = re.split('\n', text)
        return self.data_list

    def search(self):
        if self.revers == '0':
            for el in self.data_list:
                pattern = re.compile(self.pattern)
                match = pattern.findall(el)
                if match:
                    print(el)
        elif self.revers == '1':
            for el in self.data_list:
                pattern = re.compile(self.pattern)
                match = pattern.findall(el)
                if not match:
                    print(el)
        else:
            print('Attribute REVERS Not Found')


if __name__ == '__main__':
    obj = Grep()
    obj.set_data()
    obj.search()
