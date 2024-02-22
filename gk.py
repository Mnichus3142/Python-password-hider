check = 0

try:
  import tty
  import sys
  
  check = 1
except:
  import msvcrt
  
  check = 2
  
def getkeyInASCII ():   
    while True:
        if check == 1:
            tty.setcbreak(sys.stdin)
            return ord(str(sys.stdin.read(1)[0]))
    
        elif check == 2:
            if msvcrt.kbhit():
                return list(msvcrt.getch())[0]
        
        else:
            return 0