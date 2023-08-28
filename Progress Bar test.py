import time
import os

# ASCII Greyscale Stack Overflow: https://stackoverflow.com/a/74186686
# Output to CMDLine using print: https://stackoverflow.com/a/47558496
# Output to CMDLine using sys.dout: https://docs.python.org/3/library/sys.html#sys.stdout
# Print Documentation: https://docs.python.org/3/library/functions.html?highlight=print#print
# Enumerate Documentation: https://docs.python.org/3/library/functions.html?highlight=enumerate#enumerate

def clearTerminal():
    os.system('cls||clear')

progressBarLength = 10

clearTerminal()
for progress in range(0, progressBarLength + 1):
    print(f'{("█" * progress)}{("░" * (progressBarLength - progress))} {round((progress/progressBarLength) * 100)}%', end="\r")
    time.sleep(0.2)
