import os

test=os.system("""echo Signing in as root
sudo whoami
echo Root Sign-in Successful
echo Updating packages
sudo apt update
echo Installing Docker
sudo apt install docker.io -y
sudo systemctl enable docker --now
sudo usermod -aG docker $USER
echo Docker Install complete.
echo installing github repositories
mkdir gihub
cd github
git clone https://github.com/JohnHammond/msdt-follina
git clone https://github.com/paranoidninja/Brute-Ratel-C4-Community-Kit
git clone https://github.com/H1R0GH057/Anonymous


""")
