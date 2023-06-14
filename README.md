# NahamCon 2023 - Ethereum  Smart Contract Hacking Workshop

## 1 Preparations

[Setting up ZIION](https://github.com/istvanbohm/nahamcon2023/blob/main/01_ziion.md) or [installing tools manually on Ubuntu](https://github.com/istvanbohm/nahamcon2023/blob/main/01_manual_install.md)

[Setting up INFURA and Etherscan](https://github.com/istvanbohm/nahamcon2023/blob/main/01_ethereum_services.md)

## 2 Compile the project

- Clone the repository
```
git clone https://github.com/istvanbohm/nahamcon2023.git
```
- Enter ther brownie direcotry
```
cd NahamCon2023/brownie/
```
- Install the required NPM packages by executing the following command from the brownie directory
```
npm install
```

## 3 Simulate the Ethereum blockchain locally

Simulate the blockchain locally using ganache, to start execute the following command:

```
ganache-cli --hardfork istanbul --fork https://mainnet.infura.io/v3/<INFURA_KEY> -i 80000000
```

Note that you need to get the URL from [INFURA](https://github.com/istvanbohm/nahamcon2023/blob/main/01_ethereum_services.md).

After running ganache, wait for the "RPC Listening on 127.0.0.1:8545" message, then execute the following command from the brownie directory:

```
brownie console --network mainnet-fork
```

## 4 Get Familar with Brownie and how to interact with the smart contract

- The scripts folder contains example brownie scripts.
- Paste scripts section by section and examine the behavior of the contracts.
- Learn the syntax using the examples
- The brownie documentation can be found here:
```
https://eth-brownie.readthedocs.io/en/stable/
https://eth-brownie.readthedocs.io/_/downloads/en/stable/pdf/
```

## 5 Start Hacking

Identify vulnerabilities in the contracts.

