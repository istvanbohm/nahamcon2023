from brownie import *

deployer = accounts[0]
user1 = accounts[1]
user2 = accounts[2]
user3 = accounts[3]

HOUR = 3600
DAY = 24 * HOUR 
WEEK = 7 * DAY 

# Deploy contract with deployer
contract_tickets = deployer.deploy(Tickets)

# Create snapshot - You can go back to the last snapshot with chain.revert()
chain.snapshot()



###### Initialize contract with deployer ######
event = "Hacker Conference"
price = Wei("1 ether")    # 10^18 Wei = 1 Ether
tickets = 100
duration = WEEK
contract_tickets.initialize(event, price, tickets, duration, {'from': deployer})

# Get user1 Ether (ETH) balance
user1_balance = user1.balance() / 10**18    # 10^18 Wei = 1 Ether
print("user1 ETH balance: {}".format(user1_balance))

# Print the name of the event
event_name = contract_tickets.eventname()
print("event: {}".format(event_name))



###### Buy 5 tickets with user1 ######
number_of_ticets = 5
tickets_price = number_of_ticets * price
tx1 = contract_tickets.buy(number_of_ticets, {'from': user1, 'value' : tickets_price})

# View the transaction info:
tx1.info()

# Get user1 Ether (ETH) balance
user1_balance = user1.balance() / 10**18
print("user1 ETH balance: {}".format(user1_balance))

# Get contract Ether (ETH) balance
contract_eth_balance = contract_tickets.balance()
print("ticket contract ETH balance: {}".format(contract_eth_balance/10**18))



###### Refund 1 ticket with user1 ######
tx2 = contract_tickets.refund(1, {'from': user1})

# View the transaction info:
tx2.info()

# Number of tickets currently held by user1
user1_tickets = contract_tickets.purchased(user1)
print("user1 tickets: {}".format(user1_tickets))

# Get contract Ether (ETH) balance
contract_eth_balance = contract_tickets.balance()
print("ticket contract ETH balance: {}".format(contract_eth_balance/10**18))



# Wait 1 week 
chain.sleep(WEEK + 1)
chain.mine(1)



###### Withdraw funds with owner ###### 
contract_tickets.withdraw({'from': deployer})

# Get contract Ether (ETH) balance
contract_eth_balance = contract_tickets.balance()
print("tickets contract ETH balance: {}".format(contract_eth_balance/10**18))

# Get deployer Ether (ETH) balance
deployer_eth_balance = deployer.balance()
print("deployer ETH balance: {}".format(deployer_eth_balance/10**18))



