from brownie import *
import json
import requests

# Etherscan Key for loadContractABIFromAddress
etherscan_key = "<ETHERSCAN_KEY>"

def loadContractABIFromAddress(contractName, address):
	url = "https://api.etherscan.io/api?module=contract&action=getabi&address={}&apikey={}".format(str(address),str(etherscan_key))
	r = requests.get(url)
	result = r.json()['result']
	result = result.replace("false", "False")
	result = result.replace("true", "True")
	abi = eval(result.split("\n")[0])
	return Contract.from_abi(contractName, address, abi)

deployer = accounts[0]
user1 = accounts[1]
user2 = accounts[2]
user3 = accounts[3]
user4 = accounts[4]
user5 = accounts[5]
user6 = accounts[6]
user7 = accounts[7]
user8 = accounts[8]
user9 = accounts[9]

HOUR = 3600
DAY = 24 * HOUR 
WEEK = 7 * DAY 

########### Native Token (Ether) ###########

# balance of an user	# 1 token = 1 Wei, 10**18 Wei = 1 ETH
user1.balance()

# send ETH from user1 to user2
user1.transfer(user2,10 * 10**18)



############# Test ERC20 Token #############
# ERC20 tokens are like money in role playing games.

# Deploy a Mock ERC20 token contract with deployer
contract_MockWeth = deployer.deploy(MockERC20, "Mock WETH", "MWETH")	# the first parameter is the token contract
																		# the following parameters are the parameters of the constructor

# Mint tokens for user1
contract_MockWeth.mint(user1, 1000 * 10**18, {'from': deployer})		# you can configure who sends the transaction 
																		# using the additional parameters inside the {}

# Get the MWETH balance of user1
contract_MockWeth.balanceOf(user1)										# if there is no from parameter, then the sender is the contract deployer

# Transfer MWETH tokens to user2 from the msg sender
contract_MockWeth.transfer(user2, 250 * 10**18, {'from': user1})

# Allow user3 to transfer 100 * 10**18 tokens of user1
contract_MockWeth.approve(user3, 100*10**18, {'from': user1})

# Transfer the tokens of user1 to user2
contract_MockWeth.transferFrom(user1, user2, 100 * 10**18, {'from': user3})



############# Test NFT Token #############
# NFT tokens are like items in role playing games.

# Deploy the test NFT contract
contract_MockNft = deployer.deploy(MockNft, "Bored Humans Apartment Club", "BHAP")

# Mint a token with ID 222 for user1
nft_id = 222
contract_MockNft.mint(user1, nft_id)

# Get the owner of an BHAP NFT
contract_MockNft.ownerOf(nft_id)

# Transfer the NFT from user1 to user2
contract_MockNft.transferFrom(user1, user2, nft_id, {'from': user1})

# Allow user3 to transfer the NFT of user2
contract_MockNft.approve(user3, nft_id, {'from': user2})

# Transfer the NFT from user2 to user4 with user3
contract_MockNft.transferFrom(user2, user4, nft_id, {'from': user3})



############# Using Tokens From MAINNET #############

# Get these data from Etherscan: https://etherscan.io/token/0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2#code
ADDR_WETH = "0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2"
NAME_WETH = "WETH9"
ADDR_WETH_WHALE = "0xf04a5cc80b1e94c69b48f5ee68a08cd2f09a7c3e"

# Download the interface of the contract with Etherscan and connect to it using Infura
contract_WETH = loadContractABIFromAddress(NAME_WETH,ADDR_WETH)

# Check the decimals of the contract	
contract_WETH.decimals()	# 18, which means 10**18 tokens = 1 WETH

# Transfer 100 WETH from a whale to user1
contract_WETH.transfer(user1, 100 * 10**18,{'from': ADDR_WETH_WHALE})


# Get these data from Etherscan: https://etherscan.io/token/0xbc4ca0eda7647a8ab7c2061c2e118a18a936f13d#code
ADDR_BYAC = "0xBC4CA0EdA7647A8aB7C2061c2E118A18a936f13D"
NAME_BYAC = "BoredApeYachtClub"

# Download the interface of the contract with Etherscan and connect to it using Infura
contract_BAYC = loadContractABIFromAddress(NAME_BYAC, ADDR_BYAC)

# Transfer a NFT from their owner to user1
nft_id = 100
nft_owner = contract_BAYC.ownerOf(nft_id)
contract_BAYC.transferFrom(nft_owner, user1, nft_id, {'from': nft_owner})

# Get the owner of an BYAC NFT
contract_BAYC.ownerOf(nft_id)
