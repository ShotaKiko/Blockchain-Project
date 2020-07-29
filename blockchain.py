#Initializing the blockchain
blockchain = []
open_transactions = []
owner = "Shota"

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
    pass


def get_transaction_data():
    """Returns the input of the user that 
    will be taken as the new transasction amount(float value)
    
    Returns:
        :tx_recipient: transaction recipient
        :tx_amount: transaction amount
    """
    tx_recipient = input("Enter the recipient of the transaction: ")
    tx_amount = float(input("Your transaction amount please: "))
    return (tx_recipient, tx_amount) #tuple with needed values


def get_user_choice():
    """Allows the user whether to print the current blockchain
    or to add another transaction"""
    user_input = input("Your choice: ")
    return user_input


def print_blockchain_elements():
    """Output the blockchain list to the console"""
    for block in blockchain:
        print("Blockchain Output")
        print(block)
    else:
        print("-" * 22)


def verify_chain():
    """Verifies that the first index of a block(which is a list) is equal
    to the entire previous block"""
    is_valid = True
    blockchain_length = len(blockchain)
    for block_index in range(0, blockchain_length):
        if block_index == 0:
            continue
        elif blockchain[block_index][0] == blockchain[block_index - 1]: #compares the first entry to the entire previous entry
            is_valid = True
        else:
            is_valid = False #breaks loop since validity is compromised
            print("BLOCKCHAIN INVALID")
            # print("CURR", blockchain[block_index][0])
            # print("Prev", blockchain[block_index - 1])
            print_blockchain_elements() # To view the discrepency
            break
            
    return is_valid


running = True

while running:
    print("Please choose how to proceed")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("1.) Add a new transaction")
    print("2.) Ouput the current blockchain")
    print("3.) Quit the loop")
    print("4.) Repeat Question")
    print("5.) Manipulate the chain")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    user_choice = get_user_choice()
    
    if user_choice == "1":
        tx_data = get_transaction_data()
        recipient, amount = tx_data #pull from tuple
        add_transaction(recipient, amount = amount)
        print("OPEN TRANSACTIONS: ", open_transactions)
    elif user_choice == "2":
        print_blockchain_elements()
    elif user_choice == "3":
        running = False
    elif user_choice == "4":
        continue
    elif user_choice == "5":
        if len(blockchain) >= 1:
            blockchain[0] = [2]
    else:
        print("Please enter a valid option: ")
    print("Choice Registered !")
    if not verify_chain():
        break
else:
    print("Process Complete !")