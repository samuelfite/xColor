import re

with open( "/home/sam/.YEET", "r" ) as fp:
    lines = fp.readlines()
    print( len(lines) )
    read = 0
    theme = list()
    name = ""
    o = "{{{"
    c = "}}}"
    print( o )
    print( c )
    for line in lines:
        if o in line:
            name = " ".join( re.split("[^a-zA-Z]*", line) )
            print( "NAME: " + name )
            read = 1
        if c in line:
            theme.append( line )
            read = 0
            with open( "themes/"+name, 'w' ) as wf:
                print( "OPENED NAME: " + name )
                for w in theme:
                    wf.write( w )
            theme.clear()
        if read:
            theme.append( line )

