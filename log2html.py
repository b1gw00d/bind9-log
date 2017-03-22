# python 3

import os
import sys
import jinja2

try:
    log_file = str(sys.argv[1])
    html_file = str(sys.argv[2])

except IndexError:
    print ("")
    print ("usage: python3 log2html.py [query log file] [output html file]")
    print ("")
    sys.exit(0)

open_file = open(log_file, "r")

query_values = []

for line in open_file.readlines():
    t =  line.split(" ")[0], \
            line.split(" ")[1], \
            line.split(" ")[3], \
            line.split(" ")[6], \
            line.split(" ")[8]
    query_values.append(t)

open_file.close()

# jinja2 environment
loader = jinja2.FileSystemLoader(os.getcwd())
jenv = jinja2.Environment(loader=loader)
define_template = jenv.get_template("templates/template.html")

jinja_file = define_template.render(list=query_values)

w = open(html_file, "w")
w.write(jinja_file)
w.close()