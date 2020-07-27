#Initializing the blockchain
blockchain = []

def get_last_blockchain_value():
    """Returns the last value in the blockchain via index"""
    if len(blockchain) < 1:
        return None
    return blockchain[-1]
    

def add_transaction_value(transaction_amount, last_transaction=[1]):
    """ Append a new value as well as the last blockchain value to the blockchain
    
    Arguments:
    :transcaction amount: The amount that should be added.
    :last_transaction: The last blockchain transaction which defaults to 1.
    """
    if last_transaction == None:
        last_transaction = [1]
    blockchain.append([ last_transaction, transaction_amount])


def get_transaction_value():
    """Returns the input of the user that 
    will be taken as the new transasction amount(float value)"""
    user_input = float(input("Your transaction amount please: "))
    return user_input


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
    print("Output Complete")

tx_amount = get_transaction_value()
add_transaction_value(tx_amount)

running = True

while running:
    print("Please choose how to proceed")
    print("1.) Add a new transaction")
    print("2.) Ouput the current blockchain")
    print("3.) Quit the loop")
    print("4.) Repeat Question")
    user_choice = get_user_choice()
    
    if user_choice == "1":
        tx_amount = get_transaction_value()
        add_transaction_value(tx_amount, get_last_blockchain_value())
    elif user_choice == "2":
        print_blockchain_elements()
    elif user_choice == "3":
        running = False
    elif user_choice == "4":
        continue
    else:
        print("Please enter a valid option: ")
    print("Choice Registered !")

print("Process Complete !")