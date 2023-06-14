# INSTALL TOOLS ON Ubuntu 22.04

## Update the package list and the system
```
sudo apt-get update
sudo apt-get upgrade
```

## Install Python 3.10 and pipx
```
sudo apt install build-essential dkms linux-headers-$(uname -r)
sudo apt install python3.10-venv
sudo apt install python3-pip
python3 -m pip install --user pipx
python3 -m pipx ensurepath
```

You will need to open a new terminal or re-login for the PATH changes to take effect.


## Install nvm + npm
```
sudo apt install nodejs npm
sudo apt install curl 
curl https://raw.githubusercontent.com/creationix/nvm/master/install.sh | bash 
nvm install 16.16
nvm alias default 16.16
nvm use 16.16
```

## Install Hardhat
From home directory:
```
npm install --save-dev hardhat
```

## Install Brownie
```
pipx install eth-brownie
```

## Install Ganache
```
sudo npm install -g ganache-cli@v6.12.2
```


# INSTALL TOOLS ON Ubuntu 20.04

## Update the package list and the system
```
sudo apt-get update
sudo apt-get upgrade
```

## Install Python 3.8 and pipx
```
sudo apt install build-essential dkms linux-headers-$(uname -r)
sudo apt install python3-pip 
sudo apt install python3.8-venv
python3 -m pip install --user pipx
python3 -m pipx ensurepath
```

You will need to open a new terminal or re-login for the PATH changes to take effect.


## Install nvm + npm
```
sudo apt install nodejs npm
sudo apt install curl 
curl https://raw.githubusercontent.com/creationix/nvm/master/install.sh | bash 
```
You will need to open a new terminal or re-login for the PATH changes to take effect.
```
nvm install 16.16
nvm alias default 16.16
nvm use 16.16
```

## Install Hardhat
From home directory:
```
npm install --save-dev hardhat
```

## Install Brownie
```
pipx install eth-brownie
```

## Install Ganache
```
sudo npm install -g ganache-cli@v6.12.2
```

