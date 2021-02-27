import hashlib

import datetime

class Block:

    def __init__(self, timestamp, data, previous_hash):
      self.timestamp = timestamp
      self.data = data
      self.previous_hash = previous_hash
      self.hash = self.calc_hash()    

      self.previous_block = None

    def calc_hash(self):
      sha = hashlib.sha256()

      sha.update(self.data.encode('utf-8'))
      sha.update(str(self.timestamp).encode('utf-8'))
      sha.update(self.previous_hash.encode('utf-8'))

      return sha.hexdigest()

class Blockchain:

    def __init__(self):
        self.head = None

    def append(self, data):
        if self.head == None:
            coinbase = Block(datetime.datetime.now(), data, '0')
            self.head = coinbase
        
        temp = self.head
        newblock = Block(datetime.datetime.now(), data, temp.hash)
        self.head = newblock
        self.head.previous_block = temp
        return


#-----------------------
coinBlockchain = Blockchain()
coinBlockchain.append('1stBLock')
coinBlockchain.append('2ndBLock')
coinBlockchain.append('3rdBLock')

print(coinBlockchain.head.hash)
print(coinBlockchain.head.data)

print(coinBlockchain.head.previous_block.hash)
print(coinBlockchain.head.previous_block.data)

print(coinBlockchain.head.previous_block.previous_block.hash)
print(coinBlockchain.head.previous_block.previous_block.data)




