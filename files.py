file = open("teams.txt", "w")

teams = ["Barnsley", "Man u", "Man City", "Liverpool", "Chelsea"]

for line in range(0, 5):
    file.write(f"{teams[line]} \n")
file.close()

file = open("teams.txt", "r")
x = 0
for x in range(0, 5):
    if x == 0 or x == 4:
        print(file.readline().strip())
    else:
        file.readline()
    x += 1
file.close()

file = open("teams.txt", "r")
lines = file.readlines()
file.close()
lines[0] = "new line \n"

file = open("teams.txt", "w")
x = 0
for x in range(0, 5):
    file.write(lines[x])
file.close()

file = open("teams.txt", "r")
x = 0
for x in range(0, 5):
    print(file.readline().strip())
file.close()