f = open("example.txt", "w", encoding=-8)
for i in range(10):
    f.write(f"{i+1}번째")
f.close()