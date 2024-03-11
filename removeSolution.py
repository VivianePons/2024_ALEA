import sys
import json

def remove_solution(jdata):
    for c in jdata["cells"]:
        if "source" in c:
            inside_solution = False
            new_source = []
            for l in c["source"]:
                if inside_solution:
                    if l.find("# end solution") != -1:
                        inside_solution = False
                elif l.find("# begin solution") != -1:
                    inside_solution = True
                elif l.find("# one line solution replace") != -1:
                    i = l.index("# one line solution replace")
                    new_source.append(l[i+28:])
                elif l.find("# one line solution") == -1:
                    new_source.append(l)
            c["source"] = new_source
        if "outputs" in c:
            c["outputs"] = []




#input file
if len(sys.argv)<2:
    print("Please provide a file name")
inputName = sys.argv[1]

#output file
if len(sys.argv)>2:
    outputName = sys.argv[2]
else: outputName = "output"

jdata = None
with open(inputName,"r") as inputfile:
    jdata = json.load(inputfile)

remove_solution(jdata)

with open(outputName,"w") as outfile:
    json.dump(jdata,outfile)



