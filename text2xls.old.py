#!/usr/bin/env python
# -*- coding: utf-8 -*-
def count_spaces(s):
    i = 0
    for c in s:
        if c == " ":
            i += 1
        else:
            return i

i = 10
lastlevel = 0
lastheader = ""
close_stack = []
close_stack.append(str(1))
xml = ""
dot="digraph G {\n"
dotml = '<graph	file-name="graphs/nice_graph" rankdir="LR">'
lastline = " +"
file = open("tree.txt", "r") 
for lineRaw in file:
    
    line = lineRaw.lstrip(' ').rstrip()
    level = count_spaces(lineRaw)

    if level == lastlevel:
        xml += "<p name=\""+lastline.split(" +")[0]+"\" weight=\"1\" order=\""+ lastline.split(" +")[1] + "\"/>\n"
        dotml += "<node id=\""+ str(i) +"\" label=\""+ lastline.split(" +")[0] +"\" />\n"
        dotml += "<edge from=\"" + close_stack[-1] + "\" to=\""+ str(i) + "\"/>\n"
        dot += close_stack[-1] + " -> " + str(i) + "\n"
    elif level > lastlevel:
        xml += "<p name=\""+lastline.split(" +")[0]+"\" weight=\"1\" order=\""+ lastline.split(" +")[1] + "\">\n"
        dotml += "<node id=\""+ str(i) +"\" label=\""+ lastline.split(" +")[0] +"\" />\n"
        dotml += "<edge from=\"" + close_stack[-1] + "\" to=\""+ str(i) + "\"/>\n"
        dot += close_stack[-1] + " -> " + str(i) + "\n"
        close_stack.append(str(i))
    else:
        xml += "<p name=\""+lastline.split(" +")[0]+"\" weight=\"1\" order=\""+ lastline.split(" +")[1] + "\"/>\n"
        dotml += "<node id=\""+ str(i) +"\" label=\""+ lastline.split(" +")[0] +"\" />\n"
        dotml += "<edge from=\"" + close_stack[-1] + "\" to=\""+str(i) + "\"/>\n"
        dot += close_stack[-1] + " -> " + str(i) + "\n"
        for a in range(0,(lastlevel-level)/2):
            xml += "</p>\n"
            close_stack.pop()
    dot += str(i) + "[shape=box label=\""+ line.split(" +")[0] +"\"]\n"
    lastlevel = level
    lastline = line
    i+=1
    #print close_stack

for a in range(1,len(close_stack)):
    xml += "</p>\n"
dotml += "</graph>"
dot += "\n}"

file2 = open("out.xml","w")
file2.write(xml)
file2.close

file3 = open("dot.xml","w")
file3.write(dotml)
file3.close

file4 = open("dot.gv","w")
file4.write(dot)
file4.close