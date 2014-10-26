'''
Created on Oct 7, 2014

@author: dlui
'''

import sys
import ping


if __name__ == '__main__':
    blah = [123,456,"abc"]
    print blah
    print 'Hello World'
    blah.append("999")
    for i in blah:
        print i
    mystr = "hello world"
    blah.reverse()
    print blah
    print mystr.split()
    print sys.api_version
    print sys.path
    print sys.builtin_module_names
    print sys.platform
    
    ping.verbose_ping('www.google.com', count=3)