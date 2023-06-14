from brownie import *

deployer = accounts[0]
user1 = accounts[1]
user2 = accounts[2]
hacker = accounts[3]

HOUR = 3600
DAY = 24 * HOUR 
WEEK = 7 * DAY

# Mock NFT contract for testing
contract_BHAP = deployer.deploy(MockNft, "Bored Humans Apartment Club", "BHAP")

# Test data
asset = contract_BHAP
asset_id = 111
minbid = Wei("1 ether")	# 1 * 10**18
duration = WEEK

# Get the original owner of the NFT
contract_BHAP.mint(deployer, asset_id)

# Deploy contract with deployer
contract_auction  = deployer.deploy(Auction)

# Approve the transfer of the token
contract_BHAP.approve(contract_auction, asset_id, {'from': deployer})

# Initialize the auction
contract_auction.initialize(asset,asset_id,minbid,duration, {'from':deployer})

###########################################

chain.snapshot()

# user1 bids 
contract_auction.bid({'from': user1, 'value' : Wei("2 ether")})
assert contract_auction.winner()==user1

# user2 bids
contract_auction.bid({'from': user2, 'value' : Wei("5 ether")})
assert contract_auction.winner()==user2

# Wait 1 week 
chain.sleep(WEEK + 1)
chain.mine(1)

# the NFT owner is the auction contract
assert contract_BHAP.ownerOf(asset_id) == contract_auction

# the winner withdraws the NFT 
contract_auction.withdraw({'from': user2})

# the NFT owner now is the winner 
assert contract_BHAP.ownerOf(asset_id) == user2




