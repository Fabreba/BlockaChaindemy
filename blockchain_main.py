from datetime import datetime

from blockchain import Block, Blockchain

# Create the blockchain
blockchain = Blockchain()

# Add blocks to the blockchain
blockchain.add_block(Block(1, datetime.now(), "Transaction Data 1", ""))
blockchain.add_block(Block(2, datetime.now(), "Transaction Data 2", ""))
blockchain.add_block(Block(3, datetime.now(), "Transaction Data 3", ""))

# Print the contents of the blockchain
for block in blockchain.chain:
    print("Block #" + str(block.index))
    print("Timestamp: " + str(block.timestamp))
    print("Data: " + block.data)
    print("Hash: " + block.hash)
    print("Previous Hash: " + block.previous_hash)
    print("\n")
    