# Import required libraries
from web3 import Web3, HTTPProvider

# Connect to an Ethereum node
w3 = Web3(HTTPProvider('https://1rpc.io/sepolia'))

# Hash transaction
tx = '0x48bbc022bac5333c5a1c66d93398429f09c6fedf07d52dfc30e96c0f9aeaacfb'

# Get transaction data
def getTransaction(txHash):
    return w3.eth.get_transaction(txHash)

print(getTransaction(tx))