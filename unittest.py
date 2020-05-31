from blockchain import *


clients = Clients()
blockchain = BlockChain()

def spawn_client( name, pub, priv):
    sample_client = Client( pub, priv, name )
    clients.add( sample_client )


def sample_transaction():
    transaction = {
        'recv': "swiss",
        'type': "transfer",
        "amount": 5000000
    }
    transaction = Transaction( **transaction )
    prev = blockchain.chain[-1]
    block = Block( prev, 'admin', 1915, transaction)
    print( blockchain.mine( block ) )

def sample_amount():
    print(blockchain.amount( 'admin' ))
