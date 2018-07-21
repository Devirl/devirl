import hashlib as hasher

class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.hash_block()

    def hash_block(self):
        """
        generates a cryptographic hash of the block’s index, timestamp, data, and the hash of the previous block’s hash.
        hash_block => '18627f84562249c397955a1bbde617992fea2180afe0e4645ea131df12051a20'
        """
        sha = hasher.sha256()
        sha.update((str(self.index) +
                   str(self.timestamp) +
                   str(self.data) +
                   str(self.previous_hash)).encode('utf-8'))
        return sha.hexdigest()