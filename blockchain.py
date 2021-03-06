# Initializing the blockchain
MINING_REWARD = 10

genesis_block = {"previous_hash": "origin", "index": 0, "transactions": []}

blockchain = [genesis_block]
open_transactions = []
owner = "Shota"
participants = {"Shota"}


def hash_block(block):
    return "-".join([str(block[key]) for key in block])


def get_balance(participant):
    """Retrieves balance statement for participant provided
        Argument:
            :participant: the person in question
    """
    # list comp to pull participant from transaction list
    tx_sender = [
        [tx["amount"] for tx in block["transactions"] if tx["sender"] == participant]
        for block in blockchain
    ]
    # getting amt for tx for all tx in block if sender matched participant provided-- applied for every block in chain
    open_tx_sender = [
        tx["amount"] for tx in open_transactions if tx["sender"] == participant
    ]  # for checking open tx balance
    tx_sender.append(
        open_tx_sender
    )  # update with all found sending values in open transactions
    print("TXSENDER", tx_sender)
    amount_sent = 0
    for transaction in tx_sender:
        if len(transaction) > 0:
            print("Transaction1", transaction)
            amount_sent += sum(transaction)
    # getting amt for tx for all tx in block if recipient matched participant provided -- applied for every block in chain
    tx_recipient = [
        [tx["amount"] for tx in block["transactions"] if tx["recipient"] == participant]
        for block in blockchain
    ]
    print("TXRECIPIENT", tx_recipient)
    amount_received = 0
    for transaction in tx_recipient:
        if len(transaction) > 0:
            print("Transaction2", transaction)
            amount_received += sum(transaction)
    return amount_received - amount_sent  # Current balance


def get_last_blockchain_value():
    """Returns the last value in the blockchain via index"""
    if len(blockchain) < 1:
        return None
    return blockchain[-1]


def verify_transaction(transaction):
    sender_balance = get_balance(transaction["sender"])
    return sender_balance >= transaction["amount"]


def add_transaction(recipient, sender=owner, amount=1.0):
    """ Append a new value as well as the last blockchain value to the blockchain
    
    Arguments:
        :sender: The defined sender of the coins
        :recipient: The defined receiver of the coins
        :amount: The defined amount of coins being sent (default = 1.0)
    """
    transaction = {"sender": sender, "recipient": recipient, "amount": amount}

    if verify_transaction(transaction):
        open_transactions.append(transaction)
        participants.add(sender)
        participants.add(recipient)
        return True
    return False


def mine_block():
    """All open transactions are taken and added to a new block"""
    last_block = blockchain[-1]
    hashed_block = hash_block(last_block)
    reward_transaction = {
        "sender": "MINING",
        "recipient": owner,
        "amount": MINING_REWARD,
    }
    copied_transactions = open_transactions[:]
    copied_transactions.append(reward_transaction)
    block = {
        "previous_hash": hashed_block,
        "index": len(blockchain),  # will be an untaken index
        "transactions": copied_transactions,
    }
    blockchain.append(block)
    return True  # To used in if else chain


def get_transaction_data():
    """Returns the input of the user that 
    will be taken as the new transasction amount(float value)
    
    Returns:
        :tx_recipient: transaction recipient
        :tx_amount: transaction amount
    """
    tx_recipient = input("Enter the recipient of the transaction: ")
    tx_amount = float(input("Your transaction amount please: "))
    return tx_recipient, tx_amount  # tuple with needed values


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
        if block["previous_hash"] != hash_block(
            blockchain[index - 1]
        ):  # recalc hash of last block and compare with prev stored hash
            return False
    return True


def verify_transactions():
    # is_valid = True
    # for tx in open_transactions:
    #     if verify_transaction(tx):
    #         is_valid = True
    #     else:
    #         is_valid = False
    # return is_valid
    return all([verify_transaction(tx) for tx in open_transactions])


running = True

while running:
    print("Please choose how to proceed")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("1.) Add a new transaction")
    print("2.) Mine a new block")
    print("3.) Ouput the current blockchain")
    print("quit.) Quit the loop")
    print("4.) Repeat Question")
    print("5.) Ouput participants")
    print("hack.) Manipulate the chain")
    print("6.) Verify transaction validity")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    user_choice = get_user_choice()

    if user_choice == "1":
        tx_data = get_transaction_data()
        recipient, amount = tx_data  # pull from transaction tuple
        if add_transaction(recipient, amount=amount):
            print("Added transaction!")
        else:
            print("Transaction failed...")
        print("OPEN TRANSACTIONS: ", open_transactions)

    elif user_choice == "2":
        if mine_block():
            open_transactions = (
                []
            )  # reset transactions to empty list following succesful mine

    elif user_choice == "3":
        print_blockchain_elements()

    elif user_choice == "hack" or user_choice == "h":
        if len(blockchain) >= 1:
            blockchain[0] = {
                "previous_hash": "",
                "index": 0,
                "transactions": [
                    {"sender": "Ranger", "recipient": "Doug", "amount": 100}
                ],
            }

    elif user_choice == "4":
        continue

    elif user_choice == "5":
        print(participants)

    elif user_choice == "6":
        if verify_transactions():
            print("``````````````````````ALL TRANSACTIONS VALID``````````````````````")
        else:
            print("Invalid transaction detected")

    elif user_choice == "quit" or user_choice == "q":
        running = False

    else:
        print("Invalid input...Please enter a valid option: ")

    if not verify_chain():
        print_blockchain_elements()
        print("INVALID BLOCKCHAIN")
        break
    print(f'Balance of Shota: {get_balance("Shota"):6.2f}')
else:
    print("Process Complete !")
