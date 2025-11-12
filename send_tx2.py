# Import required libraries
from web3 import Web3

# Connect to an Ethereum node
web3 = Web3(Web3.HTTPProvider('https://1rpc.io/sepolia'))

# Set sender and recipient addresses
sender_address = '0xa5EFE8C042A559F13D975293af7D4CCe8a36b2A2'
recipient_address = '0x89c6c7aaE769a189BdBACf965705FF92669b606e'

# Set private key for the sender's account. 
# DO NOT SHARE YOUR PRIVATE KEY.
private_key = '0x4f98af4cbffe4153c29359b10283757aa0303bb1bcf914c2086597284d62dd6d'

# Fetch balance data
balance_sender = web3.from_wei(web3.eth.get_balance(sender_address), 'ether')
balance_recipient = web3.from_wei(web3.eth.get_balance(recipient_address), 'ether')

print(f'The balance of { sender_address } is: { balance_sender } ETH')
print(f'The balance of { recipient_address } is: { balance_recipient } ETH')

# Get and determine gas parameters
latest_block = web3.eth.get_block("latest")
base_fee_per_gas = latest_block.baseFeePerGas   # Base fee in the latest block (in wei)
max_priority_fee_per_gas = web3.to_wei(1, 'gwei') # Priority fee to include the transaction in the block
max_fee_per_gas = (5 * base_fee_per_gas) + max_priority_fee_per_gas # Maximum amount you’re willing to pay 

# Define the transaction parameters
transaction_params = {
    'from': sender_address,
    'to': recipient_address,
    'value': web3.to_wei(0.01, 'ether'),  # Transaction value (0.1 Ether in this example)
    'nonce': web3.eth.get_transaction_count(sender_address),
    'gas': 21000,  # Gas limit for the transaction
    'maxFeePerGas': max_fee_per_gas, # Maximum amount you’re willing to pay 
    'maxPriorityFeePerGas': max_priority_fee_per_gas, # Priority fee to include the transaction in the block
    'chainId': 11155111 # ChainId of Sepolia Testnet
}

# Sign the transaction
transaction = web3.eth.account.sign_transaction(transaction_params, private_key)

# Send the transaction
transaction_hash = web3.eth.send_raw_transaction(transaction.raw_transaction)

# Wait for the transaction to be mined
transaction_receipt = web3.eth.wait_for_transaction_receipt(transaction_hash)

# Check the transaction status
if transaction_receipt.status:
    print('Transaction successful!')
    print('Transaction hash:', transaction_hash.hex())
    print(f'Explorer link: https://sepolia.etherscan.io/tx/{transaction_hash.hex()}')
else:
    print('Transaction failed.')

# Fetch balance data after the transaction
balance_sender = web3.from_wei(web3.eth.get_balance(sender_address), 'ether')
balance_recipient = web3.from_wei(web3.eth.get_balance(recipient_address), 'ether')

print(f'The balance of { sender_address } is: { balance_sender } ETH')
print(f'The balance of { recipient_address } is: { balance_recipient } ETH')
