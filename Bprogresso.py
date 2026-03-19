from time import sleep
import os
print("\033[?25l]")
i = 1

while i <= 140:
    print(chr(9608) * i + " " + str(i))
    sleep(.1)
    os.system("cls")
    i += 1

    
