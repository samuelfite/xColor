import sys,os
from pprint import pprint
import re
from subprocess import check_output

DIR_PATH="/home/sam/builds/xColor/"

newtheme = check_output( [DIR_PATH+"get_theme.sh"] ).decode( "utf-8" )
print( "NEWTHEME: " + newtheme)

THEME_PATH=DIR_PATH+"themes/"
NEW_THEME_PATH=THEME_PATH+newtheme.strip('\n')

FILE_PATH="/home/sam/.Xresources"

lines = list()
with open( FILE_PATH, 'r' ) as fp:
    lines = fp.readlines()
    print( len(lines) )
    read = 0
    theme = list()
    name = ""
    o = "{{{"
    c = "}}}"
    for line in lines:
        if o in line:
            name = " ".join( re.split("[^a-zA-Z]*", line) )
            print( "NAME: " + name )
            read = 1
        if c in line:
            theme.append( line )
            read = 0
            with open( THEME_PATH+name, 'w' ) as wf:
                print( "OPENED NAME: " + name )
                for w in theme:
                    wf.write( w )
            #remove theme from array
            lines = [ x for x in lines if x not in theme ]
            theme.clear()
        if read:
            theme.append( line )

with open( NEW_THEME_PATH, 'r' ) as rp:
    theme = rp.readlines()

for i in theme:
    lines.append( i )

with open( FILE_PATH, 'w' ) as wp:
    for line in lines:
        wp.write( line )

print( "RELOADING xrdb" )
out = check_output( ["/home/sam/.scripts/xresources.sh"] ).decode( "utf-8" )
print( "OUT: "+ out )
