spaces = 75*" "

d = 'digraph G {\n'
d += '  subgraph cluster { margin="0.0" penwidth="0.0"\n'
d += '    tbl [shape=none fontname="Arial" label=<\n'
d += '        <table border="1" cellborder="0" cellspacing="0">\n'
d += '        <tr><td bgcolor="teal" align="left"><font color="white">users.txt'+75*" "+'</font></td></tr>\n'
d += '        <tr><td bgcolor="white" align="left">Primera linea</td></tr>\n'
d += '        <tr><td bgcolor="white" align="left">Sengunda linea</td></tr>\n'
d += '        <tr><td bgcolor="white" align="left"> </td></tr>\n'
d += '        <tr><td bgcolor="white" align="left"> </td></tr>\n'
d += '        <tr><td bgcolor="white" align="left"> </td></tr>\n'
d += '        <tr><td bgcolor="white" align="left"> </td></tr>\n'
d += '        <tr><td bgcolor="white" align="left"> </td></tr>\n'
d += '        </table>\n'
d += '    >];\n'
d += '  }\n'
d += '}'

print(d)