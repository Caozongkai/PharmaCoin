import hashlib
import datetime
import random

class Block:
	def __init__(self, index, timestamp, data, prev_hash):
		self.index = index
		self.timestamp = timestamp
		self.data = data
		self.prev_hash = prev_hash
		self.hash = self.hash_block()
		print("Block #%s generated!" % index)
		print("Date: %s" % timestamp)
		print("Block Data: %s" % data)
		print("Block Salt: %s" % self.salt)
		print("Block Hash: %s\n" % self.hash)

	def hash_block(self):
		temp = ""
		while temp[:4] != "0000":
			salt = random.getrandbits(32)
			text = "".join(map(str, [self.index, self.timestamp, self.data, self.prev_hash, salt]))
			text = text.encode("utf-8")
			sha = hashlib.sha256()
			sha.update(text)
			temp = sha.hexdigest()
		self.salt = salt
		return temp

def next_block(prev_block, data):
	index = prev_block.index + 1
	timestamp = datetime.datetime.now()
	prev_hash = prev_block.hash
	return Block(index, timestamp, data, prev_hash)

first = Block(0, datetime.datetime.now(), "Block #0", "0")
block = first
for i in range(10):
	block = next_block(block, "Block #%s" % i)
