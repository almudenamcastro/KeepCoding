f=open("perro.txt", "r")
g=open("gato.txt", "w")

for line in f.readlines():
    line = line.lower().replace("perr", "gat")
    g.write(line)

f.close()
g.close()