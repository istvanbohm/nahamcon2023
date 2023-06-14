from brownie import *

deployer = accounts[0]
user1 = accounts[1]
user2 = accounts[2]
user3 = accounts[3]

HOUR = 3600
DAY = 24 * HOUR 
WEEK = 7 * DAY
YEAR = 365 * DAY + 6 * HOUR

chain.snapshot()

# Deploying Mock WETH contract with deployer and mintig tokens for the users:
contract_MockWeth = deployer.deploy(MockERC20, "Mock WETH", "MWETH")
contract_MockWeth.mint(user1, 100 * 10**18)
contract_MockWeth.mint(user2, 150 * 10**18)
contract_MockWeth.mint(user3, 250 * 10**18)

# User the Mock WETH token during this test
contract_WETH = contract_MockWeth

# Deploying the Vault contract
contract_vault = deployer.deploy(Vault, contract_WETH)

# Deposit Ether with users
user1_eth_deposit = Wei(100 * 10**18)
user2_eth_deposit = Wei(100 * 10**18)
user3_eth_deposit = Wei(50 * 10**18)
contract_vault.deposit({'from':user1, 'value': user1_eth_deposit})
contract_vault.deposit({'from':user2, 'value': user2_eth_deposit})
contract_vault.deposit({'from':user3, 'value': user3_eth_deposit})

# user1 balance
user1_balance = contract_vault.balanceOf(user1)
print("user1 vault balance: {}".format(user1_balance/10**18))

# user1 balance
user2_balance = contract_vault.balanceOf(user2)
print("user2 vault balance: {}".format(user2_balance/10**18))


# Deposit WETH with users
# Aprove the WETH contract to transfer tokens from user1, then deposit tokens:
contract_WETH.approve(contract_vault, 99999999999 * 10**18, {'from': user1})   # it is common for users to approve bigger amount 
                                                                               # so they don't have to approve again
                                                                               # using this they can save money by paying less gas
weth_deposit_amount = Wei(25 * 10**18)
contract_vault.depositWeth(user1, user1, weth_deposit_amount, {'from':user1})
weth_deposit_amount = Wei(75 * 10**18)
contract_vault.depositWeth(user1, user1, weth_deposit_amount, {'from':user1})

# Aprove the WETH contract to transfer tokens from user2, then deposit tokens:
contract_WETH.approve(contract_vault, 99999999999 * 10**18, {'from': user2})
weth_deposit_amount = Wei(25 * 10**18)
contract_vault.depositWeth(user2, user2, weth_deposit_amount, {'from':user2})
weth_deposit_amount = Wei(25 * 10**18)
contract_vault.depositWeth(user2, user2, weth_deposit_amount, {'from':user2})


# user1 balance
user1_balance = contract_vault.balanceOf(user1)
print("user1 vault balance: {}".format(user1_balance/10**18))

# user1 balance
user2_balance = contract_vault.balanceOf(user2)
print("user2 vault balance: {}".format(user2_balance/10**18))

# Wait 1 year
chain.sleep(YEAR)
chain.mine(1)

# Withdraw balance with user1
print("user1 ETH balance: {}".format(user1.balance()/10**18))

user1_balance = contract_vault.balanceOf(user1)
print("user1 vault balance: {}".format(user1_balance/10**18))

contract_vault.withdraw(user1_balance,{'from':user1})

print("user1 ETH balance: {}".format(user1.balance()/10**18))

