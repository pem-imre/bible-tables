#!/usr/bin/env python
# -*- coding: utf-8 -*- N9ssYjmSWgfcdN5S
def count_spaces(s):
    i = 0
    for c in s:
        if c == " ":
            i += 1
        else:
            return i

def count_children(lines):
    #Count all lines higher level until a lower level come
    level = count_spaces(lines[0])
    i = 1
    for line in lines[1:]:
        actual_level = count_spaces(line)
        if actual_level == level:
            return i
        if actual_level > level:
            i += 1
        else:
            return i
    return 1


i = 10
lastlevel = 0
lastheader = ""
close_stack = []
close_stack.append(str(1))
dot="digraph G {\nlayout=neato\nnode [shape=plaintext]\n"
edges ="Source,Target,Label,Weight\n"
nodes="Id,Label,cOrder\n"
lastline = " +"
text_file = open("tree.txt", "r")
data = text_file.readlines()
lineCount = 0
penwidth = 0.0
edgeId = 1
for lineRaw in data[0:-1]:
    childNum = count_children(data[lineCount:])
    penWidth = 1.0 + (float(childNum) / float(len(data))) * 30.0
    line = lineRaw.lstrip(' ').rstrip()
    level = count_spaces(lineRaw)

    dot += str(i) + " [label=\""+ line.split("|")[0] + "\"]\n"
    nodes += str(i) +","+ line.split("|")[0] +","+ line.split("|")[1] + "\n"

    if level == lastlevel:
        dot += close_stack[-1] + " -> " + str(i) + " [penwidth="+ str(penWidth) +" arrowhead=none]\n"
        edges += close_stack[-1] +","+ str(i) +","+ line.split("|")[2] +"," + str(childNum) + "\n"
        edgeId += 1
    elif level > lastlevel:
        close_stack.append(str(i-1))
        dot += close_stack[-1] + " -> " + str(i) + " [penwidth="+ str(penWidth) +" arrowhead=none]\n"
        try:
            edges += close_stack[-1] +","+ str(i) +","+ line.split("|")[2] +"," + str(childNum) + "\n"
        except IndexError:
            print(line)
        edgeId += 1
    else:
        for a in range(0,(lastlevel-level)/2):
            close_stack.pop()
        dot += close_stack[-1] + " -> " + str(i) + " [penwidth="+ str(penWidth) +" arrowhead=none]\n"
        edges += close_stack[-1] +","+ str(i) +","+ line.split("|")[2] +"," + str(childNum) + "\n"
        edgeId += 1
    lastlevel = level
    lastline = line
    i+=1
    lineCount += 1

dot += "\n}"

file2 = open("dot.gv","w")
file2.write(dot)
file2.close

file3 = open("edges.csv","w")
file3.write(edges)
file3.close

file4 = open("nodes.csv","w")
file4.write(nodes)
file4.close