import os

print("Signing in as root")

test=os.system("sudo whoami")

print("Root Sign-in Successful")
os.system("""sudo apt update""")
