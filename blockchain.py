#Initializing the blockchain
genesis_block = {
    'previous_hash': '',
    'index': 0,
    'transactions': []
}

blockchain = [genesis_block]
open_transactions = []
owner = "Shota"

def hash_block(block):
    return '-'.join([str(block[key]) for key in block])


def get_last_blockchain_value():
    """Returns the last value in the blockchain via index"""
    if len(blockchain) < 1:
        return None
    return blockchain[-1]
    

def add_transaction(recipient, sender=owner, amount=1.0):
    """ Append a new value as well as the last blockchain value to the blockchain
    
    Arguments:
        :sender: The defined sender of the coins
        :recipient: The defined receiver of the coins
        :amount: The defined amount of coins being sent (default = 1.0)
    """
    transaction = {
        "sender": sender,
        "recipient": recipient,
        "amount": amount
    }

    open_transactions.append(transaction)


def mine_block():
    """All open transactions are taken and added to a new block"""
    last_block = blockchain[-1]
    hashed_block = hash_block(last_block)
    block = {
        'previous_hash': hashed_block,
        'index':len(blockchain), #will be an untaken index
        'transactions': open_transactions
    }
    blockchain.append(block)


def get_transaction_data():
    """Returns the input of the user that 
    will be taken as the new transasction amount(float value)
    
    Returns:
        :tx_recipient: transaction recipient
        :tx_amount: transaction amount
    """
    tx_recipient = input("Enter the recipient of the transaction: ")
    tx_amount = float(input("Your transaction amount please: "))
    return tx_recipient, tx_amount #tuple with needed values


def get_user_choice():
    """Allows the user whether to print the current blockchain
    or to add another transaction"""
    user_input = input("Your choice: ")
    return user_input


def print_blockchain_elements():
    """Output the blockchain list to the console"""
    counter = 1
    for block in blockchain:
        print(f"Blockchain Output-- Block -- {counter}")
        print(block)
        counter += 1
    else:
        print("-" * 22)


def verify_chain():
    """Verifies that the stored hash with the recalcucated has of previous block"""
    for (index, block) in enumerate(blockchain):
        if index == 0:
            continue
        if block['previous_hash'] != hash_block(blockchain[index - 1]): #recalc hash of last block and compare with prev stored hash
            return False
    return True
    

running = True

while running:
    print("Please choose how to proceed")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("1.) Add a new transaction")
    print("2.) Mine a new block")
    print("3.) Ouput the current blockchain")
    print("quit.) Quit the loop")
    print("4.) Repeat Question")
    print("hack.) Manipulate the chain")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    user_choice = get_user_choice()
    
    if user_choice == "1":
        tx_data = get_transaction_data()
        recipient, amount = tx_data #pull from transaction tuple
        add_transaction(recipient, amount = amount)
        print("OPEN TRANSACTIONS: ", open_transactions)
    
    elif user_choice == "2":
        mine_block()
    
    elif user_choice == "3":
        print_blockchain_elements()
    
    elif user_choice == "hack":
        if len(blockchain) >= 1:
            blockchain[0] = {
                'previous_hash': "",
                'index': 0,
                'transactions': [{"sender": "Ranger","recipient": "Doug", "amount": 100}]
            }
    
    elif user_choice == "4":
        continue
    
    elif user_choice == "quit":
        running = False
    
    else:
        print("Invalid input...Please enter a valid option: ")
    
    if not verify_chain():
        print_blockchain_elements()
        print("INVALID BLOCKCHAIN")
        break
else:
    print("Process Complete !")