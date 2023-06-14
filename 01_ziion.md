
# 1 Installing ZIION

## 1.1 Download ZIION

https://www.ziion.org/download

## 1.2 Read the Documentation

https://docs.ziion.org/install-ziion/get-the-ziion-vm-up-and-running

## 1.3 Confirm the Hash of the Virtual Image File

### Windows 

Run powershell and execute the following command:

```
certutil.exe -hashfile .\ZIION_22.8_amd64.ova SHA256
```

### Linux

Run terminal and execute the following command:

```
sha256sum .\ZIION_22.8_amd64.ova
```

### MacOS

```
shasum -a 256 ./ZIION_22.8_arm64.pvmp
```

# 2 Configure ZIION

## Change Language

Settings > Region & Language > Input Sources 

## Install Virtual Machine Tools 

- VirtualBox Guest Additions

- VMware Tools

## Configure Terminal (Optional)

- Create a new profile 
- Disable terminal bell 
- Modify color schemes
- Keep in mind that the default shell is not bash








