import os

print("Signing in as root")

test=os.system("sudo whoami")
while True:
  if test=="root":
    print("Root Sign-in Successful")
    break
  elif:
    "An error occured, trying again."
    continue

os.system("""sudo apt update""")
