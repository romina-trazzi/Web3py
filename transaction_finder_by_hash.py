# Import required libraries
from web3 import Web3

# Connect to an Ethereum node
web3 = Web3(Web3.HTTPProvider('https://1rpc.io/sepolia'))

# Set sender and recipient addresses
sender_address = '0xa5EFE8C042A559F13D975293af7D4CCe8a36b2A2'
recipient_address = '0x89c6c7aaE769a189BdBACf965705FF92669b606e'

# Set private key for the sender's account. 
private_key = '0x4f98af4cbffe4153c29359b10283757aa0303bb1bcf914c2086597284d62dd6d'

# Fetch balance data
balance_sender = web3.from_wei(web3.eth.get_balance(sender_address), 'ether')
balance_recipient = web3.from_wei(web3.eth.get_balance(recipient_address), 'ether')

print(f'The balance of { sender_address } is: { balance_sender } ETH')
print(f'The balance of { recipient_address } is: { balance_recipient } ETH')

# Hash transaction
tx = '0x48bbc022bac5333c5a1c66d93398429f09c6fedf07d52dfc30e96c0f9aeaacfb'

# Get transaction data
def getTransaction(txHash):
    return web3.eth.get_transaction(txHash)

print(getTransaction(tx))