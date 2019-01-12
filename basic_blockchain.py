import datetime
import hashlib

class Block:

	blockNo = 0
	data = None
	next = None
	hash = None
	nonce = 0
	previous_hash = 0x0
	timestamp = datetime.datetime.now()

	def __init__(self , data):
		self.data = data

	def hash(self):
		h = hashlib.sha256()
		h.update(
			str(self.nonce).encode('utf-8')+
			str(self.data).encode('utf-8')+
			str(self.previous_hash).encode('utf-8')+
			str(self.nonce).encode('utf-8')+
			str(self.blockNo).encode('utf-8')
			)
		return h.hexdigest()

	def __str__(self):
		return 'Block No ' + str(self.blockNo) + 'Block hash' + str(self.hash())

class blockchain:

	maxNonce = 2**32
	diff = 10
	target = 2**(256 - diff)
	block = Block('genesis')
	head = block

	def add(self , block):
		block.previous_hash = self.block.hash()
		block.blockNo = self.block.blockNo+1

		self.block.next = block
		self.block = block

	def mine(self , block):
		for n in range(self.maxNonce):
	            #is the value of the given block's hash less than our target value?
	            if int(block.hash(), 16) <= self.target:
	                #if it is,
	                #add the block to the chain
	                self.add(block)
	                print(block)
	                break
	            else:
	                block.nonce += 1

chain = blockchain()
for n in range(10):
	chain.mine(Block('Block' + str(n+1)))

while chain.head != None:
	print(chain.head)
	chain.head = chain.head.next



