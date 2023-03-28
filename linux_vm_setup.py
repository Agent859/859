import os

test=os.system("""echo Signing in as root
cd ~
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
mkdir github
cd github
git clone https://github.com/JohnHammond/msdt-follina
git clone https://github.com/paranoidninja/Brute-Ratel-C4-Community-Kit
git clone https://github.com/H1R0GH057/Anonymous
git clone https://github.com/debajyotidasgupta/blackeye.git
cd ..
echo Github Repositories installed
echo Starting apt installs
sudo apt install steghide -y
sudo apt install beef -y
echo apt installs complete
echo setting up Proxychains

echo ---OPEN INFO FILE---
cd ../..
nano /etc/proxychains.conf
echo Proxychain setup complete


""")
