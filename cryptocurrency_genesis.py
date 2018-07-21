from cryptocurrency_block import *
import datetime as date

def create_genesis_block():
    """
    manually creates a first block of a blockchain with index of 0 and
    arbitrary previous hash.
    first_block = create_genesis_block()
    first_block
    """
    return Block(0, date.datetime.now(), "Genesis Block", "0")