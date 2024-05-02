import os
os.system("cls || clear")

print("==== Números ímpares ====")

for i in range(1,20):
    if (i % 2) != 0:    
        print(f"Número: {i}")

print("==== Números pares ====")
for i in range (1,20):
    if (i % 2) == 0:
        print(f"Número: {i}")
