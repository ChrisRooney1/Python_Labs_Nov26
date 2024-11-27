#!/usr/bin/python

Belgium = 'Belgium,10445852,Brussels,737966,Europe,1830,Euro,Catholicism,Dutch,French,German'

fields = Belgium.split(",")

new_belgium = ":".join(fields)

print("-" * len(Belgium))
print(new_belgium)

print(f"The population of Belgium: {fields[1]} + the population of the largest city: {fields[3]} is")
population = int(fields[1]) + int(fields[3])
print(population)

print("-" * len(Belgium))

for line in open(r'C:\Project\Python_Labs_Nov26\labs\projects\04 String Handling\messier.txt',encoding='latin_1'):
    if not line: break
    if line.startswith("M"):
        if line[6:40].rstrip() != "":
            print(line[0:4].rstrip() + "|" + line[6:40].rstrip()) 
        else:
            print(line[0:4].rstrip() + "|no name|" + "")