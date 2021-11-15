
# Initialize blockchain list
blockchain = []


def get_last_block_chain_value():
    """ Returns the last value of the current blockchain. """
    if len(blockchain) < 1:
        return None
    return blockchain[-1]


def add_transaction(transaction_amount, last_tranaction=[1]):
    """ Append a new value as well as the last blockchain value to the blockchain. 
    
    Arguments:
        :transaction_amount: the amount that should be added.
        :last_transaction: The last blockchain transaction (default [1]). """
    if last_tranaction == None:
        last_tranaction = [1]
    blockchain.append([last_tranaction, transaction_amount])


def get_transaction_value():
    """ Returns the input of the user (a new transaction amount) as a float. """
    user_input = float(input('Your Transaction Amount Please: '))
    return user_input


def get_user_choice():
    user_input = input('Your choice: ')
    return user_input


def print_blockchain_elements():
    # Output the blockchain list to the console
    for block in blockchain:
        print('-' * 20)
        print('Outputting Block')
        print(block)
    else:
        print('-' * 20)


def verify_chain():
    # block_index = 0
    is_valid = True
    for block_index in range(len(blockchain)):
        if block_index == 0:
            continue          
        if blockchain[block_index] [0] == blockchain[block_index - 1]:
            is_valid = True
        else:
            is_valid = False
            break
    return is_valid;


def exit_program():
    print('\n Done! \n')
    exit()


waiting_for_input = True

while waiting_for_input:
    print('Please choose:')
    print('1: Add a new transaction value')
    print('2: Output the blockchain blocks')
    print('3: Quit')
    print('H: Hack the chain')
    user_choice = get_user_choice()
    if user_choice == '1':
        tx_amount = get_transaction_value()
        add_transaction(tx_amount, get_last_block_chain_value())
    elif user_choice == '2':
        print_blockchain_elements()
    elif user_choice == '3':
        waiting_for_input = False
    elif user_choice == 'H':
        if len(blockchain) >= 1:
            blockchain[0] = [2]
    else:
        print('====== Input was invalid, please pick a value from the list! ======')
    if not verify_chain():
        print_blockchain_elements()
        print('Invalid Blockchain!')
        break
else:
    print('User left!') 

exit_program()