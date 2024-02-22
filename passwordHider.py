import gk
import time

def passwordHider(prompt):
    print(prompt, end="", flush=True)
  
    password = ""
  
    while True:
        ch = gk.getkeyInASCII()
        if ch == 13 or ch == 10:
            break
        elif ch == 8:
            if password:
                password = password[:-1]
                print("\b \b", end="", flush=True)
        else:
            password = str(password) + str(chr(ch))
            print(f"{chr(ch)}", end="", flush=True)
            time.sleep(0.15)
            print("\b \b", end="", flush=True)
            print("*", end="", flush=True)
    return password