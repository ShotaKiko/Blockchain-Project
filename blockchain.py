#Initializing the blockchain
blockchain = []

def get_last_blockchain_value():
    """Returns the last value in the blockchain via index"""
    
    return blockchain[-1]
    

def add_value(transaction_amount, last_transaction = 1):
    """ Append a new value as well as the last blockchain value to the blockchain
    
    Arguments:
    :transcaction amount: The amount that should be added.
    :last_transaction: The last blockchain transaction which defaults to 1.
    """
    
    blockchain.append([ last_transaction, transaction_amount])


def get_user_input():
    """Returns the input of the user that 
    will be taken as the new transasction amount(float value)"""
    
    return float(input("Your transaction amount please: "))

tx_amount = get_user_input()
add_value(tx_amount)

tx_amount = get_user_input()
add_value(last_transaction = get_last_blockchain_value(), transaction_amount = tx_amount)

tx_amount = get_user_input()
add_value(tx_amount, get_last_blockchain_value())

print(blockchain)