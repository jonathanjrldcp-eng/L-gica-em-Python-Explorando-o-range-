import time
import os

for i  in range(10,0,-1):
    print(i)

time.sleep(2)
input("Pressione Enter para continuar...")
os.system('cls' if os.name == 'nt' else 'clear')

for i  in range(1,11):
    print(7*i)

time.sleep(2)
input("Pressione Enter para continuar...")
os.system('cls' if os.name == 'nt' else 'clear')

for i  in range(0,11,2):
    print(7*i)
input("Pressione Enter para continuar...")
os.system('cls' if os.name == 'nt' else 'clear')