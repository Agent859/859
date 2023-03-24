import os

print("Signing in as root")

test=os.system("""echo Signing in as root

sudo whoami

echo Root Sign-in Successful

echo Updating packages

sudo apt update""")
