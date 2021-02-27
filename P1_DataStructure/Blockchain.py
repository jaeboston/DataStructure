import hashlib
import time 
  

class Block:

  def __init__(self, timestamp, data, previous_hash):
    self.timestamp = timestamp
    self.data = data
    self.previous_hash = previous_hash
    self.hash = self.calc_hash()

    self.previous = None


  def calc_hash(self):
    sha = hashlib.sha256()
    hash_str = self.data.encode('utf-8')
    sha.update(hash_str)
    return sha.hexdigest()   


block1 = Block(time.time(), 'data1', None)
block2 = Block(time.time(), 'data2', block1.hash)
block2.previous = block1
block3 = Block(time.time(), 'data3', block2.hash)
block3.previous = block2
block4 = Block(time.time(), 'data4', block3.hash)
block4.previous = block3

block = block4

while(block):
  print(f'Blockdata={block.data} and blockhash={block.hash}')
  block = block.previous

